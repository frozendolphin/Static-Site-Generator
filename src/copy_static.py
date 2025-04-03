import os
import shutil



def delete_public_content():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("public")
    
def copy_static_to_public():  
    if not os.path.exists("./static"):
        return None     
    file_paths = get_static_file_list("./static")
    for path in file_paths:
        new_path = path.replace("static", "public")
        shutil.copy(path, new_path)

def get_static_file_list(folder_path):
    file_paths = []
    for path in os.listdir(folder_path):
        new_path = os.path.join(folder_path, path)
        if os.path.isfile(new_path):
            file_paths.append(new_path)
        if os.path.isdir(new_path):
            dir_path = new_path.replace("static", "public")
            os.mkdir(dir_path)
            file_paths.extend(get_static_file_list(new_path))
    return file_paths