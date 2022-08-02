import os
from pathlib import Path

from PyPDF2 import PdfFileReader

from format import format_text, PaperFormat


def main():
    paper_format = PaperFormat(title_lines_num=1, chapter_has_dot=False)

    path = Path("res/DenseCLIP2.pdf")
    # path = "res/Imagen.pdf"
    with open(path, "rb") as pdf:
        reader = PdfFileReader(pdf)

        page_num = reader.getNumPages()
        all_text = ""

        for i in range(page_num):
            page = reader.getPage(i)
            text = page.extract_text()

            text = format_text(text, i, paper_format=paper_format)
            all_text += text

        os.makedirs("output", exist_ok=True)
        with open(f"output/{path.stem}.txt", "w") as f:
            f.write(all_text)


if __name__ == '__main__':
    main()
