



def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        lines = block.split("\n")
        para = " ".join(lines)
        if para.startswith("# "):
            return para.lstrip("#").strip()
    raise Exception("no h1")

