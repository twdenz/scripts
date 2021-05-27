#!/usr/bin/env python3

"""
The script loops through the current working dir, finds unique file extensions, 
creates folders for the file extensions and moves the files inside of those folders.
"""

import os
import ntpath

cwd = os.getcwd()
exts = set() # Use set because we want unique file extensions
filelist = dict()

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail

for file in os.listdir(cwd):
    name, ext = os.path.splitext(cwd + file)
    file_ext_name = ext[1:]
    if ext: # Tests whether the extension is a valid string
        exts.add(file_ext_name)
        filelist.setdefault(file_ext_name,[]).append(os.path.join(cwd, file)) # Adds key to dict if not exists, else append to [] list

# print(exts)
# print(filelist)

# Make folders for the amount of file extensions present in the current folder
for ext in exts:
    dirname = ext + '-bestanden'
    path = os.path.join(cwd, dirname)
    try:
        os.mkdir(path)
        print(f"Directory {dirname} created")
    except:
        print(f"Directory {dirname} already existed")
 
# Move the files per extension to the correct folder
for file_ext in filelist:
    # print(f"This key: {key},has the following files: {filelist[key]}")
    for file in filelist[file_ext]:
        file_name = path_leaf(file)
        print(file)
        folder = file_ext + '-bestanden'
        new_file_name = os.path.join(cwd, folder, file_name)
        print(f"Was moved to: \n {new_file_name}")
        os.rename(file, new_file_name)

     
