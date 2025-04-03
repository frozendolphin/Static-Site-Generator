import os

from block_markdown import markdown_to_html_node

def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        lines = block.split("\n")
        para = " ".join(lines)
        if para.startswith("# "):
            return para.lstrip("#").strip()
    raise Exception("no h1")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        markdown = f.read()
    
    with open(template_path) as g:
        template = g.read()
    
    content_node = markdown_to_html_node(markdown)
    content_in_html = content_node.to_html()
    
    title = extract_title(markdown)
    
    new_template = template.replace(r"{{ Title }}", title).replace(r"{{ Content }}", content_in_html)
    
    with open(dest_path, "w") as h:
        h.write(new_template)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    for content in os.listdir(dir_path_content):
        new_path = os.path.join(dir_path_content, content)
        new_dest = os.path.join(dest_dir_path, content)
        new_dest = new_dest.replace("md", "html")
        if os.path.isfile(new_path):
            generate_page(new_path, template_path, new_dest)
        if os.path.isdir(new_path):
            if not os.path.exists(new_dest):
                os.mkdir(new_dest)
            generate_pages_recursive(new_path, template_path, new_dest)    