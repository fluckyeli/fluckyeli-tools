def fmt_article(content: str):
    fmt_content = content.strip().replace(" ", "").replace("\t", "")
    fmt_content = fmt_content.replace("，", "，\n")
    fmt_content = fmt_content.replace("。", "。\n")
    fmt_content = fmt_content.replace("！", "！\n")
    fmt_content = fmt_content.replace("？", "？\n")
    fmt_content = fmt_content.replace("；", "；\n")
    return fmt_content.strip()


with open("格式化后文章.txt", "w", encoding="utf-8") as fw:
    with open("原文.txt", "r", encoding="utf-8") as fr:
        for line in fr:
            formatted_line = fmt_article(line)
            fw.write(formatted_line + "\n")



