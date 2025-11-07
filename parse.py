import os

for root, _, files in os.walk("."):
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(root, f)
            with open(path, "rb") as fin:
                data = fin.read()
            if b"\x00" in data:
                print("⚠️ Нулевой байт найден в:", path)
