from textnode import TextNode, text_type_bold

def main():
    testA = TextNode("text sample", text_type_bold, 'https://test.com')
    testB = TextNode("text samples", text_type_bold, 'https://test.com')
    print(repr(testA))


main()




