import os
import shutil
import logging
from copystatic import copyStatic
from generatePage import generate_page

def main():
    
    # file path for copystatic
    base_dir = os.path.dirname(os.path.dirname(__file__))
    public_path = os.path.join(base_dir, "public")
    static_path = os.path.join(base_dir, "static")

    #file path for generatePage
    from_path = os.path.join(base_dir,"content","index.md")
    template_path = os.path.join(base_dir, "template.html")
    dest_path = os.path.join(base_dir, "public","index.html" )

    if os.path.exists(public_path):
        logging.info("Delete public folder successfully!")
        shutil.rmtree(public_path)

    os.makedirs(public_path)    
    copyStatic(static_path, public_path)
    generate_page(from_path, template_path, dest_path)


main()




