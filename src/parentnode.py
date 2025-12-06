from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("invalid HTML: no tag")
        if self.children == None:
            raise ValueError("invalid HTML: children no value")
        
        return f"<{self.tag}{self.props_to_html()}>{self.children}</{self.tag}>"
