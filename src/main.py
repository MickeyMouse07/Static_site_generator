import os
import shutil
import logging
import sys
from copystatic import copyStatic
from generatePage import generate_pages_recursive

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    # file path for copystatic
    base_dir = os.path.dirname(os.path.dirname(__file__))
   
    static_path = os.path.join(base_dir, "static")
    # change "public" to "doc" for github page
    public_path = os.path.join(base_dir, "docs")
    
    #file path for generatePage recursive
    dir_path_content = os.path.join(base_dir,"content")
    template_path = os.path.join(base_dir, "template.html")
    # change "public" to "doc" for github page
    #dest_dir_path = os.path.join(base_dir, "docs")


    if os.path.exists(public_path):
        logging.info("Delete the destination folder successfully!")
        shutil.rmtree(public_path)

    os.makedirs(public_path)    
    copyStatic(static_path, public_path)
    generate_pages_recursive(dir_path_content,template_path, public_path, basepath)


main()




