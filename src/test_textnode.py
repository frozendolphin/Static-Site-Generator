import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    
    def test_uneq(self):
        n1 = TextNode("This text node", TextType.BOLD_TEXT)
        n2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(n1, n2)
        
    def test_equrl(self):
        n1 = TextNode("This text node", TextType.NORMAL_TEXT, "https://www.google.com/")
        n2 = TextNode("This text node", TextType.NORMAL_TEXT, "https://www.google.com/")
        self.assertEqual(n1, n2)

    def test_unequrl(self):
        n1 = TextNode("This text node", TextType.NORMAL_TEXT, "https://www.gogle.com/")
        n2 = TextNode("This text node", TextType.NORMAL_TEXT, "https://www.google.com/")
        self.assertNotEqual(n1, n2)
        
    def test_uneqtype(self):
        n1 = TextNode("This text node", TextType.NORMAL_TEXT, "https://www.google.com/")
        n2 = TextNode("This text node", TextType.ITALIC_TEXT, "https://www.google.com/")
        self.assertNotEqual(n1, n2)

if __name__ == "__main__":
    unittest.main()