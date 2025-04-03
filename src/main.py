import os
import shutil

from copy_static import delete_public_content, copy_static_to_public
from generate_page import generate_page, generate_pages_recursive

def main():
    delete_public_content()
    copy_static_to_public()
    generate_pages_recursive("content/", "template.html", "public/")
    
    
if __name__ == "__main__":
    main()