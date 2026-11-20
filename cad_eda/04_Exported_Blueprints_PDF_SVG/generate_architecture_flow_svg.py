"""generate_architecture_flow_svg.py
Generates 02_System_Architecture_Flow.svg (A4 Landscape 297x210 mm)
Compliant with ISO 7200 Title Block, 96 DPI calibration, Zero Text Collision.
"""

from pathlib import Path

DPI_SCALE = 3.779527559  # 96 DPI: 1 mm = 3.779527559 px
WIDTH_MM = 297.0
HEIGHT_MM = 210.0
W_PX = WIDTH_MM * DPI_SCALE
H_PX = HEIGHT_MM * DPI_SCALE

# Margin
M_LEFT = 20.0
M_TOP = 10.0
M_RIGHT = 10.0
M_BOTTOM = 10.0

X0 = M_LEFT
Y0 = M_TOP
X1 = WIDTH_MM - M_RIGHT
Y1 = HEIGHT_MM - M_BOTTOM

TB_W = 180.0
TB_H = 40.0
TB_X0 = X1 - TB_W
TB_Y0 = Y1 - TB_H
TB_X1 = X1
TB_Y1 = Y1

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH_MM} {HEIGHT_MM}" width="{W_PX:.2f}px" height="{H_PX:.2f}px">')
svg.append('''  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#1E293B" />
    </linearGradient>
    <linearGradient id="cardGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="100%" stop-color="#38BDF8" />
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D4AF37" />
      <stop offset="100%" stop-color="#F59E0B" />
    </linearGradient>
    <linearGradient id="crimsonGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E11D48" />
      <stop offset="100%" stop-color="#FB7185" />
    </linearGradient>
    <marker id="arrowCyan" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#00F0FF" />
    </marker>
    <marker id="arrowGold" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#D4AF37" />
    </marker>
    <marker id="arrowRed" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#EF4444" />
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#10B981" />
    </marker>
    <style>
      .paper { fill: #FFFFFF; stroke: #000000; stroke-width: 0.70; }
      .border { fill: none; stroke: #000000; stroke-width: 0.50; }
      .title-block-line { stroke: #000000; stroke-width: 0.25; }
      .text-title { font-family: "Segoe UI", Arial, sans-serif; font-size: 3.2px; font-weight: bold; fill: #000000; }
      .text-sub { font-family: "Segoe UI", Arial, sans-serif; font-size: 2.2px; font-weight: bold; fill: #334155; }
      .text-body { font-family: "Segoe UI", Arial, sans-serif; font-size: 1.8px; fill: #000000; }
      .text-caption { font-family: "Segoe UI", Arial, sans-serif; font-size: 1.4px; fill: #64748B; }
      .node-hdr { font-family: "Segoe UI", Arial, sans-serif; font-size: 2.4px; font-weight: bold; fill: #FFFFFF; }
      .node-txt { font-family: "Segoe UI", Arial, sans-serif; font-size: 1.7px; fill: #E2E8F0; }
      .node-sub { font-family: "Segoe UI", Arial, sans-serif; font-size: 1.4px; fill: #94A3B8; }
      .accent-cyan { fill: #00F0FF; font-weight: bold; }
      .accent-gold { fill: #F59E0B; font-weight: bold; }
      .accent-red { fill: #F87171; font-weight: bold; }
      .accent-green { fill: #34D399; font-weight: bold; }
    </style>
  </defs>''')

# 1. Base Paper & Border
svg.append(f'  <!-- Sheet Canvas: A4 Landscape ({WIDTH_MM} x {HEIGHT_MM} mm) -->')
svg.append(f'  <rect x="0" y="0" width="{WIDTH_MM}" height="{HEIGHT_MM}" class="paper"/>')
svg.append(f'  <rect x="{X0}" y="{Y0}" width="{X1 - X0}" height="{Y1 - Y0}" class="border"/>')

# Title Header at Top Left
svg.append(f'  <!-- Diagram Title Banner -->')
svg.append(f'  <rect x="{X0 + 2}" y="{Y0 + 2}" width="263" height="11" rx="1.5" fill="#0F172A" stroke="#00F0FF" stroke-width="0.4"/>')
svg.append(f'  <text x="{X0 + 6}" y="{Y0 + 6.5}" font-family="Segoe UI" font-size="3.2px" font-weight="bold" fill="#00F0FF">PRISM SAFETY GPS (PRJ-PSG-01) — SISTEM ARSITEKTUR &amp; TOPOLOGI GATEWAY</text>')
svg.append(f'  <text x="{X0 + 6}" y="{Y0 + 10}" font-family="Segoe UI" font-size="2.0px" fill="#94A3B8">Smartphone Local Edge Gateway (BLE 5.0 GATT → WebSocket/Firebase → Google Maps) | Dual Fail-Safe SOS Machine</text>')

# 2. Main Section 1: Edge Gateway Architecture Flow (Y: 25 to 88 mm)
# Column 1: PRISM SAFETY GPS Hardware Node (X: 24 to 88)
svg.append(f'''
  <!-- NODE 1: PRISM SAFETY GPS HARDWARE -->
  <g transform="translate({X0 + 4}, 25)">
    <rect width="66" height="66" rx="2" fill="url(#cardGrad1)" stroke="#38BDF8" stroke-width="0.5"/>
    <rect width="66" height="7" rx="2" fill="#0284C7"/>
    <text x="4" y="4.8" class="node-hdr">1. PRISM SAFETY GPS (EDGE SENSOR)</text>
    
    <!-- Sub-blocks inside hardware -->
    <rect x="3" y="10" width="60" height="11" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="14.5" class="node-txt"><tspan class="accent-cyan">ESP32-C3 SuperMini</tspan> RISC-V 32-bit @ 160MHz</text>
    <text x="5" y="18.5" class="node-sub">BLE 5.0 GATT Server, FreeRTOS, Low-Power Standby</text>
    
    <rect x="3" y="23" width="60" height="11" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="27.5" class="node-txt"><tspan class="accent-cyan">ADXL345</tspan> 3-Axis IMU (I2C 0x53, SDA:8, SCL:9)</text>
    <text x="5" y="31.5" class="node-sub">Ambang Benturan: |a(t)| ≥ 3.8g, Interupsi HW INT1: GPIO3</text>
    
    <rect x="3" y="36" width="60" height="11" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="40.5" class="node-txt"><tspan class="accent-cyan">u-blox NEO-6M</tspan> GNSS (UART1 RX0:20, TX0:21)</text>
    <text x="5" y="44.5" class="node-sub">Antena Keramik 25x25mm Menghadap Langit, 5Hz Update</text>
    
    <rect x="3" y="49" width="60" height="13" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="53.5" class="node-txt"><tspan class="accent-gold">Power &amp; Alarm</tspan>: Li-Po 103040 1200mAh + TP4056</text>
    <text x="5" y="57.5" class="node-sub">Pembagi R1-R2 (2x100kΩ) → ADC1_CH2, Active Buzzer: GPIO4</text>
    <text x="5" y="60.5" class="node-sub">Filter Decoupling: C1 100uF + C2 100nF, C3 100uF + C4 100nF</text>
  </g>
''')

# Transmission arrow 1: BLE 5.0 GATT
svg.append(f'''
  <!-- ARROW 1: BLE 5.0 GATT -->
  <g transform="translate(94, 52)">
    <line x1="0" y1="0" x2="16" y2="0" stroke="#00F0FF" stroke-width="1.2" stroke-dasharray="3,1.5" marker-end="url(#arrowCyan)"/>
    <rect x="1" y="-10" width="14" height="8" rx="1" fill="#0F172A" stroke="#00F0FF" stroke-width="0.3"/>
    <text x="8" y="-5.5" font-family="Segoe UI" font-size="1.5px" font-weight="bold" fill="#00F0FF" text-anchor="middle">BLE 5.0 GATT</text>
    <text x="8" y="-3.2" font-family="Segoe UI" font-size="1.2px" fill="#94A3B8" text-anchor="middle">4 Hz / 250ms</text>
  </g>
''')

# Column 2: Smartphone Local Edge Gateway (X: 114 to 178)
svg.append(f'''
  <!-- NODE 2: SMARTPHONE LOCAL EDGE GATEWAY -->
  <g transform="translate(112, 25)">
    <rect width="64" height="66" rx="2" fill="url(#cardGrad1)" stroke="#38BDF8" stroke-width="0.5"/>
    <rect width="64" height="7" rx="2" fill="#2563EB"/>
    <text x="4" y="4.8" class="node-hdr">2. SMARTPHONE LOCAL EDGE GATEWAY</text>
    
    <rect x="3" y="10" width="58" height="12" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="14.5" class="node-txt"><tspan class="accent-cyan">Web Bluetooth / Companion PWA</tspan></text>
    <text x="5" y="18.5" class="node-sub">UUID: 4fafc201-1fb5-459e-8fcc-c5c9c331914b</text>
    <text x="5" y="21.0" class="node-sub">Char: beb5483e (Notify), 82b97611 (Command)</text>
    
    <rect x="3" y="24" width="58" height="13" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="28.5" class="node-txt"><tspan class="accent-gold">Dual Fail-Safe Evaluator</tspan></text>
    <text x="5" y="32.5" class="node-sub">Countdown Timer 12s | Evaluasi Varians Percepatan</text>
    <text x="5" y="35.5" class="node-sub">Tombol Pembatalan Darurat: "CANCEL_SOS"</text>
    
    <rect x="3" y="39" width="58" height="13" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="43.5" class="node-txt"><tspan class="accent-red">Dead-Man's Switch Level 1</tspan></text>
    <text x="5" y="47.5" class="node-sub">Deteksi Putus BLE Seketika saat Impact Terjadi</text>
    <text x="5" y="50.5" class="node-sub">Otomatis Teruskan Koordinat Terakhir (x_last, y_last)</text>

    <rect x="3" y="54" width="58" height="9" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="58.5" class="node-txt"><tspan class="accent-green">Jalur Seluler 4G/5G / Wi-Fi</tspan> Backhaul</text>
    <text x="5" y="61.5" class="node-sub">Kompresi Paket JSON Latensi Rendah (&lt; 150ms)</text>
  </g>
''')

# Transmission arrow 2: WebSocket / HTTPS
svg.append(f'''
  <!-- ARROW 2: WSS / HTTPS -->
  <g transform="translate(180, 52)">
    <line x1="0" y1="0" x2="16" y2="0" stroke="#F59E0B" stroke-width="1.2" stroke-dasharray="3,1.5" marker-end="url(#arrowGold)"/>
    <rect x="1" y="-10" width="14" height="8" rx="1" fill="#0F172A" stroke="#F59E0B" stroke-width="0.3"/>
    <text x="8" y="-5.5" font-family="Segoe UI" font-size="1.5px" font-weight="bold" fill="#F59E0B" text-anchor="middle">WSS / HTTPS</text>
    <text x="8" y="-3.2" font-family="Segoe UI" font-size="1.2px" fill="#94A3B8" text-anchor="middle">JSON Stream</text>
  </g>
''')

# Column 3: Cloud Server & Google Maps Live Dashboard (X: 200 to 282)
svg.append(f'''
  <!-- NODE 3: CLOUD & GOOGLE MAPS LIVE STREAM -->
  <g transform="translate(198, 25)">
    <rect width="85" height="66" rx="2" fill="url(#cardGrad1)" stroke="#38BDF8" stroke-width="0.5"/>
    <rect width="85" height="7" rx="2" fill="#7C3AED"/>
    <text x="4" y="4.8" class="node-hdr">3. CLOUD BACKBONE &amp; GOOGLE MAPS DASHBOARD</text>
    
    <rect x="3" y="10" width="79" height="13" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="14.5" class="node-txt"><tspan class="accent-gold">Firebase Realtime Database</tspan></text>
    <text x="5" y="18.5" class="node-sub">Sinkronisasi State Global, Telemetri Real-Time</text>
    <text x="5" y="21.5" class="node-sub">Dead-Man's Switch Level 2: Hook onDisconnect() Cloud</text>
    
    <rect x="3" y="25" width="79" height="13" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="29.5" class="node-txt"><tspan class="accent-cyan">Google Maps JavaScript API V3</tspan></text>
    <text x="5" y="33.5" class="node-sub">Live Breadcrumb Tracking, Heading Vector, Geofencing</text>
    <text x="5" y="36.5" class="node-sub">Popup Telemetri: Kecepatan, G-Force Peak, Status Baterai %</text>
    
    <rect x="3" y="40" width="79" height="23" rx="1" fill="#1E293B" stroke="#475569" stroke-width="0.3"/>
    <text x="5" y="44.5" class="node-txt"><tspan class="accent-red">Emergency Dispatch &amp; Family Notification</tspan></text>
    <text x="5" y="48.5" class="node-sub">• Notifikasi Telegram Bot / WhatsApp / SMS Darurat</text>
    <text x="5" y="52.0" class="node-sub">• Pin Peta Titik Benturan Presisi &amp; Rute Terdekat ke RS</text>
    <text x="5" y="55.5" class="node-sub">• Log Forensik: Profil Akselerasi 3-Sumbu Pasca-Insiden</text>
    <text x="5" y="59.0" class="node-sub">• Peringatan Audio &amp; Visual Real-Time pada Dashboard Petugas</text>
  </g>
''')

# 3. Main Section 2: Dual Fail-Safe SOS State Machine (Y: 96 to 158 mm)
svg.append(f'''
  <!-- SECTION 2: DUAL FAIL-SAFE SOS STATE MACHINE -->
  <g transform="translate({X0 + 4}, 95)">
    <!-- Outer Container -->
    <rect width="259" height="63" rx="2" fill="#0B132B" stroke="#D4AF37" stroke-width="0.5"/>
    <rect width="259" height="6.5" rx="2" fill="#B45309"/>
    <text x="4" y="4.5" class="node-hdr">STATE MACHINE: DUAL FAIL-SAFE SOS &amp; IMPACT IMMOBILITY DETECTION</text>
    
    <!-- State 0: Normal Tracking -->
    <g transform="translate(6, 12)">
      <rect width="68" height="45" rx="2" fill="#1E293B" stroke="#10B981" stroke-width="0.6"/>
      <rect width="68" height="6" rx="2" fill="#065F46"/>
      <text x="4" y="4.2" class="node-hdr" fill="#34D399">STATE 0: NORMAL TRACKING</text>
      <text x="4" y="11" class="node-txt">Kondisi Normal Berkendara</text>
      <text x="4" y="15" class="node-sub">• Akselerasi dinamis: |a(t)| &lt; 2.5g</text>
      <text x="4" y="18.5" class="node-sub">• Kecepatan GNSS: v ≥ 0.0 km/h</text>
      <text x="4" y="22" class="node-sub">• Laju Telemetri BLE: 4 Hz (250ms)</text>
      <text x="4" y="25.5" class="node-sub">• Buzzer: MATI (Low)</text>
      <text x="4" y="29" class="node-sub">• Indikator LED ESP32: Berkedip 1Hz</text>
      <text x="4" y="33" class="node-txt"><tspan class="accent-green">Siaga Aktif (Standby Proteksi)</tspan></text>
      <text x="4" y="37" class="node-sub">Loop I2C &amp; UART NMEA parser berjalan</text>
      <text x="4" y="40.5" class="node-sub">Monitoring Voltase Baterai Li-Po 103040</text>
    </g>
    
    <!-- Transition 0 -> 1 -->
    <g transform="translate(76, 30)">
      <line x1="0" y1="0" x2="16" y2="0" stroke="#F59E0B" stroke-width="1.0" marker-end="url(#arrowGold)"/>
      <rect x="1" y="-8.5" width="14" height="6.5" rx="1" fill="#1E293B" stroke="#F59E0B" stroke-width="0.3"/>
      <text x="8" y="-4.5" font-family="Segoe UI" font-size="1.4px" font-weight="bold" fill="#F59E0B" text-anchor="middle">|a(t)| ≥ 3.8g</text>
      <text x="8" y="-2.5" font-family="Segoe UI" font-size="1.1px" fill="#94A3B8" text-anchor="middle">Impact Spike</text>
    </g>

    <!-- State 1: Warning Impact -->
    <g transform="translate(94, 12)">
      <rect width="72" height="45" rx="2" fill="#1E293B" stroke="#F59E0B" stroke-width="0.6"/>
      <rect width="72" height="6" rx="2" fill="#92400E"/>
      <text x="4" y="4.2" class="node-hdr" fill="#FBBF24">STATE 1: WARNING IMPACT</text>
      <text x="4" y="11" class="node-txt">Peringatan Benturan Terdeteksi</text>
      <text x="4" y="15" class="node-sub">• Mulai Timer Evaluasi: <tspan class="accent-gold">ΔT_eval = 12 s</tspan></text>
      <text x="4" y="18.5" class="node-sub">• Buzzer: Pulsa Intermiten (Beep... Beep...)</text>
      <text x="4" y="22" class="node-sub">• Layar HP: Popup Konfirmasi Darurat</text>
      <text x="4" y="25.5" class="node-sub">• Rekam Peak G-Force &amp; Titik Lokasi</text>
      <text x="4" y="29.5" class="node-txt"><tspan class="accent-cyan">Opsi Pembatalan (False Alarm):</tspan></text>
      <text x="4" y="33.5" class="node-sub">Jika Pengguna Menekan "SAYA AMAN",</text>
      <text x="4" y="37" class="node-sub">Kirim "CANCEL_SOS" via BLE → Kembali</text>
      <text x="4" y="40.5" class="node-sub">ke STATE 0 secara instan.</text>
    </g>
    
    <!-- Transition 1 -> 0 (Cancel SOS) -->
    <path d="M 120 12 C 110 5, 80 5, 60 12" fill="none" stroke="#10B981" stroke-width="0.8" stroke-dasharray="2,1" marker-end="url(#arrowGreen)"/>
    <text x="90" y="7.5" font-family="Segoe UI" font-size="1.2px" font-weight="bold" fill="#10B981" text-anchor="middle">Pengguna Batal: CANCEL_SOS</text>

    <!-- Transition 1 -> 2 -->
    <g transform="translate(168, 30)">
      <line x1="0" y1="0" x2="16" y2="0" stroke="#EF4444" stroke-width="1.0" marker-end="url(#arrowRed)"/>
      <rect x="0" y="-10" width="16" height="8.5" rx="1" fill="#1E293B" stroke="#EF4444" stroke-width="0.3"/>
      <text x="8" y="-6.5" font-family="Segoe UI" font-size="1.3px" font-weight="bold" fill="#EF4444" text-anchor="middle">ΔT = 12 s Lolos</text>
      <text x="8" y="-4.2" font-family="Segoe UI" font-size="1.1px" fill="#E2E8F0" text-anchor="middle">v &lt; 0.5 m/s</text>
      <text x="8" y="-2.2" font-family="Segoe UI" font-size="1.1px" fill="#94A3B8" text-anchor="middle">σ_a² &lt; 0.03 g²</text>
    </g>

    <!-- State 2: SOS Immobile -->
    <g transform="translate(186, 12)">
      <rect width="68" height="45" rx="2" fill="#1E293B" stroke="#EF4444" stroke-width="0.8"/>
      <rect width="68" height="6" rx="2" fill="#991B1B"/>
      <text x="4" y="4.2" class="node-hdr" fill="#F87171">STATE 2: SOS IMMOBILE (DARURAT)</text>
      <text x="4" y="11" class="node-txt"><tspan class="accent-red">KORBAN TIDAK BERGERAK</tspan></text>
      <text x="4" y="15" class="node-sub">• Buzzer: Bunyi Sirene Kontinu Keras</text>
      <text x="4" y="18.5" class="node-sub">• Push Notifikasi Darurat ke Keluarga &amp; RS</text>
      <text x="4" y="22" class="node-sub">• Transmisi Koordinat GPS Darurat (Lat, Lng)</text>
      <text x="4" y="25.5" class="node-sub">• Google Maps: Peringatan Merah Berkedip</text>
      <text x="4" y="29.5" class="node-txt"><tspan class="accent-gold">Dead-Man's Fail-Safe Backup:</tspan></text>
      <text x="4" y="33.5" class="node-sub">Jika BLE Terputus Mendadak Saat Tabrakan,</text>
      <text x="4" y="37" class="node-sub">Gateway Langsung Memicu SOS pada Titik</text>
      <text x="4" y="40.5" class="node-sub">Terakhir Tanpa Menunggu Respon Korban.</text>
    </g>
  </g>
''')

# 4. ISO 7200 Title Block (Bottom Right: 180 x 40 mm)
svg.append(f'''
  <!-- ISO 7200 / UHAMKA TITLE BLOCK (180 x 40 mm) -->
  <g id="TitleBlock">
    <!-- Outer Title Block Frame -->
    <rect x="{TB_X0}" y="{TB_Y0}" width="{TB_W}" height="{TB_H}" fill="#FFFFFF" class="border"/>
    
    <!-- Horizontal Dividers -->
    <line x1="{TB_X0}" y1="{TB_Y0 + 13}" x2="{TB_X1}" y2="{TB_Y0 + 13}" class="title-block-line"/>
    <line x1="{TB_X0}" y1="{TB_Y0 + 26}" x2="{TB_X1}" y2="{TB_Y0 + 26}" class="title-block-line"/>
    
    <!-- Vertical Dividers -->
    <line x1="{TB_X0 + 105}" y1="{TB_Y0}" x2="{TB_X0 + 105}" y2="{TB_Y0 + 13}" class="title-block-line"/>
    <line x1="{TB_X0 + 145}" y1="{TB_Y0}" x2="{TB_X0 + 145}" y2="{TB_Y0 + 13}" class="title-block-line"/>
    <line x1="{TB_X0 + 60}" y1="{TB_Y0 + 13}" x2="{TB_X0 + 60}" y2="{TB_Y1}" class="title-block-line"/>
    <line x1="{TB_X0 + 120}" y1="{TB_Y0 + 13}" x2="{TB_X0 + 120}" y2="{TB_Y1}" class="title-block-line"/>
    <line x1="{TB_X0 + 155}" y1="{TB_Y0 + 26}" x2="{TB_X0 + 155}" y2="{TB_Y1}" class="title-block-line"/>

    <!-- Row 1: Left - Institution -->
    <text x="{TB_X0 + 3}" y="{TB_Y0 + 4.5}" class="text-caption">LEMBAGA / INSTITUSI PENDIDIKAN:</text>
    <text x="{TB_X0 + 3}" y="{TB_Y0 + 8.5}" class="text-sub">UNIVERSITAS MUHAMMADIYAH PROF. DR. HAMKA</text>
    <text x="{TB_X0 + 3}" y="{TB_Y0 + 11.5}" class="text-caption">FTII — PROGRAM STUDI TEKNIK ELEKTRO | PRISM ENGINEERING HUB</text>

    <!-- Row 1: Middle - Projection -->
    <text x="{TB_X0 + 107}" y="{TB_Y0 + 4.5}" class="text-caption">METODE PROYEKSI:</text>
    <!-- Third Angle Symbol -->
    <polygon points="{TB_X0 + 115},{TB_Y0 + 6} {TB_X0 + 123},{TB_Y0 + 7.5} {TB_X0 + 123},{TB_Y0 + 10.5} {TB_X0 + 115},{TB_Y0 + 12}" fill="none" stroke="#000" stroke-width="0.3"/>
    <circle cx="{TB_X0 + 130}" cy="{TB_Y0 + 9}" r="1.5" fill="none" stroke="#000" stroke-width="0.3"/>
    <circle cx="{TB_X0 + 130}" cy="{TB_Y0 + 9}" r="3.2" fill="none" stroke="#000" stroke-width="0.3"/>
    <line x1="{TB_X0 + 113}" y1="{TB_Y0 + 9}" x2="{TB_X0 + 135}" y2="{TB_Y0 + 9}" stroke="#666" stroke-width="0.2" stroke-dasharray="1,0.5"/>
    <text x="{TB_X0 + 107}" y="{TB_Y0 + 12.2}" class="text-caption">PROYEKSI SUDUT KETIGA</text>

    <!-- Row 1: Right - Tolerances & Scale -->
    <text x="{TB_X0 + 147}" y="{TB_Y0 + 4.5}" class="text-caption">STANDAR TOLERANSI:</text>
    <text x="{TB_X0 + 147}" y="{TB_Y0 + 8.0}" class="text-sub">ISO 2768-m</text>
    <text x="{TB_X0 + 147}" y="{TB_Y0 + 11.5}" class="text-caption">SATUAN: mm | SKALA: NTS</text>

    <!-- Row 2 & 3: Author & Roles -->
    <text x="{TB_X0 + 3}" y="{TB_Y0 + 16.5}" class="text-caption">PERANCANG / PENELITI UTAMA:</text>
    <text x="{TB_X0 + 3}" y="{TB_Y0 + 20.5}" class="text-sub">Ahmad Rifa'i Wibisono</text>
    <text x="{TB_X0 + 3}" y="{TB_Y0 + 24.0}" class="text-caption">NIM: 2201015024 (TEKNIK ELEKTRO)</text>
    
    <text x="{TB_X0 + 3}" y="{TB_Y0 + 29.5}" class="text-caption">OTORITAS HOST / NODE:</text>
    <text x="{TB_X0 + 3}" y="{TB_Y0 + 33.5}" class="text-body" font-weight="bold">ROOT_1_PC_AM5 (GOLDENRATIO1618)</text>
    <text x="{TB_X0 + 3}" y="{TB_Y0 + 37.5}" class="text-caption">C:\Antigravity\PRISM SAFETY GPS</text>

    <!-- Middle: Project and Drawing Title -->
    <text x="{TB_X0 + 63}" y="{TB_Y0 + 16.5}" class="text-caption">NAMA PROYEK / ID REGISTRI:</text>
    <text x="{TB_X0 + 63}" y="{TB_Y0 + 21.0}" class="text-title">PRISM SAFETY GPS (PRJ-PSG-01)</text>
    <text x="{TB_X0 + 63}" y="{TB_Y0 + 24.5}" class="text-caption">COMPACT IMPACT-SENSING &amp; REAL-TIME GNSS TRACKER</text>
    
    <text x="{TB_X0 + 63}" y="{TB_Y0 + 29.5}" class="text-caption">JUDUL LEMBAR GAMBAR KERJA:</text>
    <text x="{TB_X0 + 63}" y="{TB_Y0 + 34.0}" class="text-title" fill="#0284C7">02_System_Architecture_Flow.svg</text>
    <text x="{TB_X0 + 63}" y="{TB_Y0 + 37.5}" class="text-caption">TOPOLOGI GATEWAY LOKAL HP &amp; MESIN KEADAAN SOS</text>

    <!-- Right: Technical Details -->
    <text x="{TB_X0 + 123}" y="{TB_Y0 + 16.5}" class="text-caption">TANGGAL SINKRONISASI:</text>
    <text x="{TB_X0 + 123}" y="{TB_Y0 + 21.0}" class="text-body" font-weight="bold">2026-11-05 WIB</text>
    <text x="{TB_X0 + 123}" y="{TB_Y0 + 24.5}" class="text-caption">STATUS: APPROVED FOR PROD</text>

    <text x="{TB_X0 + 123}" y="{TB_Y0 + 29.5}" class="text-caption">LEMBAR:</text>
    <text x="{TB_X0 + 123}" y="{TB_Y0 + 35.5}" class="text-sub">02 / 08</text>

    <text x="{TB_X0 + 158}" y="{TB_Y0 + 29.5}" class="text-caption">FORMAT:</text>
    <text x="{TB_X0 + 158}" y="{TB_Y0 + 35.5}" class="text-sub">A4 LAND</text>
  </g>
''')

svg.append('</svg>')

out_path = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\04_Exported_Blueprints_PDF_SVG\02_System_Architecture_Flow.svg")
out_path.write_text('\n'.join(svg), encoding="utf-8")
print(f"Generated: {out_path} ({out_path.stat().st_size} bytes)")
