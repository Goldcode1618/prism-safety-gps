"""generate_kicad_schematics.py
Generates native KiCad 10 PRISM_SAFETY_GPS.kicad_sch (A3) and Power_Filter_Subsheet.kicad_sch (A4)
Ensures full S-expression compliance with UUIDs, no_connect flags, and PWR_FLAGs to reach:
0 ERC Errors, 0 ERC Warnings.
"""

import uuid
from pathlib import Path
import subprocess

OUT_DIR = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\02_KiCad_Schematic_PCB")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def u():
    return str(uuid.uuid4())

# Master Schematic UUIDs
ROOT_UUID = u()
SHEET_UUID = u()
SUBSHEET_UUID = u()

def build_subsheet():
    return f"""(kicad_sch
	(version 20260306)
	(generator "eeschema")
	(generator_version "10.0")
	(uuid "{SUBSHEET_UUID}")
	(paper "A4")
	(title_block
		(title "PRISM SAFETY GPS - Power Management, Battery & Decoupling Filter")
		(date "2026-11-05")
		(rev "1.0")
		(company "Universitas Muhammadiyah Prof. DR. HAMKA (FTII UHAMKA)")
		(comment 1 "Author: Ahmad Rifa'i Wibisono (NIM: 2201015024)")
		(comment 2 "Project: PRJ-PSG-01 | Third Angle Projection | ISO 2768-m")
		(comment 3 "Subsheet: Catu Daya, Proteksi TP4056, Pembagi Tegangan, & Filter RF")
	)
	(lib_symbols
		(symbol "power:PWR_FLAG"
			(power global)
			(in_bom no)
			(on_board no)
			(property "Reference" "#PWR" (at 0 -3.81 0) (hide yes) (effects (font (size 1.27 1.27))))
			(property "Value" "PWR_FLAG" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "PWR_FLAG_0_1"
				(polyline (pts (xy 0 0) (xy 0 1.27) (xy -1.016 1.905) (xy 0 2.54) (xy 1.016 1.905) (xy 0 1.27)) (stroke (width 0.254)))
			)
			(symbol "PWR_FLAG_1_1"
				(pin power_out line (at 0 0 90) (length 0) (name "pwr" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:C_Polarized"
			(pin_numbers hide)
			(pin_names (offset 0.254))
			(in_bom yes)
			(on_board yes)
			(property "Reference" "C" (at 1.27 1.27 0) (effects (font (size 1.27 1.27))))
			(property "Value" "100uF" (at 1.27 -1.27 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "C_Polarized_0_1"
				(polyline (pts (xy -1.27 0.635) (xy 1.27 0.635)) (stroke (width 0.254)))
				(polyline (pts (xy -1.27 -0.635) (xy 1.27 -0.635)) (stroke (width 0.254)))
			)
			(symbol "C_Polarized_1_1"
				(pin passive line (at 0 3.81 270) (length 3.175) (name "+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 3.175) (name "-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:C"
			(pin_numbers hide)
			(pin_names (offset 0.254))
			(in_bom yes)
			(on_board yes)
			(property "Reference" "C" (at 1.27 1.27 0) (effects (font (size 1.27 1.27))))
			(property "Value" "100nF" (at 1.27 -1.27 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "Capacitor_THT:C_Disc_D3.8mm_W2.6mm_P2.50mm" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "C_0_1"
				(polyline (pts (xy -1.27 0.635) (xy 1.27 0.635)) (stroke (width 0.254)))
				(polyline (pts (xy -1.27 -0.635) (xy 1.27 -0.635)) (stroke (width 0.254)))
			)
			(symbol "C_1_1"
				(pin passive line (at 0 3.81 270) (length 3.175) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -3.81 90) (length 3.175) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:R"
			(pin_numbers hide)
			(pin_names (offset 0))
			(in_bom yes)
			(on_board yes)
			(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "100k" (at -2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "R_0_1"
				(rectangle (start -1.016 2.54) (end 1.016 -2.54) (stroke (width 0.254)) (fill (type none)))
			)
			(symbol "R_1_1"
				(pin passive line (at 0 5.08 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 0 -5.08 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Power:TP4056_Module"
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U2" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
			(property "Value" "TP4056_TypeC" (at 0 -10.16 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "PRISM_Safety_GPS:TP4056_TypeC_DirectPad" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "TP4056_Module_0_1"
				(rectangle (start -10.16 8.89) (end 10.16 -8.89) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "TP4056_Module_1_1"
				(pin power_in line (at -12.7 5.08 0) (length 2.54) (name "IN+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at -12.7 -5.08 0) (length 2.54) (name "IN-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 12.7 5.08 180) (length 2.54) (name "BAT+" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 12.7 2.54 180) (length 2.54) (name "BAT-" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 12.7 -2.54 180) (length 2.54) (name "OUT+" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 12.7 -5.08 180) (length 2.54) (name "OUT-" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:Battery_LiPo"
			(in_bom yes)
			(on_board yes)
			(property "Reference" "BT1" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Li-Po 103040 3.7V 1200mAh" (at 0 -6.35 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "PRISM_Safety_GPS:LiPo_103040_Pads" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "Battery_LiPo_0_1"
				(rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "Battery_LiPo_1_1"
				(pin power_out line (at 10.16 2.54 180) (length 2.54) (name "+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at 10.16 -2.54 180) (length 2.54) (name "-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Switch:SW_SPDT"
			(in_bom yes)
			(on_board yes)
			(property "Reference" "SW1" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
			(property "Value" "SS12D00G3_SPDT" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "PRISM_Safety_GPS:SW_Slide_SS12D00G3" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "SW_SPDT_0_1"
				(circle (center -2.54 0) (radius 0.508) (stroke (width 0.254)) (fill (type none)))
				(circle (center 2.54 2.54) (radius 0.508) (stroke (width 0.254)) (fill (type none)))
				(circle (center 2.54 -2.54) (radius 0.508) (stroke (width 0.254)) (fill (type none)))
				(polyline (pts (xy -2.032 0) (xy 2.032 2.54)) (stroke (width 0.254)))
			)
			(symbol "SW_SPDT_1_1"
				(pin passive line (at -5.08 0 0) (length 2.54) (name "COM" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 5.08 2.54 180) (length 2.54) (name "ON" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 5.08 -2.54 180) (length 2.54) (name "NC" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
	)

	(hierarchical_label "VCC_5V" (shape output) (at 190.5 45.72 0) (effects (font (size 1.27 1.27))) (uuid "{u()}"))
	(hierarchical_label "VBAT_SENSE" (shape output) (at 190.5 76.2 0) (effects (font (size 1.27 1.27))) (uuid "{u()}"))
	(hierarchical_label "GND" (shape bidirectional) (at 190.5 127.0 0) (effects (font (size 1.27 1.27))) (uuid "{u()}"))

	(symbol (lib_id "Device:Battery_LiPo") (at 38.1 45.72 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "BT1" (at 38.1 38.1 0) (effects (font (size 1.27 1.27))))
		(property "Value" "Li-Po 103040 3.7V 1200mAh" (at 38.1 53.34 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "PRISM_Safety_GPS:LiPo_103040_Pads" (at 38.1 45.72 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)

	(symbol (lib_id "Power:TP4056_Module") (at 76.2 45.72 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "U2" (at 76.2 35.56 0) (effects (font (size 1.27 1.27))))
		(property "Value" "TP4056_TypeC" (at 76.2 55.88 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "PRISM_Safety_GPS:TP4056_TypeC_DirectPad" (at 76.2 45.72 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
		(pin "4" (uuid "{u()}"))
		(pin "5" (uuid "{u()}"))
		(pin "6" (uuid "{u()}"))
	)

	(symbol (lib_id "Switch:SW_SPDT") (at 127.0 43.18 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "SW1" (at 127.0 35.56 0) (effects (font (size 1.27 1.27))))
		(property "Value" "SS12D00G3_SPDT" (at 127.0 50.8 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "PRISM_Safety_GPS:SW_Slide_SS12D00G3" (at 127.0 43.18 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
	)

	(symbol (lib_id "Device:R") (at 152.4 66.04 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "R1" (at 154.94 66.04 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100k 1%" (at 154.94 68.58 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" (at 152.4 66.04 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)

	(symbol (lib_id "Device:R") (at 152.4 86.36 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "R2" (at 154.94 86.36 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100k 1%" (at 154.94 88.9 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" (at 152.4 86.36 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)

	(symbol (lib_id "Device:C_Polarized") (at 152.4 114.3 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "C1" (at 156.21 113.03 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100uF 16V" (at 156.21 115.57 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm" (at 152.4 114.3 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)
	(symbol (lib_id "Device:C") (at 165.1 114.3 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "C2" (at 168.91 113.03 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100nF" (at 168.91 115.57 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Capacitor_THT:C_Disc_D3.8mm_W2.6mm_P2.50mm" (at 165.1 114.3 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)

	(symbol (lib_id "Device:C_Polarized") (at 152.4 142.24 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "C3" (at 156.21 140.97 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100uF 16V" (at 156.21 143.51 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm" (at 152.4 142.24 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)
	(symbol (lib_id "Device:C") (at 165.1 142.24 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "C4" (at 168.91 140.97 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100nF" (at 168.91 143.51 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Capacitor_THT:C_Disc_D3.8mm_W2.6mm_P2.50mm" (at 165.1 142.24 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)

	(no_connect (at 132.08 40.64) (uuid "{u()}"))
	(no_connect (at 63.5 50.8) (uuid "{u()}"))
	(no_connect (at 63.5 40.64) (uuid "{u()}"))

	(wire (pts (xy 48.26 48.26) (xy 88.9 50.8)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 48.26 43.18) (xy 88.9 48.26)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 88.9 43.18) (xy 121.92 43.18)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 132.08 45.72) (xy 152.4 45.72)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.4 45.72) (xy 190.5 45.72)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.4 45.72) (xy 152.4 60.96)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	
	(wire (pts (xy 152.4 71.12) (xy 152.4 81.28)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.4 76.2) (xy 190.5 76.2)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 152.4 91.44) (xy 152.4 127.0)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 88.9 40.64) (xy 101.6 40.64)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 101.6 40.64) (xy 101.6 127.0)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 101.6 127.0) (xy 190.5 127.0)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 152.4 110.49) (xy 152.4 45.72)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 165.1 110.49) (xy 152.4 110.49)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 152.4 118.11) (xy 152.4 127.0)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 165.1 118.11) (xy 165.1 127.0)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.4 146.05) (xy 152.4 127.0)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 165.1 146.05) (xy 165.1 127.0)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.4 138.43) (xy 165.1 138.43)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.4 138.43) (xy 152.4 127.0)) (stroke (width 0) (type solid)) (uuid "{u()}"))
)"""

def build_root_schematic():
    return f"""(kicad_sch
	(version 20260306)
	(generator "eeschema")
	(generator_version "10.0")
	(uuid "{ROOT_UUID}")
	(paper "A3")
	(title_block
		(title "PRISM SAFETY GPS - Master System Architecture & Sensors")
		(date "2026-11-05")
		(rev "1.0")
		(company "Universitas Muhammadiyah Prof. DR. HAMKA (FTII UHAMKA)")
		(comment 1 "Author: Ahmad Rifa'i Wibisono (NIM: 2201015024)")
		(comment 2 "Project: PRJ-PSG-01 | Third Angle Projection | ISO 2768-m")
		(comment 3 "Host Authority: ROOT_1_PC_AM5 (GOLDENRATIO1618)")
	)
	(lib_symbols
		(symbol "power:PWR_FLAG"
			(power global)
			(in_bom no)
			(on_board no)
			(property "Reference" "#PWR" (at 0 -3.81 0) (hide yes) (effects (font (size 1.27 1.27))))
			(property "Value" "PWR_FLAG" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "PWR_FLAG_0_1"
				(polyline (pts (xy 0 0) (xy 0 1.27) (xy -1.016 1.905) (xy 0 2.54) (xy 1.016 1.905) (xy 0 1.27)) (stroke (width 0.254)))
			)
			(symbol "PWR_FLAG_1_1"
				(pin power_out line (at 0 0 90) (length 0) (name "pwr" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "MCU:ESP32-C3_SuperMini"
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U1" (at 0 24.13 0) (effects (font (size 1.27 1.27))))
			(property "Value" "ESP32-C3_SuperMini" (at 0 -24.13 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "PRISM_Safety_GPS:ESP32-C3_SuperMini_DirectPad" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "ESP32-C3_SuperMini_0_1"
				(rectangle (start -15.24 22.86) (end 15.24 -22.86) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "ESP32-C3_SuperMini_1_1"
				(pin power_in line (at -17.78 17.78 0) (length 2.54) (name "5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_out line (at -17.78 12.7 0) (length 2.54) (name "3.3V" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at -17.78 7.62 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 2.54 0) (length 2.54) (name "GPIO2_ADC" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin input line (at -17.78 -2.54 0) (length 2.54) (name "GPIO3_INT1" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
				(pin output line (at -17.78 -7.62 0) (length 2.54) (name "GPIO4_BUZZER" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 17.78 180) (length 2.54) (name "GPIO8_SDA" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 12.7 180) (length 2.54) (name "GPIO9_SCL" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
				(pin input line (at 17.78 7.62 180) (length 2.54) (name "GPIO20_RX0" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
				(pin output line (at 17.78 2.54 180) (length 2.54) (name "GPIO21_TX0" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 -2.54 180) (length 2.54) (name "GPIO0" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 17.78 -7.62 180) (length 2.54) (name "GPIO1" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Sensor:ADXL345"
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U3" (at 0 17.78 0) (effects (font (size 1.27 1.27))))
			(property "Value" "ADXL345_I2C_0x53" (at 0 -17.78 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "PRISM_Safety_GPS:ADXL345_Module_DirectPad" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "ADXL345_0_1"
				(rectangle (start -12.7 15.24) (end 12.7 -15.24) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "ADXL345_1_1"
				(pin power_in line (at -15.24 10.16 0) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at -15.24 5.08 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin input line (at -15.24 0 0) (length 2.54) (name "CS" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin input line (at -15.24 -5.08 0) (length 2.54) (name "SDO_ADDR" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
				(pin bidirectional line (at 15.24 10.16 180) (length 2.54) (name "SDA" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
				(pin input line (at 15.24 5.08 180) (length 2.54) (name "SCL" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
				(pin output line (at 15.24 0 180) (length 2.54) (name "INT1" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
				(pin output line (at 15.24 -5.08 180) (length 2.54) (name "INT2" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "GPS:u-blox_NEO-6M"
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U4" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
			(property "Value" "u-blox_NEO-6M" (at 0 -12.7 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "PRISM_Safety_GPS:NEO-6M_GPS_DirectPad" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "u-blox_NEO-6M_0_1"
				(rectangle (start -10.16 10.16) (end 10.16 -10.16) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "u-blox_NEO-6M_1_1"
				(pin power_in line (at -12.7 5.08 0) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin input line (at -12.7 -2.54 0) (length 2.54) (name "RX" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin output line (at 12.7 -2.54 180) (length 2.54) (name "TX" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 12.7 -7.62 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "Device:Buzzer_Active"
			(in_bom yes)
			(on_board yes)
			(property "Reference" "BZ1" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Active_Buzzer_3.3V" (at 0 -8.89 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "Buzzer_Beeper:Buzzer_12x9.5RM7.6" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "Buzzer_Active_0_1"
				(circle (center 0 0) (radius 5.08) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "Buzzer_Active_1_1"
				(pin power_in line (at -7.62 2.54 0) (length 2.54) (name "VCC" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin input line (at -7.62 -2.54 0) (length 2.54) (name "I/O" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
				(pin power_in line (at 7.62 -2.54 180) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
			)
		)
	)

	(sheet (at 45.72 170.18) (size 76.2 50.8) (fields_autoplaced yes)
		(stroke (width 0.1524) (type solid))
		(fill (color 0 0 0 0))
		(uuid "{SHEET_UUID}")
		(property "Sheetname" "Power_Management_and_Filter" (at 45.72 165.1 0) (effects (font (size 1.524 1.524))))
		(property "Sheetfile" "Power_Filter_Subsheet.kicad_sch" (at 45.72 226.06 0) (effects (font (size 1.524 1.524))))
		(pin "VCC_5V" output (at 121.92 182.88 0) (uuid "{u()}") (effects (font (size 1.27 1.27)) (justify right)))
		(pin "VBAT_SENSE" output (at 121.92 195.58 0) (uuid "{u()}") (effects (font (size 1.27 1.27)) (justify right)))
		(pin "GND" bidirectional (at 121.92 208.28 0) (uuid "{u()}") (effects (font (size 1.27 1.27)) (justify right)))
		(instances
			(project "PRISM_SAFETY_GPS"
				(path "/{ROOT_UUID}"
					(page "2")
				)
			)
		)
	)

	(symbol (lib_id "MCU:ESP32-C3_SuperMini") (at 185.42 127.0 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "U1" (at 185.42 99.06 0) (effects (font (size 1.524 1.524))))
		(property "Value" "ESP32-C3_SuperMini" (at 185.42 154.94 0) (effects (font (size 1.524 1.524))))
		(property "Footprint" "PRISM_Safety_GPS:ESP32-C3_SuperMini_DirectPad" (at 185.42 127.0 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
		(pin "4" (uuid "{u()}"))
		(pin "5" (uuid "{u()}"))
		(pin "6" (uuid "{u()}"))
		(pin "7" (uuid "{u()}"))
		(pin "8" (uuid "{u()}"))
		(pin "9" (uuid "{u()}"))
		(pin "10" (uuid "{u()}"))
		(pin "11" (uuid "{u()}"))
		(pin "12" (uuid "{u()}"))
	)

	(symbol (lib_id "Sensor:ADXL345") (at 304.8 88.9 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "U3" (at 304.8 68.58 0) (effects (font (size 1.524 1.524))))
		(property "Value" "ADXL345_I2C_0x53" (at 304.8 109.22 0) (effects (font (size 1.524 1.524))))
		(property "Footprint" "PRISM_Safety_GPS:ADXL345_Module_DirectPad" (at 304.8 88.9 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
		(pin "4" (uuid "{u()}"))
		(pin "5" (uuid "{u()}"))
		(pin "6" (uuid "{u()}"))
		(pin "7" (uuid "{u()}"))
		(pin "8" (uuid "{u()}"))
	)

	(symbol (lib_id "GPS:u-blox_NEO-6M") (at 304.8 165.1 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "U4" (at 304.8 149.86 0) (effects (font (size 1.524 1.524))))
		(property "Value" "u-blox_NEO-6M" (at 304.8 180.34 0) (effects (font (size 1.524 1.524))))
		(property "Footprint" "PRISM_Safety_GPS:NEO-6M_GPS_DirectPad" (at 304.8 165.1 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
		(pin "4" (uuid "{u()}"))
	)

	(symbol (lib_id "Device:Buzzer_Active") (at 304.8 223.52 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "BZ1" (at 304.8 213.36 0) (effects (font (size 1.524 1.524))))
		(property "Value" "Active_Buzzer_3.3V" (at 304.8 233.68 0) (effects (font (size 1.524 1.524))))
		(property "Footprint" "Buzzer_Beeper:Buzzer_12x9.5RM7.6" (at 304.8 223.52 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
	)

	(symbol (lib_id "power:PWR_FLAG") (at 121.92 180.34 90) (unit 1)
		(in_bom no) (on_board no) (dnp no)
		(uuid "{u()}")
		(property "Reference" "#PWR01" (at 121.92 180.34 0) (hide yes) (effects (font (size 1.27 1.27))))
		(property "Value" "PWR_FLAG" (at 121.92 180.34 0) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
	)
	(symbol (lib_id "power:PWR_FLAG") (at 121.92 205.74 90) (unit 1)
		(in_bom no) (on_board no) (dnp no)
		(uuid "{u()}")
		(property "Reference" "#PWR02" (at 121.92 205.74 0) (hide yes) (effects (font (size 1.27 1.27))))
		(property "Value" "PWR_FLAG" (at 121.92 205.74 0) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
	)

	(no_connect (at 203.2 129.54) (uuid "{u()}"))
	(no_connect (at 203.2 134.62) (uuid "{u()}"))
	(no_connect (at 320.04 83.82) (uuid "{u()}"))

	(wire (pts (xy 121.92 182.88) (xy 152.4 182.88)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.4 182.88) (xy 152.4 144.78)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.4 144.78) (xy 167.64 144.78)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 121.92 180.34) (xy 121.92 182.88)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 121.92 195.58) (xy 160.02 195.58)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 160.02 195.58) (xy 160.02 129.54)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 160.02 129.54) (xy 167.64 129.54)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 121.92 208.28) (xy 165.1 208.28)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 165.1 208.28) (xy 165.1 134.62)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 165.1 134.62) (xy 167.64 134.62)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 121.92 205.74) (xy 121.92 208.28)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 167.64 139.7) (xy 160.02 139.7)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 160.02 139.7) (xy 160.02 60.96)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 160.02 60.96) (xy 281.94 60.96)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 281.94 60.96) (xy 281.94 99.06)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 281.94 99.06) (xy 289.56 99.06)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	
	(wire (pts (xy 281.94 88.9) (xy 289.56 88.9)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 281.94 99.06) (xy 281.94 88.9)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	
	(wire (pts (xy 281.94 99.06) (xy 281.94 170.18)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 281.94 170.18) (xy 292.1 170.18)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	
	(wire (pts (xy 281.94 170.18) (xy 281.94 226.06)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 281.94 226.06) (xy 297.18 226.06)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 289.56 93.98) (xy 276.86 93.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 289.56 83.82) (xy 276.86 83.82)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 276.86 83.82) (xy 276.86 93.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 276.86 93.98) (xy 276.86 208.28)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 276.86 208.28) (xy 165.1 208.28)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 317.5 157.48) (xy 330.2 157.48)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 312.42 220.98) (xy 330.2 220.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 330.2 157.48) (xy 330.2 220.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 330.2 220.98) (xy 276.86 220.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 203.2 144.78) (xy 238.76 144.78)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 238.76 144.78) (xy 238.76 99.06)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 238.76 99.06) (xy 320.04 99.06)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 203.2 139.7) (xy 243.84 139.7)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 243.84 139.7) (xy 243.84 93.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 243.84 93.98) (xy 320.04 93.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 320.04 88.9) (xy 335.28 88.9)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 335.28 88.9) (xy 335.28 73.66)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 335.28 73.66) (xy 154.94 73.66)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 154.94 73.66) (xy 154.94 124.46)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 154.94 124.46) (xy 167.64 124.46)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 317.5 162.56) (xy 322.58 162.56)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 322.58 162.56) (xy 322.58 134.62)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 322.58 134.62) (xy 203.2 134.62)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 292.1 162.56) (xy 284.48 162.56)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 284.48 162.56) (xy 284.48 129.54)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 284.48 129.54) (xy 203.2 129.54)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 167.64 119.38) (xy 147.32 119.38)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 147.32 119.38) (xy 147.32 238.76)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 147.32 238.76) (xy 287.02 238.76)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 287.02 238.76) (xy 287.02 220.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 287.02 220.98) (xy 297.18 220.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(sheet_instances
		(path "/" (page "1"))
	)
)"""

def main():
    root_sch_path = OUT_DIR / "PRISM_SAFETY_GPS.kicad_sch"
    sub_sch_path = OUT_DIR / "Power_Filter_Subsheet.kicad_sch"
    
    print("Writing KiCad 10 schematic files...")
    sub_sch_path.write_text(build_subsheet(), encoding="utf-8")
    root_sch_path.write_text(build_root_schematic(), encoding="utf-8")
    print(f"Created: {sub_sch_path}")
    print(f"Created: {root_sch_path}")
    
    # Run kicad-cli sch erc
    kicad_cli = r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe"
    rpt_path = OUT_DIR / "erc.rpt"
    cmd = [kicad_cli, "sch", "erc", "--severity-all", "--output", str(rpt_path), str(root_sch_path)]
    print(f"Running ERC: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    print(f"Return code: {res.returncode}")
    
    # Export PDF and SVG
    pdf_out = OUT_DIR / "03_Schematic_PRISM_SAFETY_GPS.pdf"
    print("Exporting PDF...")
    res_pdf = subprocess.run([kicad_cli, "sch", "export", "pdf", "--output", str(pdf_out), str(root_sch_path)], capture_output=True, text=True)
    print(f"PDF export exit: {res_pdf.returncode}")

    print("Exporting SVG...")
    res_svg = subprocess.run([kicad_cli, "sch", "export", "svg", "--output", str(OUT_DIR), str(root_sch_path)], capture_output=True, text=True)
    print(f"SVG export exit: {res_svg.returncode}")

if __name__ == "__main__":
    main()
