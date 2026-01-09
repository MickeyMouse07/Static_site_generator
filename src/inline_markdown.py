from textnode import TextNode, TextType
import re



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newNode = [] 


    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            newNode.append(old_node)
            continue


    
        split_nodes = []
        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")


        for i in range(len(sections)): 
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type)) 

        newNode.extend(split_nodes)

    return newNode
              

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    newNode = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            newNode.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)

        if len(images) == 0:
            newNode.append(old_node)
            continue


        split_nodes = []

        original_text = old_node.text
        for img in images:
             sections = original_text.split(f"![{img[0]}]({img[1]})", 1)

             if len(sections) != 2:
                 raise ValueError("mismatched search string")

             if sections[0] != "":
                 split_nodes.append(TextNode(sections[0], TextType.TEXT))

             split_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))

             original_text = sections[1]


        if original_text != "":
            split_nodes.append(TextNode(original_text, TextType.TEXT))
        


        newNode.extend(split_nodes)

    return newNode
                 
   
def split_nodes_link(old_nodes):
    newNode = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            newNode.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)

        if len(links) == 0:
            newNode.append(old_node)
            continue


        split_nodes = []
        original_text = old_node.text
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)

            if len(sections) != 2:
                raise ValueError("mismatched search string")
            

            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            split_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

            original_text = sections[1]

        if original_text != "":
            split_nodes.append(TextNode(original_text, TextType.TEXT))


        newNode.extend(split_nodes)

    return newNode

