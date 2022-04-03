from pathlib import Path

Path("TTTT.txt").write_text(Path("name.txt").read_text() + Path("numbers.txt").read_text())
