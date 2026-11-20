/**
 * ============================================================================
 * PRISM SAFETY GPS — Firmware Utama ESP32-C3 SuperMini (BLE 5.0 + GPS + IMU)
 * ============================================================================
 * Target MCU     : ESP32-C3 SuperMini (RISC-V 32-bit @ 160MHz)
 * Sensor IMU     : Analog Devices ADXL345 (I2C: SDA=GPIO8, SCL=GPIO9, INT1=GPIO3)
 * Modul GNSS     : u-blox NEO-6M GY-NEO6MV2 (UART1: RX=GPIO20, TX=GPIO21 @ 9600)
 * Alarm Lokal    : Active Buzzer 3.3V (GPIO4)
 * Sensor Baterai : Pembagi Tegangan 2x 100kOhm Li-Po 103040 (GPIO2 / ADC1_CH2)
 * Protokol Lokal : Bluetooth Low Energy (BLE 5.0 GATT Server Notify -> HP)
 * ============================================================================
 */

#include <Arduino.h>
#include <Wire.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#include <math.h>

// --- Definisi Pin ESP32-C3 SuperMini ---
#define PIN_I2C_SDA       8
#define PIN_I2C_SCL       9
#define PIN_ADXL_INT1     3
#define PIN_GPS_RX        20  // Hubungkan ke pin TX pada NEO-6M
#define PIN_GPS_TX        21  // Hubungkan ke pin RX pada NEO-6M
#define PIN_BUZZER        4
#define PIN_BAT_ADC       2

// --- Konstanta Alamat I2C ADXL345 ---
#define ADXL345_ADDR      0x53
#define REG_POWER_CTL     0x2D
#define REG_DATA_FORMAT   0x31
#define REG_DATAX0        0x32

// --- Parameter Ambang Deteksi Benturan & Berhenti Bergerak ---
#define IMPACT_THRESH_G         3.8f    // Ambang benturan keras (dalam satuan g)
#define PRE_SHOCK_THRESH_G      2.5f    // Ambang guncangan awal (pre-alert)
#define STATIC_VAR_THRESH       0.03f   // Ambang varians percepatan saat diam (g^2)
#define STATIC_SPEED_KMH        1.8f    // Ambang kecepatan dianggap berhenti (< 0.5 m/s)
#define EVAL_WINDOW_MS          12000UL // Jendela evaluasi pasca-benturan (12 detik)
#define BLE_HEARTBEAT_MS        250UL   // Interval pengiriman paket telemetri BLE (4 Hz)

// --- UUID Layanan & Karakteristik BLE GATT ---
#define SERVICE_UUID            "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHAR_TELEMETRY_UUID     "beb5483e-36e1-4688-b7f5-ea07361b26a8"
#define CHAR_COMMAND_UUID       "82b97611-9921-4712-a1b2-3456789abcde"

// --- State Machine Keselamatan ---
enum SafetyState {
  STATE_NORMAL_TRACKING = 0,
  STATE_WARNING_IMPACT  = 1,
  STATE_SOS_IMMOBILE    = 2
};

SafetyState currentState = STATE_NORMAL_TRACKING;
unsigned long impactTimestampMs = 0;
unsigned long lastBleTxMs = 0;
float peakImpactG = 0.0f;

// Buffer Varians Percepatan untuk Deteksi Berhenti Pasca-Benturan
#define SAMPLE_WIN 25
float magHistory[SAMPLE_WIN];
int sampleIdx = 0;

// Data GPS Sederhana (Parser NMEA $GPRMC / $GPGGA)
double gpsLat = -6.255000;
double gpsLng = 107.150000;
float gpsSpeedKmh = 0.0f;
bool gpsFixValid = false;
String nmeaBuffer = "";

HardwareSerial gpsSerial(1);
BLEServer* pServer = nullptr;
BLECharacteristic* pTelemetryChar = nullptr;
bool deviceConnected = false;

// Callback Koneksi BLE
class ServerCallbacks : public BLEServerCallbacks {
  void onConnect(BLEServer* pServer) override {
    deviceConnected = true;
  }
  void onDisconnect(BLEServer* pServer) override {
    deviceConnected = false;
    BLEDevice::startAdvertising(); // Langsung iklan ulang jika putus
  }
};

// Callback Perintah dari HP (Misal: Pengguna Menekan Tombol "SAYA AMAN / BATAL SOS")
class CommandCallbacks : public BLECharacteristicCallbacks {
  void onWrite(BLECharacteristic* pCharacteristic) override {
    String cmd = pCharacteristic->getValue().c_str();
    if (cmd == "CANCEL_SOS" || cmd == "RESET") {
      currentState = STATE_NORMAL_TRACKING;
      peakImpactG = 0.0f;
      digitalWrite(PIN_BUZZER, LOW);
    }
  }
};

void initADXL345() {
  Wire.begin(PIN_I2C_SDA, PIN_I2C_SCL);
  // Set Range +-16g, Full Resolution (13-bit, 3.9 mg/LSB)
  Wire.beginTransmission(ADXL345_ADDR);
  Wire.write(REG_DATA_FORMAT);
  Wire.write(0x0B);
  Wire.endTransmission();

  // Aktifkan Measurement Mode
  Wire.beginTransmission(ADXL345_ADDR);
  Wire.write(REG_POWER_CTL);
  Wire.write(0x08);
  Wire.endTransmission();
}

void readADXL345(float &ax, float &ay, float &az, float &magG) {
  Wire.beginTransmission(ADXL345_ADDR);
  Wire.write(REG_DATAX0);
  Wire.endTransmission(false);
  Wire.requestFrom(ADXL345_ADDR, 6, true);

  if (Wire.available() >= 6) {
    int16_t rawX = (int16_t)(Wire.read() | (Wire.read() << 8));
    int16_t rawY = (int16_t)(Wire.read() | (Wire.read() << 8));
    int16_t rawZ = (int16_t)(Wire.read() | (Wire.read() << 8));
    // Faktor skala Full-Res ADXL345 = 0.0039 g/LSB
    ax = rawX * 0.0039f;
    ay = rawY * 0.0039f;
    az = rawZ * 0.0039f;
    magG = sqrtf(ax * ax + ay * ay + az * az);
  }
}

float computeAccelVariance() {
  float mean = 0.0f;
  for (int i = 0; i < SAMPLE_WIN; i++) mean += magHistory[i];
  mean /= SAMPLE_WIN;

  float var = 0.0f;
  for (int i = 0; i < SAMPLE_WIN; i++) {
    float diff = magHistory[i] - mean;
    var += diff * diff;
  }
  return var / SAMPLE_WIN;
}

// Konversi Koordinat NMEA (ddmm.mmmm) ke Decimal Degrees
double nmeaToDecimal(String coord, String dir) {
  if (coord.length() < 4) return 0.0;
  int dotIdx = coord.indexOf('.');
  int degLen = (dotIdx > 4) ? 3 : 2;
  double deg = coord.substring(0, degLen).toDouble();
  double min = coord.substring(degLen).toDouble();
  double dec = deg + (min / 60.0);
  if (dir == "S" || dir == "W") dec = -dec;
  return dec;
}

void parseGPRMC(String line) {
  // Format: $GPRMC,hhmmss.ss,A,llll.ll,a,yyyyy.yy,a,x.x,x.x,ddmmyy,,,*hh
  int idx[12];
  int count = 0;
  for (int i = 0; i < line.length() && count < 12; i++) {
    if (line[i] == ',') idx[count++] = i;
  }
  if (count >= 8) {
    String status = line.substring(idx[1] + 1, idx[2]);
    if (status == "A") {
      gpsFixValid = true;
      String rawLat = line.substring(idx[2] + 1, idx[3]);
      String latDir = line.substring(idx[3] + 1, idx[4]);
      String rawLng = line.substring(idx[4] + 1, idx[5]);
      String lngDir = line.substring(idx[5] + 1, idx[6]);
      String knots  = line.substring(idx[6] + 1, idx[7]);
      gpsLat = nmeaToDecimal(rawLat, latDir);
      gpsLng = nmeaToDecimal(rawLng, lngDir);
      gpsSpeedKmh = knots.toFloat() * 1.852f;
    } else {
      gpsFixValid = false;
    }
  }
}

void pollGPS() {
  while (gpsSerial.available()) {
    char c = (char)gpsSerial.read();
    if (c == '\n') {
      if (nmeaBuffer.startsWith("$GPRMC") || nmeaBuffer.startsWith("$GNRMC")) {
        parseGPRMC(nmeaBuffer);
      }
      nmeaBuffer = "";
    } else if (c != '\r') {
      nmeaBuffer += c;
    }
  }
}

float readBatteryVoltage() {
  int mv = analogReadMilliVolts(PIN_BAT_ADC);
  return (mv * 2.0f) / 1000.0f; // Rasio pembagi tegangan 100k / 100k = 2x
}

void setup() {
  Serial.begin(115200);
  pinMode(PIN_BUZZER, OUTPUT);
  digitalWrite(PIN_BUZZER, LOW);

  gpsSerial.begin(9600, SERIAL_8N1, PIN_GPS_RX, PIN_GPS_TX);
  initADXL345();

  for (int i = 0; i < SAMPLE_WIN; i++) magHistory[i] = 1.0f;

  // Inisialisasi BLE 5.0 GATT Server
  BLEDevice::init("PRISM-SAFETY-GPS");
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new ServerCallbacks());

  BLEService* pService = pServer->createService(SERVICE_UUID);
  pTelemetryChar = pService->createCharacteristic(
    CHAR_TELEMETRY_UUID,
    BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY
  );
  pTelemetryChar->addDescriptor(new BLE2902());

  BLECharacteristic* pCmdChar = pService->createCharacteristic(
    CHAR_COMMAND_UUID,
    BLECharacteristic::PROPERTY_WRITE
  );
  pCmdChar->setCallbacks(new CommandCallbacks());

  pService->start();
  BLEAdvertising* pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pAdvertising->setScanResponse(true);
  BLEDevice::startAdvertising();
}

void loop() {
  pollGPS();

  float ax = 0, ay = 0, az = 0, magG = 1.0f;
  readADXL345(ax, ay, az, magG);
  magHistory[sampleIdx] = magG;
  sampleIdx = (sampleIdx + 1) % SAMPLE_WIN;

  unsigned long now = millis();

  // 1. Deteksi Benturan Keras (Impact Trigger)
  if (magG >= IMPACT_THRESH_G) {
    if (magG > peakImpactG) peakImpactG = magG;
    if (currentState == STATE_NORMAL_TRACKING) {
      currentState = STATE_WARNING_IMPACT;
      impactTimestampMs = now;
    }
  }

  // 2. Evaluasi Pasca-Benturan (Apakah Berhenti Bergerak?)
  if (currentState == STATE_WARNING_IMPACT) {
    unsigned long elapsed = now - impactTimestampMs;
    // Buzzer berbunyi putus-putus selama masa evaluasi 12 detik
    digitalWrite(PIN_BUZZER, ((elapsed / 250) % 2 == 0) ? HIGH : LOW);

    if (elapsed >= EVAL_WINDOW_MS) {
      float accVar = computeAccelVariance();
      bool isStationary = (accVar < STATIC_VAR_THRESH) && (gpsSpeedKmh < STATIC_SPEED_KMH);
      if (isStationary) {
        currentState = STATE_SOS_IMMOBILE;
        digitalWrite(PIN_BUZZER, HIGH); // Bunyi sirine kontinu
      } else {
        // Subjek masih bergerak normal setelah guncangan -> kembali ke normal
        currentState = STATE_NORMAL_TRACKING;
        peakImpactG = 0.0f;
        digitalWrite(PIN_BUZZER, LOW);
      }
    }
  }

  // 3. Pengiriman Paket Telemetri JSON via BLE Notify ke HP (4 Hz)
  if (now - lastBleTxMs >= BLE_HEARTBEAT_MS) {
    lastBleTxMs = now;
    float vBat = readBatteryVoltage();
    float accVar = computeAccelVariance();

    char payload[160];
    snprintf(
      payload, sizeof(payload),
      "{\"st\":%d,\"lat\":%.6f,\"lng\":%.6f,\"spd\":%.1f,\"g\":%.2f,\"pk\":%.2f,\"var\":%.4f,\"bat\":%.2f,\"fix\":%d}",
      (int)currentState, gpsLat, gpsLng, gpsSpeedKmh, magG, peakImpactG, accVar, vBat, gpsFixValid ? 1 : 0
    );

    if (deviceConnected) {
      pTelemetryChar->setValue((uint8_t*)payload, strlen(payload));
      pTelemetryChar->notify();
    }
    Serial.println(payload);
  }

  delay(20); // Sampling IMU ~50 Hz
}
