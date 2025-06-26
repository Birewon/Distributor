'''
About "Distributor" program:

This program sorts any files from the Downloads directory into any directory.
Using libraries: os
'''

import os, shutil

def init_folders():
    download_path = r'C:\Users\PC\Downloads' # Your path
    folders = ['Photo', 'Video', 'EXE', 'Files', 'Archives', 'Another'] # Folders
    for folder in folders:
        try:
            os.mkdir(f'{download_path}\\{folder}')
        except:
            pass




