from pathlib import Path

for item in Path("tests").glob("test_rect_*.py"):

    name = item.name.replace("rect", "crect")
    path = item.parent / name

    text = []
    for line in item.read_text().splitlines():
        if line.startswith("from twod import Point, Rect"):
            text.append("from twod import Point")
            text.append("from twod import CRect as Rect")
            continue
        text.append(line)

    path.write_text("\n".join(text))
