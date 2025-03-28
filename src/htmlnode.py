import functools

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        return functools.reduce(lambda x,y: x + f' {y[0]}="{y[1]}"' , list(self.props.items()), "")
    
    def __repr__(self):
        return f"tag:{self.tag}, val:{self.value}, children:{self.children}, props:{self.props}"
        

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag == None:
            return self.value
        prop = ""
        if self.props != None:
            prop = self.props_to_html()
        return f"<{self.tag}{prop}>{self.value}</{self.tag}>"
      
      
class ParentNode(HTMLNode):      
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent Node must have a tag")
        if self.children == None:
            raise ValueError("Parent Node must have a child or more")
        text = ""
        for obj in self.children:
            text += obj.to_html()
        return f"<{self.tag}>{text}</{self.tag}>"
    
    
    
        