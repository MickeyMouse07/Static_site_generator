import os
import shutil
import logging
from copystatic import copyStatic
from generatePage import generate_pages_recursive

def main():
    
    # file path for copystatic
    base_dir = os.path.dirname(os.path.dirname(__file__))
    static_path = os.path.join(base_dir, "static")
    public_path = os.path.join(base_dir, "public")
    

    #file path for generatePage recursive
    dir_path_content = os.path.join(base_dir,"content")
    template_path = os.path.join(base_dir, "template.html")
    dest_dir_path = os.path.join(base_dir, "public")




    if os.path.exists(public_path):
        logging.info("Delete public folder successfully!")
        shutil.rmtree(public_path)




    os.makedirs(public_path)    
    copyStatic(static_path, public_path)
    generate_pages_recursive(dir_path_content,template_path,dest_dir_path)


main()




