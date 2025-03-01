from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)


    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.tag == "p":
            return f"<p>{self.value}<p>"
        if self.tag == "a":
            return f"<a {super().props_to_html()}>{self.value}</a>"
        
