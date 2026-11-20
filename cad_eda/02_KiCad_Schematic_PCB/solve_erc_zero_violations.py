"""solve_erc_zero_violations.py
Generates 100% grid-aligned (multiples of 1.27 mm / 50 mil) KiCad 10 schematics.
Project-local symbol library prefix (PRISM:*) eliminates lib_symbol_mismatch.
Junctions added at every T-junction.
PWR_FLAGs placed only where required without duplicate power outputs.
Target: 0 Errors, 0 Warnings.
"""

import uuid
from pathlib import Path
import subprocess

OUT_DIR = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\02_KiCad_Schematic_PCB")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def u():
    return str(uuid.uuid4())

def grid(val):
    """Snap val (in mm) to nearest 1.27 mm (50 mil) grid"""
    return round(val / 1.27) * 1.27

ROOT_UUID = u()
SHEET_UUID = u()
SUBSHEET_UUID = u()

def build_perfect_subsheet():
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
		(symbol "PRISM:C_Polarized"
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
		(symbol "PRISM:C"
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
		(symbol "PRISM:R"
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
		(symbol "PRISM:TP4056_Module"
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
		(symbol "PRISM:Battery_LiPo"
			(in_bom yes)
			(on_board yes)
			(property "Reference" "BT1" (at 0 6.35 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Li-Po 103040 3.7V 1200mAh" (at 0 -6.35 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "PRISM_Safety_GPS:LiPo_103040_Pads" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "Battery_LiPo_0_1"
				(rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254)) (fill (type background)))
			)
			(symbol "Battery_LiPo_1_1"
				(pin passive line (at 10.16 2.54 180) (length 2.54) (name "+" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
				(pin passive line (at 10.16 -2.54 180) (length 2.54) (name "-" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
			)
		)
		(symbol "PRISM:SW_SPDT"
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

	(hierarchical_label "VCC_5V" (shape output) (at 190.50 40.64 0) (effects (font (size 1.27 1.27))) (uuid "{u()}"))
	(hierarchical_label "VBAT_SENSE" (shape output) (at 190.50 76.20 0) (effects (font (size 1.27 1.27))) (uuid "{u()}"))
	(hierarchical_label "GND" (shape bidirectional) (at 190.50 127.00 0) (effects (font (size 1.27 1.27))) (uuid "{u()}"))

	(symbol (lib_id "PRISM:Battery_LiPo") (at 38.10 45.72 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "BT1" (at 38.10 38.10 0) (effects (font (size 1.27 1.27))))
		(property "Value" "Li-Po 103040 3.7V 1200mAh" (at 38.10 53.34 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "PRISM_Safety_GPS:LiPo_103040_Pads" (at 38.10 45.72 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)

	(symbol (lib_id "PRISM:TP4056_Module") (at 76.20 45.72 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "U2" (at 76.20 35.56 0) (effects (font (size 1.27 1.27))))
		(property "Value" "TP4056_TypeC" (at 76.20 55.88 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "PRISM_Safety_GPS:TP4056_TypeC_DirectPad" (at 76.20 45.72 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
		(pin "4" (uuid "{u()}"))
		(pin "5" (uuid "{u()}"))
		(pin "6" (uuid "{u()}"))
	)

	(symbol (lib_id "PRISM:SW_SPDT") (at 127.00 48.26 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "SW1" (at 127.00 40.64 0) (effects (font (size 1.27 1.27))))
		(property "Value" "SS12D00G3_SPDT" (at 127.00 55.88 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "PRISM_Safety_GPS:SW_Slide_SS12D00G3" (at 127.00 48.26 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
	)

	(symbol (lib_id "PRISM:R") (at 152.40 66.04 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "R1" (at 154.94 66.04 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100k 1%" (at 154.94 68.58 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" (at 152.40 66.04 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)

	(symbol (lib_id "PRISM:R") (at 152.40 86.36 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "R2" (at 154.94 86.36 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100k 1%" (at 154.94 88.90 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" (at 152.40 86.36 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)

	(symbol (lib_id "PRISM:C_Polarized") (at 152.40 114.30 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "C1" (at 156.21 113.03 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100uF 16V" (at 156.21 115.57 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm" (at 152.40 114.30 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)
	(symbol (lib_id "PRISM:C") (at 165.10 114.30 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "C2" (at 168.91 113.03 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100nF" (at 168.91 115.57 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Capacitor_THT:C_Disc_D3.8mm_W2.6mm_P2.50mm" (at 165.10 114.30 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)

	(symbol (lib_id "PRISM:C_Polarized") (at 152.40 142.24 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "C3" (at 156.21 140.97 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100uF 16V" (at 156.21 143.51 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm" (at 152.40 142.24 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)
	(symbol (lib_id "PRISM:C") (at 165.10 142.24 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "C4" (at 168.91 140.97 0) (effects (font (size 1.27 1.27))))
		(property "Value" "100nF" (at 168.91 143.51 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "Capacitor_THT:C_Disc_D3.8mm_W2.6mm_P2.50mm" (at 165.10 142.24 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
	)

	(no_connect (at 132.08 50.80) (uuid "{u()}"))
	(no_connect (at 63.50 40.64) (uuid "{u()}"))
	(no_connect (at 63.50 50.80) (uuid "{u()}"))

	<!-- Junctions in Subsheet -->
	(junction (at 139.70 40.64) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 152.40 40.64) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 152.40 76.20) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 101.60 127.00) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 152.40 127.00) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 165.10 127.00) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 139.70 110.49) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 152.40 110.49) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 152.40 138.43) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))

	<!-- Wires in Subsheet -->
	(wire (pts (xy 48.26 43.18) (xy 88.90 40.64)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 48.26 48.26) (xy 88.90 43.18)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 88.90 48.26) (xy 121.92 48.26)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 132.08 45.72) (xy 139.70 45.72)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 139.70 45.72) (xy 139.70 40.64)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 139.70 40.64) (xy 152.40 40.64)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 40.64) (xy 190.50 40.64)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 152.40 40.64) (xy 152.40 60.96)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 71.12) (xy 152.40 76.20)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 76.20) (xy 152.40 81.28)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 76.20) (xy 190.50 76.20)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 91.44) (xy 152.40 127.00)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 88.90 50.80) (xy 101.60 50.80)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 101.60 50.80) (xy 101.60 127.00)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 101.60 127.00) (xy 152.40 127.00)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 127.00) (xy 165.10 127.00)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 165.10 127.00) (xy 190.50 127.00)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 139.70 40.64) (xy 139.70 110.49)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 139.70 110.49) (xy 152.40 110.49)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 110.49) (xy 165.10 110.49)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 118.11) (xy 152.40 127.00)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 165.10 118.11) (xy 165.10 127.00)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(wire (pts (xy 139.70 110.49) (xy 139.70 138.43)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 139.70 138.43) (xy 152.40 138.43)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 138.43) (xy 165.10 138.43)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 146.05) (xy 152.40 127.00)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 165.10 146.05) (xy 165.10 127.00)) (stroke (width 0) (type solid)) (uuid "{u()}"))
)"""

def build_perfect_root():
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
		(symbol "PRISM:PWR_FLAG"
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
		(symbol "PRISM:ESP32-C3_SuperMini"
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
		(symbol "PRISM:ADXL345"
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
		(symbol "PRISM:u-blox_NEO-6M"
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
		(symbol "PRISM:Buzzer_Active"
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

	(sheet (at 45.72 170.18) (size 76.20 50.80) (fields_autoplaced yes)
		(stroke (width 0.1524) (type solid))
		(fill (color 0 0 0 0))
		(uuid "{SHEET_UUID}")
		(property "Sheetname" "Power_Management_and_Filter" (at 45.72 165.10 0) (effects (font (size 1.524 1.524))))
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

	(symbol (lib_id "PRISM:ESP32-C3_SuperMini") (at 185.42 127.00 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "U1" (at 185.42 99.06 0) (effects (font (size 1.524 1.524))))
		(property "Value" "ESP32-C3_SuperMini" (at 185.42 154.94 0) (effects (font (size 1.524 1.524))))
		(property "Footprint" "PRISM_Safety_GPS:ESP32-C3_SuperMini_DirectPad" (at 185.42 127.00 0) (hide yes) (effects (font (size 1.27 1.27))))
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

	(symbol (lib_id "PRISM:ADXL345") (at 304.80 88.90 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "U3" (at 304.80 68.58 0) (effects (font (size 1.524 1.524))))
		(property "Value" "ADXL345_I2C_0x53" (at 304.80 109.22 0) (effects (font (size 1.524 1.524))))
		(property "Footprint" "PRISM_Safety_GPS:ADXL345_Module_DirectPad" (at 304.80 88.90 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
		(pin "4" (uuid "{u()}"))
		(pin "5" (uuid "{u()}"))
		(pin "6" (uuid "{u()}"))
		(pin "7" (uuid "{u()}"))
		(pin "8" (uuid "{u()}"))
	)

	(symbol (lib_id "PRISM:u-blox_NEO-6M") (at 304.80 165.10 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "U4" (at 304.80 149.86 0) (effects (font (size 1.524 1.524))))
		(property "Value" "u-blox_NEO-6M" (at 304.80 180.34 0) (effects (font (size 1.524 1.524))))
		(property "Footprint" "PRISM_Safety_GPS:NEO-6M_GPS_DirectPad" (at 304.80 165.10 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
		(pin "4" (uuid "{u()}"))
	)

	(symbol (lib_id "PRISM:Buzzer_Active") (at 304.80 223.52 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{u()}")
		(property "Reference" "BZ1" (at 304.80 213.36 0) (effects (font (size 1.524 1.524))))
		(property "Value" "Active_Buzzer_3.3V" (at 304.80 233.68 0) (effects (font (size 1.524 1.524))))
		(property "Footprint" "Buzzer_Beeper:Buzzer_12x9.5RM7.6" (at 304.80 223.52 0) (hide yes) (effects (font (size 1.27 1.27))))
		(pin "1" (uuid "{u()}"))
		(pin "2" (uuid "{u()}"))
		(pin "3" (uuid "{u()}"))
	)

	(no_connect (at 203.20 129.54) (uuid "{u()}"))
	(no_connect (at 203.20 134.62) (uuid "{u()}"))
	(no_connect (at 320.04 93.98) (uuid "{u()}"))

	<!-- Master Sheet Junctions -->
	(junction (at 269.24 83.82) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 269.24 93.98) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 269.24 172.72) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 269.24 208.28) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 279.40 78.74) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 279.40 88.90) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))
	(junction (at 279.40 160.02) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))

	<!-- Master Sheet Wires - All 100% Grid Snapped -->
	<!-- 1. VCC_5V: Sheet Pin (121.92, 182.88) to U1 Pin 1 (167.64, 109.22) -->
	(wire (pts (xy 121.92 182.88) (xy 152.40 182.88)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 182.88) (xy 152.40 109.22)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 152.40 109.22) (xy 167.64 109.22)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	<!-- 2. VBAT_SENSE: Sheet Pin (121.92, 195.58) to U1 Pin 4 [GPIO2] (167.64, 124.46) -->
	(wire (pts (xy 121.92 195.58) (xy 157.48 195.58)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 157.48 195.58) (xy 157.48 124.46)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 157.48 124.46) (xy 167.64 124.46)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	<!-- 3. GND Bus: Sheet Pin (121.92, 208.28) to U1 Pin 3 (167.64, 119.38) and to sensors -->
	(wire (pts (xy 121.92 208.28) (xy 162.56 208.28)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 162.56 208.28) (xy 162.56 119.38)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 162.56 119.38) (xy 167.64 119.38)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	
	<!-- GND Bus extending to U3, U4, BZ1 -->
	(wire (pts (xy 162.56 208.28) (xy 269.24 208.28)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 269.24 208.28) (xy 269.24 83.82)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 269.24 83.82) (xy 289.56 83.82)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 269.24 93.98) (xy 289.56 93.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	
	(wire (pts (xy 269.24 208.28) (xy 269.24 226.06)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 269.24 172.72) (xy 317.50 172.72)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 269.24 226.06) (xy 312.42 226.06)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	<!-- 4. 3.3V out: U1 Pin 2 (167.64, 114.30) to U3 Pin 1 [VCC] (289.56, 78.74), U3 Pin 3 [CS] (289.56, 88.90), U4 Pin 1 [VCC] (292.10, 160.02), BZ1 Pin 1 [VCC] (297.18, 220.98) -->
	(wire (pts (xy 167.64 114.30) (xy 154.94 114.30)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 154.94 114.30) (xy 154.94 64.77)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 154.94 64.77) (xy 279.40 64.77)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 279.40 64.77) (xy 279.40 78.74)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 279.40 78.74) (xy 289.56 78.74)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	
	(wire (pts (xy 279.40 78.74) (xy 279.40 88.90)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 279.40 88.90) (xy 289.56 88.90)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	
	(wire (pts (xy 279.40 88.90) (xy 279.40 160.02)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 279.40 160.02) (xy 292.10 160.02)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	
	(wire (pts (xy 279.40 160.02) (xy 279.40 220.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 279.40 220.98) (xy 297.18 220.98)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	<!-- 5. I2C Bus: SDA -> U1 Pin 7 (203.20, 109.22) to U3 Pin 5 (320.04, 78.74) -->
	(wire (pts (xy 203.20 109.22) (xy 241.30 109.22)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 241.30 109.22) (xy 241.30 78.74)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 241.30 78.74) (xy 320.04 78.74)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	<!-- I2C Bus: SCL -> U1 Pin 8 (203.20, 114.30) to U3 Pin 6 (320.04, 83.82) -->
	(wire (pts (xy 203.20 114.30) (xy 245.11 114.30)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 245.11 114.30) (xy 245.11 83.82)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 245.11 83.82) (xy 320.04 83.82)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	<!-- 6. ADXL345 INT1 -> U3 Pin 7 (320.04, 88.90) to U1 Pin 5 [GPIO3] (167.64, 129.54) -->
	(wire (pts (xy 320.04 88.90) (xy 335.28 88.90)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 335.28 88.90) (xy 335.28 69.85)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 335.28 69.85) (xy 149.86 69.85)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 149.86 69.85) (xy 149.86 129.54)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 149.86 129.54) (xy 167.64 129.54)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	<!-- 7. GNSS UART: U4 Pin 3 [TX] (317.50, 167.64) to U1 Pin 9 [GPIO20_RX0] (203.20, 119.38) -->
	(wire (pts (xy 317.50 167.64) (xy 325.12 167.64)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 325.12 167.64) (xy 325.12 119.38)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 325.12 119.38) (xy 203.20 119.38)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	<!-- GNSS UART: U1 Pin 10 [GPIO21_TX0] (203.20, 124.46) to U4 Pin 2 [RX] (292.10, 167.64) -->
	(wire (pts (xy 203.20 124.46) (xy 260.35 124.46)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 260.35 124.46) (xy 260.35 167.64)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 260.35 167.64) (xy 292.10 167.64)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	<!-- 8. Buzzer Control: U1 Pin 6 [GPIO4] (167.64, 134.62) to BZ1 Pin 2 [I/O] (297.18, 226.06) -->
	(wire (pts (xy 167.64 134.62) (xy 144.78 134.62)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 144.78 134.62) (xy 144.78 240.03)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 144.78 240.03) (xy 284.48 240.03)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 284.48 240.03) (xy 284.48 226.06)) (stroke (width 0) (type solid)) (uuid "{u()}"))
	(wire (pts (xy 284.48 226.06) (xy 297.18 226.06)) (stroke (width 0) (type solid)) (uuid "{u()}"))

	(sheet_instances
		(path "/" (page "1"))
	)
)"""

def main():
    root_sch_path = OUT_DIR / "PRISM_SAFETY_GPS.kicad_sch"
    sub_sch_path = OUT_DIR / "Power_Filter_Subsheet.kicad_sch"
    
    sub_sch_path.write_text(build_perfect_subsheet(), encoding="utf-8")
    root_sch_path.write_text(build_perfect_root(), encoding="utf-8")
    
    kicad_cli = r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe"
    rpt_path = OUT_DIR / "erc.rpt"
    cmd = [kicad_cli, "sch", "erc", "--severity-all", "--output", str(rpt_path), str(root_sch_path)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("ERC Return code:", res.returncode)
    
    if rpt_path.exists():
        rpt_text = rpt_path.read_text(encoding="utf-8")
        errors = [l for l in rpt_text.splitlines() if "; error" in l]
        warnings = [l for l in rpt_text.splitlines() if "; warning" in l]
        print(f"ERC Summary: {len(errors)} Errors, {len(warnings)} Warnings")
        for l in rpt_text.splitlines()[:30]:
            print(" ", l)

if __name__ == "__main__":
    main()
