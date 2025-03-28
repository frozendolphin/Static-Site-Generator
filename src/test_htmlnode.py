import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLnode(unittest.TestCase):

    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_one(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_repr_all(self):
        node = HTMLNode("a", "Click Me!", [], {"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), "tag:a, val:Click Me!, children:[], props:{'href': 'https://www.google.com'}")
    
    def test_repr_none(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.__repr__(), "tag:None, val:None, children:None, props:None")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_all(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click Me!</a>')
        
    def test_leaf_to_html_novalue(self):
        node = LeafNode("p", None, None)
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "Hello!!!")
        self.assertEqual(node.to_html(), "Hello!!!")
        
    def test_leaf_to_html_none(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()
    
if __name__ == "__main__":
    unittest.main()