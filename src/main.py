#from textnode import TextNode, TextType
import os
import shutil
import logging
from copystatic import copyStatic

def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    public_path = os.path.join(base_dir, "public")
    static_path = os.path.join(base_dir, "static")

    if os.path.exists(public_path):
        logging.info("Delete public folder successfully!")
        shutil.rmtree(public_path)

    os.makedirs(public_path)    
    copyStatic(static_path, public_path)


main()




