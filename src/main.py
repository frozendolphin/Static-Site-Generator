import os
import shutil

from copy_static import delete_public_content, copy_static_to_public

def main():
    delete_public_content()
    copy_static_to_public()
    
    
if __name__ == "__main__":
    main()