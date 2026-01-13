from enum import Enum


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
        
    if textBlock.startswith("> "):
        codeA = True
        for line in blockSplit:
            if not line.strip().startswith("> "):
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
       



           
