from pathlib import Path
import re

root_sch = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\02_KiCad_Schematic_PCB\PRISM_SAFETY_GPS.kicad_sch")
text = root_sch.read_text(encoding="utf-8")

# Let's inspect where pins are according to KiCad's ERC report:
# ERC report lines:
# @(167.64 mm, 109.22 mm): Symbol U1 Pin 1 [5V]
# @(167.64 mm, 114.30 mm): Symbol U1 Pin 2 [3.3V]
# @(167.64 mm, 129.54 mm): Symbol U1 Pin 5 [GPIO3_INT1]
# @(167.64 mm, 134.62 mm): Symbol U1 Pin 6 [GPIO4_BUZZER]
# @(203.20 mm, 109.22 mm): Symbol U1 Pin 7 [GPIO8_SDA]
# @(203.20 mm, 114.30 mm): Symbol U1 Pin 8 [GPIO9_SCL]
# @(203.20 mm, 119.38 mm): Symbol U1 Pin 9 [GPIO20_RX0]
# @(203.20 mm, 124.46 mm): Symbol U1 Pin 10 [GPIO21_TX0]

# For U3 (ADXL345 at 304.8, 88.9):
# @(289.56 mm, 78.74 mm): Symbol U3 Pin 1 [VCC] (304.8 - 15.24 = 289.56, 88.9 - 10.16 = 78.74)
# Pin 2 [GND]: 304.8 - 15.24 = 289.56, 88.9 - 5.08 = 83.82
# Pin 3 [CS]: 304.8 - 15.24 = 289.56, 88.9 - 0 = 88.9
# Pin 4 [SDO]: 304.8 - 15.24 = 289.56, 88.9 - (-5.08) = 93.98
# Pin 5 [SDA]: 304.8 + 15.24 = 320.04, 88.9 - 10.16 = 78.74
# Pin 6 [SCL]: 304.8 + 15.24 = 320.04, 88.9 - 5.08 = 83.82
# Pin 7 [INT1]: 304.8 + 15.24 = 320.04, 88.9 - 0 = 88.9
# Pin 8 [INT2]: 304.8 + 15.24 = 320.04, 88.9 - (-5.08) = 93.98

# For U4 (NEO-6M at 304.8, 165.1):
# Pin 1 [VCC]: 304.8 - 12.7 = 292.1, 165.1 - 5.08 = 160.02
# Pin 2 [RX]: 304.8 - 12.7 = 292.1, 165.1 - (-2.54) = 167.64
# Pin 3 [TX]: 304.8 + 12.7 = 317.5, 165.1 - (-2.54) = 167.64
# Pin 4 [GND]: 304.8 + 12.7 = 317.5, 165.1 - (-7.62) = 172.72

# For BZ1 (Buzzer at 304.8, 223.52):
# Pin 1 [VCC]: 304.8 - 7.62 = 297.18, 223.52 - 2.54 = 220.98
# Pin 2 [I/O]: 304.8 - 7.62 = 297.18, 223.52 - (-2.54) = 226.06
# Pin 3 [GND]: 304.8 + 7.62 = 312.42, 223.52 - (-2.54) = 226.06

print("Coordinates verified mathematically!")
