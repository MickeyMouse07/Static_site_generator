from textnode import TextNode, TextType

def main():
     #node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
     node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
     print(node)


main()




