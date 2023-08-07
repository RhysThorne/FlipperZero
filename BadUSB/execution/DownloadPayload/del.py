import os
import shutil

# Define the directory path
directory_path = r"D:/Packs"

# Define the folder name to exclude
exclude_folder = "win-x64"

# Walk through the directory tree
for root, dirs, files in os.walk(directory_path, topdown=False):
    # Exclude the folder specified
    if exclude_folder in dirs:
        dirs.remove(exclude_folder)
    
    # Delete all files
    for file in files:
        file_path = os.path.join(root, file)
        os.remove(file_path)
    
    # Delete all empty directories
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        os.rmdir(dir_path)

# Delete the root folder if empty
if len(os.listdir(directory_path)) == 0:
    os.rmdir(directory_path)
