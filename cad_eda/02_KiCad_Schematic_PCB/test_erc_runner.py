import subprocess
from pathlib import Path

test_dir = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\02_KiCad_Schematic_PCB\test_erc")

sym_lib = """(kicad_symbol_lib
	(version 20231120)
	(generator "kicad_symbol_editor")
	(generator_version "10.0")
	(symbol "R"
		(pin_numbers hide)
		(pin_names (offset 0))
		(in_bom yes)
		(on_board yes)
		(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
		(property "Value" "100k" (at -2.032 0 90) (effects (font (size 1.27 1.27))))
		(property "Footprint" "" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
		(symbol "R_0_1"
			(rectangle (start -1.016 2.54) (end 1.016 -2.54) (stroke (width 0.254)) (fill (type none)))
		)
		(symbol "R_1_1"
			(pin passive line (at 0 2.54 270) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
			(pin passive line (at 0 -2.54 90) (length 0) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
		)
	)
)"""
(test_dir / "PRISM.kicad_sym").write_text(sym_lib, encoding="utf-8")

sym_table = """(sym_lib_table
  (version 7)
  (lib (name "PRISM")(type "KiCad")(uri "${KIPRJMOD}/PRISM.kicad_sym")(options "")(descr "PRISM"))
)"""
(test_dir / "sym-lib-table").write_text(sym_table, encoding="utf-8")

kicad_cli = r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe"
rpt = test_dir / "erc.rpt"
res = subprocess.run([kicad_cli, "sch", "erc", "--severity-all", "--output", str(rpt), str(test_dir / "test.kicad_sch")], capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("REPORT:\n", rpt.read_text(encoding="utf-8") if rpt.exists() else "No report")
