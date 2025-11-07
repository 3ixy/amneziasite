import os
import html2text

converter = html2text.HTML2Text()
converter.ignore_links = False
for root, _, files in os.walk(".."):
    for f in files:
        if f.endswith(".md"):
            md_path = os.path.join(root, f)
            with open(md_path, "r", encoding="utf-8") as fin:
                lines = fin.readlines()

            if len(lines) > 86:
                lines = lines[86:]  # пропустить первые 86 строк
            else:
                lines = []  # если меньше 86 строк — удалить всё

            with open(md_path, "w", encoding="utf-8") as fout:
                fout.writelines(lines)

            print(f"🧹 Trimmed first 86 lines in: {md_path}")