import re

from textnode import TextNode, TextType
from htmlnode import LeafNode

def main():
    new_obj = TextNode("im text", TextType.IMAGES)
    new_obj2 = TextNode("im text", TextType.IMAGES)
    print(new_obj)
    print(new_obj == new_obj2)
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL_TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGES:
            prop = {"src":text_node.url, "alt":text_node.alt}
            return LeafNode("img", "", prop)   
        case _:
            raise Exception("No pattern match")         

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
            continue
        splitted_list = old_node.text.split(delimiter)
        if len(splitted_list)%2 == 0:
            raise Exception("invalid markdown syntax")
        
        for i in range(len(splitted_list)):
            if splitted_list[i] == "":
                continue
            if i%2 == 0:
                new_nodes.append(TextNode(splitted_list[i], TextType.NORMAL_TEXT))
            else:
                new_nodes.append(TextNode(splitted_list[i], text_type))
    return new_nodes
             
def extract_markdown_images(text):
    res = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return res
    
def extract_markdown_links(text):
    res = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return res
    

    
if __name__ == "__main__":
    main()