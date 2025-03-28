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
    
    
if __name__ == "__main__":
    main()