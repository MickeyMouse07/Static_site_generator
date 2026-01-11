def markdown_to_blocks(markdown):
    result = []
    splitBlock = markdown.split("\n\n")

    for eachSplit in splitBlock:
        cleanSplit = eachSplit.strip()
        if cleanSplit != "":
            result.append(cleanSplit)

    return result
