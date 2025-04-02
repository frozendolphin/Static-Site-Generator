import re

from textnode import TextNode, TextType

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
    
def split_nodes_image(old_nodes):
    if old_nodes == []:
        return []
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
            continue
        if old_node.text == "":
            continue
        image_list = extract_markdown_images(old_node.text)
        if image_list == []:
            new_nodes.append(TextNode(old_node.text, TextType.NORMAL_TEXT))
            continue
        new_nodes.extend(splitter(old_node.text, image_list, TextType.IMAGES))
    return new_nodes    

def split_nodes_link(old_nodes):
    if old_nodes == []:
        return []
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
            continue
        if old_node.text == "":
            continue
        
        link_list = extract_markdown_links(old_node.text)
        if link_list == []:
            new_nodes.append(TextNode(old_node.text, TextType.NORMAL_TEXT))
            continue
        new_nodes.extend(splitter(old_node.text, link_list, TextType.LINKS))
    return new_nodes    
        
def splitter(text, lst, type):
    new_list = []
    if lst == []:
        if text:
            new_list.append(TextNode(text, TextType.NORMAL_TEXT))
        return new_list
    match type:
        case TextType.IMAGES:
            delimeter = f"![{lst[0][0]}]({lst[0][1]})"
        case TextType.LINKS:
            delimeter = f"[{lst[0][0]}]({lst[0][1]})"
    splitted = text.split(delimeter, maxsplit=1)
    if splitted[0]:
        new_list.append(TextNode(splitted[0], TextType.NORMAL_TEXT))
    new_list.append(TextNode(lst[0][0], type, lst[0][1]))
    new_list.extend(splitter(splitted[1], lst[1:], type))
    return new_list
        
def text_to_textnodes(text):
    if text == "":
        raise Exception("empty text")
    new_list = []
    node = [TextNode(text, TextType.NORMAL_TEXT)]
    new_list = split_nodes_delimiter(node, "**", TextType.BOLD_TEXT)
    new_list = split_nodes_delimiter(new_list, "_", TextType.ITALIC_TEXT)
    new_list = split_nodes_delimiter(new_list, "`", TextType.CODE_TEXT)
    new_list = split_nodes_link(new_list)
    new_list = split_nodes_image(new_list)
    return new_list
        