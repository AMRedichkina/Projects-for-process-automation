"""
File Organizer:
A script that organizes files into folders
based on specific criteria (e.g. file type, date modified).
"""

import os
import shutil

FILE_NAME = "main.py"
LOCATION = input('Please, enter directory address: ')

def foldername(extension):
    """
    Returns the name of the folder
    that the file should be organized
    in based on the extension of the file.
    """
    if(extension == ""):
        return None
    
    extension_map = {
            "c": "C programs",
            "class": "Java programs", 
            "cpp": "Cpp programs", 
            "doc": "Documents",
            "exe": "Software", 
            "jpg": "Images", 
            "jpeg": "Images", 
            "java": "Java programs", 
            "mkv": "Videos",
            "mp3": "Music", 
            "mp4": "Videos", 
            "pdf": "PDFs", 
            "ppt": "Ppt files",
            "py": "Python files", 
            "raw": "Images", 
            "txt": "Notes-Text", 
            "xlsx": "Excel files",
        }
    return extension_map.get(extension, "Extras")

def organize_files(path):
    """
    The function takes a file path
    as input and organizes all the files
    in the directory into folders,
    based on their file extensions.
    """
    if not os.path.exists(path):
        print("ERROR! Invalid location")

    files = os.listdir(path)
    extensions = {os.path.splitext(file)[1].strip(".") for file in files}

    # Create Folders
    for ext in extensions:
        folder = foldername(ext) or ''
        new = os.path.join(path, folder)
        if folder and not os.path.exists(new):
            os.makedirs(new)

    # Move Files To Folders
    for file in files:
        if file is FILE_NAME:
            continue

        ext = os.path.splitext(file)[1].strip(".")
        folder = foldername(ext)
        if not folder:
            continue

        src = os.path.join(path, file)
        dest = os.path.join(path, folder, file)

        if not os.path.exists(dest):
            shutil.move(src, dest)
            print(f"Moved {file} to {folder}")

    print(f"\nSUCCESS! All files organized in {path}")


if __name__ == "__main__":
    try:
        organize_files(LOCATION)
    except Exception as e:
        print(f"Error: {e}")
