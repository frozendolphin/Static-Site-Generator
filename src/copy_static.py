import os
import shutil



def delete_public_content(dir_to_copy):
    if os.path.exists(dir_to_copy):
        shutil.rmtree(dir_to_copy)
    os.mkdir(dir_to_copy)
    
def copy_static_to_public(dir_to_copy):  
    if not os.path.exists("./static"):
        return None     
    file_paths = get_static_file_list("./static", dir_to_copy)
    for path in file_paths:
        new_path = path.replace("static/", dir_to_copy)
        shutil.copy(path, new_path)

def get_static_file_list(folder_path, dir_to_copy):
    file_paths = []
    for path in os.listdir(folder_path):
        new_path = os.path.join(folder_path, path)
        if os.path.isfile(new_path):
            file_paths.append(new_path)
        if os.path.isdir(new_path):
            dir_path = new_path.replace("static/", dir_to_copy)
            os.mkdir(dir_path)
            file_paths.extend(get_static_file_list(new_path, dir_to_copy))
    return file_paths