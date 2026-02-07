import os
from markdown_blocks import markdown_to_html_node,extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path,"r") as f:
        markDownFile = f.read()
       

    with open(template_path,"r") as f:
        templeteFile = f.read()
        


    rootNode = markdown_to_html_node(markDownFile)
    htmlContent = rootNode.to_html()
    xTiltle = extract_title(markDownFile)

    newMarkdown = templeteFile.replace("{{ Title }}", xTiltle)
    newMarkdown = newMarkdown.replace("{{ Content }}", htmlContent)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
         f.write(newMarkdown)



    