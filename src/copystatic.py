import os
import shutil
import logging

os.makedirs("log", exist_ok=True)
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(message)s",
    filename = os.path.join("log", "filecopy.log"),
    )

def copyStatic(src, dst):

    if os.path.isfile(src):
        logging.info(f"Copy file: {src} -> {dst}")
        shutil.copy2(src, dst)
        return
   
    if not os.path.exists(dst):
        logging.info(f"Create dir: {dst}")
        os.makedirs(dst)
   
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        copyStatic(src_path, dst_path)