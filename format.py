from collections import OrderedDict


# PDF全体のフォーマット設定
class PaperFormat:
    def __init__(self, chapter_has_dot=True, title_lines_num=1):
        # 1. Introductionのように章立てに"."が使われているか
        self.chapter_has_dot = chapter_has_dot

        # タイトルが何行分またがって表示されているか
        self.title_lines_num = title_lines_num


def format_text(
        text: str,
        page_num: int,
        paper_format: PaperFormat,
):
    all_texts = text.splitlines(keepends=True)
    results = ""
    is_body = False if page_num == 0 else True

    chapter_num_prefix = [f"{n}. " if paper_format.chapter_has_dot else f"{n} " for n in range(10)]
    chapter_str_prefix = ["Abstract", "Reference", "Appendix:"]
    chapter_prefix = tuple(chapter_num_prefix + chapter_str_prefix)

    for i, text_line in enumerate(all_texts):
        # Title
        if i == (paper_format.title_lines_num - 1) and page_num == 0:
            text_line += "\n"
        elif i < paper_format.title_lines_num and page_num == 0:
            text_line = text_line.replace("\n", " ")

        # 1.Introductionなどで始まる場合、改行を入れてわかりやすくする
        elif text_line.startswith(chapter_prefix):
            text_line = f"\n\n{text_line}"

            # Abstract以前はbody部分とは別に処理したい
            if text_line.startswith("Abstract"):
                is_body = True

        # body部分は整形して改行する
        elif is_body:
            replace_dict = OrderedDict({
                "\t": " ",
                "-\n": "",
                "\n": " ",
                "”": "\"",
                " ”": "\"",
                "“": "\"",
                "  ": " ",
                "　": " ",
            })
            for key, value in replace_dict.items():
                text_line = text_line.replace(key, value)

        # Abstractより前のパート(だいたい著者のパート)
        elif not is_body:
            nums = 10
            num_dict = {}
            for j in range(nums):
                num_dict[str(j)] = ""

            replace_dict = OrderedDict({
                "\n": "",
                **num_dict,
            })
            for key, value in replace_dict.items():
                text_line = text_line.replace(key, value)

        results += text_line
    return results


if __name__ == '__main__':
    pass
