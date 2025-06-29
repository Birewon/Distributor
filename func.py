
import os, shutil

def init_folders(downloads_path):
    download_path = downloads_path # Your path to Downloads
    folders = ['Photo', 'Video', 'EXE', 'Files', 'Archives', 'Another'] # Folders
    for folder in folders:
        try:
            os.mkdir(f'{download_path}\\{folder}')
        except:
            pass


def sorting(downloads_path):
    list = os.listdir(downloads_path)
    for file in list:
        try:
            path_to_file = os.path.join(downloads_path, file)
            path_to_new_folder = os.path.join(downloads_path, 'Files', file)
            os.replace(path_to_file, path_to_new_folder)
        except:
            pass

