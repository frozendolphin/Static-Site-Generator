import os
import shutil
import sys

from copy_static import delete_public_content, copy_static_to_public
from generate_page import generate_pages_recursive

def main():
    dir_to_copy, basepath = get_basepath()
    delete_public_content(dir_to_copy)
    copy_static_to_public(dir_to_copy)
    generate_pages_recursive("content/", "template.html", dir_to_copy, basepath)

    
def get_basepath():
    if len(sys.argv) > 1:
        return ("docs/", sys.argv[1])
    return ("public/", "/")
    
if __name__ == "__main__":
    main()