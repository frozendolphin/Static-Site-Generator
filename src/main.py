from textnode import TextNode, TextType

def main():
    new_obj = TextNode("im text", TextType.IMAGES)
    new_obj2 = TextNode("im text", TextType.IMAGES)
    print(new_obj)
    print(new_obj == new_obj2)
    
    
if __name__ == "__main__":
    main()