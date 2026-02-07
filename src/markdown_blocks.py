import re
from enum import Enum
from inline_markdown import text_to_textnodes
from textnode import (TextNode, TextType, text_node_to_html_node)
from htmlnode import (ParentNode, LeafNode)



class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    result = []
    splitBlock = markdown.split("\n\n")

    for eachSplit in splitBlock:
        cleanSplit = eachSplit.strip()
        if cleanSplit != "":
            result.append(cleanSplit)

    return result


def block_to_block_type(textBlock):
    blockSplit = textBlock.split("\n")

    if textBlock.startswith("#"):
        count = 0
        while count <= len(textBlock) and textBlock[count] == "#":
            count += 1
        
        if count > 0 and count < 6 and textBlock[count] == " ":
            return BlockType.HEADING
        

    if blockSplit[0].startswith('```') and len(blockSplit) > 1:
        if blockSplit[-1].startswith('```'):
            return BlockType.CODE
        
    if textBlock.startswith(">"):
        codeA = True
        for line in blockSplit:
            if not line.strip().startswith(">"):
                codeA = False
                break

        if codeA == True:
            return BlockType.QUOTE

        
    if textBlock.startswith("- "):
        list = True
        for line in blockSplit:
            if not line.strip().startswith("- "):
                list = False
                break

        if list == True:
            return BlockType.UNORDERED_LIST
        
    
    if textBlock.startswith("1. "):
       num = 1
       order = True

       for line in blockSplit:
           if line.strip().startswith(f"{num}. "):
               num += 1
           else:
               order = False
               break
       if order:
           return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH   
       

def text_to_children(text):
    toTextNode = text_to_textnodes(text)
    result = []
    
    for eachNode in toTextNode:
        html_node = text_node_to_html_node(eachNode)
        result.append(html_node)
        

    return result


           
def markdown_to_html_node(markdown):
    block = markdown_to_blocks(markdown)
    children= []

    for eachItem in block:
        typeBlock = block_to_block_type(eachItem)
        
        if typeBlock == BlockType.PARAGRAPH:
            lines = eachItem.split("\n")
            paragraph = " ".join(lines)
            paraNode = text_to_children(paragraph)
            node = ParentNode("p", paraNode)
            lines = eachItem.split("\n")
            children.append(node)

        if typeBlock == BlockType.QUOTE:
            new_lines = []
            lines = eachItem.split("\n")
            for line in lines:
                if not line.startswith(">"):
                    raise ValueError("invalid quote block")
                new_lines.append(line.lstrip(">").strip())
            content = " ".join(new_lines)
            Qblock = text_to_children(content)

            node = ParentNode("blockquote", Qblock)
            children.append(node)

        if typeBlock == BlockType.UNORDERED_LIST:
            items = eachItem.strip().split("-")
            listItem = []

            for item in items:  
                if item != "":
                    child = text_to_children(item.strip("\n").strip())
                    innerNode = ParentNode("li", child)
                    listItem.append(innerNode)
                   
            node = ParentNode("ul", listItem)
            children.append(node)


        
        if typeBlock == BlockType.ORDERED_LIST: 
            items = re.split(r"^\d+\. ", eachItem.strip(), flags=re.MULTILINE)
            listItem = []

            for item in items:  
                if item != "":
                    child = text_to_children(item.strip())
                    innerNode = ParentNode("li", child)
                    listItem.append(innerNode)
                   
            node = ParentNode("ol", listItem)
            children.append(node)


        if typeBlock == BlockType.CODE:
            if not eachItem.startswith("```") or not eachItem.endswith("```"):
                raise ValueError("invalid code block")
            
            txt = eachItem[4:-3]
            child = [text_node_to_html_node(TextNode(txt, TextType.CODE))]    
            node = ParentNode("pre", child)
            children.append(node)


        if typeBlock == BlockType.HEADING:
            numTag = 0
            while numTag <= len(eachItem) and eachItem[numTag] == "#":
                numTag += 1
            
            
            txt = eachItem[numTag + 1:]

            child = text_to_children(txt)

            node = ParentNode(f"h{numTag}", child)
            
            children.append(node)


    bigNode = ParentNode("div", children, None)
    return bigNode

        
def extract_title(markdown):
    block = markdown_to_blocks(markdown)

    for eachItem in block:
        splitLine = eachItem.split("\n")

        for each in splitLine:
            each = each.strip()
            if each.startswith("# "):
                return each[2:].strip()
 
    raise ValueError("No h1 value found")
    





