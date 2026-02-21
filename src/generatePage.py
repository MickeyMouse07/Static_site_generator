import os
import shutil
import logging
from markdown_blocks import markdown_to_html_node,extract_title

os.makedirs("log", exist_ok=True)
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(message)s",
    filename = os.path.join("log", "filecopy.log"),
    )

def generate_page(from_path, template_path, dest_path):
    #print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    logging.info(f"Generating page: {from_path} -> {dest_path} using {template_path}")
    

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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
   
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dst_path = os.path.join(dest_dir_path, item)
        mdFile = os.path.join(dest_dir_path, "index.html")

        if os.path.isfile(src_path):
            if item.endswith(".md"):
                generate_page(src_path, template_path, mdFile)
                

        else:
            if not os.path.exists(dst_path):
                logging.info(f"Create dir: {dst_path}")
                os.makedirs(dst_path)

            generate_pages_recursive(src_path, template_path, dst_path)


    





        
       