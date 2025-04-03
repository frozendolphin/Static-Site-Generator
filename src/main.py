import os
import shutil

from copy_static import delete_public_content, copy_static_to_public
from generate_page import generate_page

def main():
    delete_public_content()
    copy_static_to_public()
    generate_page("content/index.md", "template.html", "public/index.html")
    
    
if __name__ == "__main__":
    main()