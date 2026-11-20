# 00_MASTER_BLUEPRINT_DAN_RAB_PRISM_SAFETY_GPS.md
# Rancang Bangun & Analisis Mendalam RAB Final: PRISM SAFETY GPS

> **ID Proyek:** `PRJ-PSG-01`  
> **Lokasi Direktori Lokal:** `C:\Antigravity\PRISM SAFETY GPS`  
> **Lokasi Cermin Cloud:** `G:\My Drive\Antigravity\PRISM SAFETY GPS`  
> **Blueprint SSOT Nexus:** `G:\My Drive\00_ANTIGRAVITY_NEXUS\05_PROJECT_BLUEPRINTS\02_PRISM_SAFETY_GPS_ARCHITECTURE.md`  
> **Otoritas Node:** `ROOT_1_PC_AM5` (GOLDENRATIO1618) & `ROOT_2_LAPTOP_ADVAN` (ADVAN-1701)  
> **Perancang Utama:** Ahmad Rifa'i Wibisono (Teknik Elektro FTII UHAMKA)  
> **Tanggal Sinkronisasi Final:** 5 November 2026 05:35 WIB  
> **Status:** 100% LOCKED & SYNCHRONIZED (11/11 BOM ITEMS COMPLETE — Rp207.973)  

---

## 1. Ringkasan Eksekutif, Visi, Misi, & Tujuan Sistem

### 1.1 Visi & Misi Rekayasa
- **Visi**: Menciptakan perangkat keselamatan aktif *ultra-compact* berbiaya terjangkau (**Rp207.973**) yang mampu mendeteksi insiden kecelakaan/benturan secara deterministik dan mengirimkan koordinat satelit GPS *real-time* beserta sinyal darurat otomatis (*Dual Fail-Safe SOS*).
- **Misi**: Mengoptimalkan arsitektur **Smartphone Local Edge Gateway** (Alat $\xrightarrow{\text{BLE 5.0 GATT}}$ HP $\xrightarrow{\text{WebSocket / HTTPS}}$ Server [Firebase Realtime Database](https://firebase.google.com/docs/database) $\xrightarrow{\text{Live Stream}}$ [Google Maps Platform](https://developers.google.com/maps/documentation/javascript/overview)), sehingga perangkat bebas dari beban ukuran serta konsumsi daya modem 4G internal, menghasilkan efisiensi daya hingga $19.15\text{ jam}$ pelacakan nonstop dan $> 34\text{ hari}$ dalam mode *standby*.

### 1.2 Tujuan Pokok Sistem
1. **Akuisisi Navigasi Mandiri**: Mengunci koordinat lintang-bujur dan kecepatan permukaan secara mandiri melalui modul satelit [u-blox NEO-6M GY-NEO6MV2](https://www.u-blox.com/en/product/neo-6-series) berantena keramik aktif.
2. **Deteksi Benturan & Evaluasi Imobilitas Pasca-Benturan**: Memantau vektor percepatan 3-sumbu menggunakan sensor [Analog Devices ADXL345](https://www.analog.com/en/products/adxl345.html) ($\pm 16\,g$) dan memicu alarm darurat apabila subjek berhenti bergerak selama $\Delta T_{\text{eval}} = 12\text{ detik}$ setelah benturan keras ($|\vec{a}(t)| \ge 3.8\,g$).
3. **Pengaman Putus Koneksi Mendadak (*Dead-Man's Switch*)**: Mengaktifkan sinyal darurat otomatis pada koordinat terakhir yang diketahui apabila koneksi BLE alat ke HP terputus mendadak saat benturan, atau apabila koneksi internet HP ke server terputus melalui mekanisme `onDisconnect()` di sisi server Firebase.

---

## 2. Tabel Induk RAB Final Terkunci (11 Item Lengkap Keranjang Shopee)

Seluruh 11 item perangkat keras (10 item dari tangkapan layar keranjang awal + 1 item modul cas TP4056 Type-C & Resistor pembagi tegangan senilai **Rp6.200**) telah terkunci 100% dan siap *checkout*:

| No | Toko / Vendor Shopee | Nama Komponen & Spesifikasi Teknis | Qty | Harga Satuan (IDR) | Subtotal (IDR) | Fungsi & Peran pada Rangkaian |
| :-: | :--- | :--- | :-: | ---: | ---: | :--- |
| 1 | **SeProject Makerstore** | [ESP32-C3 SuperMini BLE 5.0 RISC-V](https://www.tokopedia.com/find/esp32-c3-super-mini?utm_source=google&utm_medium=organic&utm_campaign=find) (*Tidak Solder*) | 1 pcs | Rp37.100 | **Rp37.100** | Mikrokontroler utama $160\text{ MHz}$ & pemancar BLE 5.0 GATT ke HP |
| 2 | **kolektron** | [GPS u-blox NEO-6M GY-NEO6MV2](https://www.u-blox.com/en/product/neo-6-series) + EEPROM & Antena Patch | 1 set | Rp55.000 | **Rp55.000** | Penerima sinyal satelit L1 C/A ($9600\text{ bps}$ UART1) |
| 3 | **Arduin0 Official Store** | [ADXL345 3-Axis Digital Gravity Sensor](https://www.analog.com/en/products/adxl345.html) ($\pm 16\,g$ $\text{I}^2\text{C}$/SPI) | 1 pcs | Rp46.860 | **Rp46.860** | Sensor deteksi benturan & kemiringan pasca-insiden |
| 4 | **3celectronic888** | [Baterai Li-Po 103040 $3.7\text{ V } 1200\text{ mAh}$](https://www.tokopedia.com/find/baterai-lipo-500mah?utm_source=google&utm_medium=organic&utm_campaign=find) + Proteksi PCM | 1 pcs | Rp35.227 | **Rp35.227** | Catu daya utama $4.44\text{ Wh}$ berdimensi pipih $10\times 30\times 40\text{ mm}$ |
| 5 | **Toko Komponen (Tambahan)** | [Modul Charger TP4056 USB-C + Proteksi](https://www.tokopedia.com/find/tp4056-dengan-proteksi?utm_source=google&utm_medium=organic&utm_campaign=find) & [Resistor $100\text{ k}\Omega$](https://www.tokopedia.com/dielectronics/resistor-100k-ohm-14w-025w-metal-film-10-pcs?utm_source=google&utm_medium=organic&utm_campaign=pdp) | 1 pkt | Rp6.200 | **Rp6.200** | Pengisi ulang baterai CC/CV $1\text{ A}$ & pembagi tegangan ADC `GPIO 2` |
| 6 | **Mechatronics Store** | Modul Alarm Board Buzzer 3.3V–5V (*Low Level Active Buzzer*) | 1 pcs | Rp6.990 | **Rp6.990** | Sirine peringatan lokal ber-driver transistor pengaman GPIO |
| 7 | **INDI ELEKTRIK BEKASI** | [Box Multi Plastik X1 Hitam Tebal](https://www.tokopedia.com/find/box-hitam-plastik-x1?utm_source=google&utm_medium=organic&utm_campaign=find) ($75\times 50\times 25\text{ mm}$) | 1 pcs | Rp7.071 | **Rp7.071** | Enclosure pelindung benturan untuk seluruh modul & baterai |
| 8 | **SukiTech** | [PCB Dot Matrix Thru-Hole Double Layer $4\times 6\text{ cm}$](https://www.tokopedia.com/megaarduino/pcb-bolong-pcb-lubang-4x6-cm-4-x-6-cm-dual-layer-prototype-pcb-4-6cm) | 2 pcs | Rp3.500 | **Rp7.000** | Papan dudukan sirkuit fiberglass FR4 dua sisi |
| 9 | **Roela Store** | [Saklar ON/OFF Mini Slide Switch 3-Pin SPDT](https://www.tokopedia.com/find/saklar-geser-mini?utm_source=google&utm_medium=organic&utm_campaign=find) | 2 pcs | Rp1.600 | **Rp3.200** | Saklar pemutus fisik arus baterai utama |
| 10 | **ne.elektronik** | [Kapasitor Elco $100\,\mu\text{F } 16\text{ V}$](https://www.tokopedia.com/find/elco-100uf-16v?utm_source=google&utm_medium=organic&utm_campaign=find) Auran Original | 10 pcs | Rp250 | **Rp2.500** | Tandon penyangga arus transien modul GPS & BLE |
| 11 | **Arduin0 Official Store** | Kapasitor Keramik $100\text{ nF}$ (Kode 104) | 5 pcs | Rp165 | **Rp825** | Filter penapis derau frekuensi tinggi dekat pin `VCC` IC |
| | **SUBTOTAL MURNI HARDWARE** | **11 Komponen Lengkap Siap Rakit** | | | **Rp207.973** | **100% Lengkap & Terverifikasi** |
| | **Opsi Proteksi Pengiriman** | Proteksi Kerusakan Shopee ($3 \times \text{Rp500}$) | 3 pkt | Rp500 | **Rp1.500** | Opsional pada 3 item di keranjang |
| | **GRAND TOTAL CHECKOUT** | **Total Akhir Keranjang Belanja (di Luar Ongkir Reguler)** | | | **Rp209.473** | **Siap Checkout** |

---

## 3. Model Matematis, Anggaran Daya, & State Machine Darurat

### 3.1 Kalkulasi Anggaran Daya (Power Budget) pada Baterai 103040 ($1200\text{ mAh}$)
- **Arus Kerja Pelacakan Aktif ($I_{\text{total}}$)**:
  $$I_{\text{total}} = I_{\text{ESP32-C3 (BLE)}} (18.0\text{ mA}) + I_{\text{NEO-6M}} (37.0\text{ mA}) + I_{\text{ADXL345}} (0.14\text{ mA}) = 55.14\text{ mA}$$
- **Durasi Operasional Nonstop ($\eta_{\text{reg}} = 0.88$)**:
  $$T_{\text{active}} = \frac{0.88 \times 1200\text{ mAh}}{55.14\text{ mA}} \approx 19.15\text{ jam nonstop}$$
- **Durasi Mode Siaga Parkir (*Motion-Gated Deep Sleep*, $I_{\text{sleep}} \approx 1.266\text{ mA}$)**:
  $$T_{\text{standby}} = \frac{0.88 \times 1200\text{ mAh}}{1.266\text{ mA}} \approx 834\text{ jam } (\approx 34.7\text{ hari})$$

### 3.2 Persamaan Deteksi Benturan & Evaluasi Berhenti Pasca-Benturan
1. **Magnitudo Vektor Percepatan Tiga Sumbu ($\lvert\vec{a}(t)\rvert$)**:
   $$|\vec{a}(t)| = \sqrt{a_x^2(t) + a_y^2(t) + a_z^2(t)} \ge 3.8\,g$$
2. **Evaluasi Imobilitas Pasca-Benturan ($\Delta T_{\text{eval}} = 12\text{ detik}$)**:
   $$\sigma_a^2 = \frac{1}{N}\sum_{k=1}^{N}\left(|\vec{a}_k| - \bar{a}\right)^2 < 0.03\,g^2 \quad \land \quad v_{\text{GNSS}} < 1.8\text{ km/jam } (0.5\text{ m/s})$$
   Jika terpenuhi tanpa pembatalan pengguna, status beralih ke **`STATE_SOS_IMMOBILE`**.

---

## 4. Matriks Sambungan Pin Hardware (Wiring Pinout Matrix)

| Komponen Sumber | Pin Komponen | Pin Tujuan pada **ESP32-C3 SuperMini** | Jalur Bus / Protokol | Catatan Rekayasa |
| :--- | :--- | :--- | :--- | :--- |
| **[ADXL345](https://www.analog.com/en/products/adxl345.html)** (IMU) | `VCC` & `CS` | Pin `3.3V` | Power $3.3\text{ V}$ & $\text{I}^2\text{C}$ Mode | `CS` ke `3.3V` mengaktifkan mode komunikasi $\text{I}^2\text{C}$ |
| **[ADXL345](https://www.analog.com/en/products/adxl345.html)** (IMU) | `GND` & `SDO` | Pin `GND` | Ground & Alamat `0x53` | `SDO` ke `GND` mengunci alamat $\text{I}^2\text{C}$ di `0x53` |
| **[ADXL345](https://www.analog.com/en/products/adxl345.html)** (IMU) | `SDA` | **`GPIO 8`** | $\text{I}^2\text{C}$ Data | Default SDA ESP32-C3 SuperMini |
| **[ADXL345](https://www.analog.com/en/products/adxl345.html)** (IMU) | `SCL` | **`GPIO 9`** | $\text{I}^2\text{C}$ Clock | Default SCL ESP32-C3 SuperMini |
| **[ADXL345](https://www.analog.com/en/products/adxl345.html)** (IMU) | `INT1` | **`GPIO 3`** | Interrupt Wakeup | Membangunkan MCU dari *Deep Sleep* saat benturan |
| **[u-blox NEO-6M](https://www.u-blox.com/en/product/neo-6-series)** (GPS) | `VCC` & `GND` | Pin `3.3V` & `GND` | Power + Filter Elco $100\,\mu\text{F}$ | Pasang Elco $100\,\mu\text{F}$ + Keramik $100\text{ nF}$ paralel di dekat GPS |
| **[u-blox NEO-6M](https://www.u-blox.com/en/product/neo-6-series)** (GPS) | `TX` | **`GPIO 20` (RX0)** | `HardwareSerial(1)` RX | Kalimat NMEA dari GPS masuk ke RX ESP32-C3 |
| **[u-blox NEO-6M](https://www.u-blox.com/en/product/neo-6-series)** (GPS) | `RX` | **`GPIO 21` (TX0)** | `HardwareSerial(1)` TX | Jalur perintah konfigurasi dari ESP32-C3 ke GPS |
| **Modul Alarm Buzzer** | `VCC`, `GND`, `I/O` | `3.3V`, `GND`, **`GPIO 4`** | Digital Control | *Low-level/Active trigger* via transistor driver onboard |
| **Pembagi ADC Baterai** | Titik Tengah $2\times 100\text{ k}\Omega$ | **`GPIO 2` (ADC1_CH2)** | Analog Input ($V_{\text{bat}}/2$) | Membaca persentase baterai $103040$ secara aman |
| **Modul Cas TP4056** | `OUT+` (via Saklar) & `OUT-` | Pin `5V` & `GND` | Main Battery Power | Mengisi baterai via USB-C & menyuplai LDO ESP32-C3 |
