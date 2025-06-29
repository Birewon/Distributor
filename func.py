
import os, shutil

folders = ['Photo', 'Video', 'EXE', 'Files', 'Archives', 'Another'] # Folders


def init_folders(downloads_path):
    download_path = downloads_path # Your path to Downloads
    for folder in folders:
        try:
            os.mkdir(f'{download_path}\\{folder}')
        except:
            pass


def sorting(downloads_path):
    list = os.listdir(downloads_path)
    photo_suf = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.psd']
    video_suf = ['.mp4', '.avi', '.mov', '.mp3', '.wav', '.flac']
    exe_suf = ['.exe', '.msi', '.dmg', '.deb', '.rpm', '.apk', '.app']
    files_suf = ['.py','.txt','.pdf', '.doc', '.docx', '.odt', '.rtf', '.tex', '.md', '.markdown', '.js', '.java', '.cpp', '.c', '.h', '.cs', '.php', '.html', '.css', '.htm', '.json', '.xml', '.csv', '.xls', '.xlsx', '.ods', '.sql', '.db', '.sqlite']
    archives_suf = ['.zip', '.rar', '.7z', '.tar', '.gz']
    for file in list:
        try:
            path_to_file = os.path.join(downloads_path, file)
            filename, file_extension = os.path.splitext(file)
            if file_extension in photo_suf and filename not in folders:
                folder = folders[0]
            elif file_extension in video_suf and filename not in folders:
                folder = folders[1]
            elif file_extension in exe_suf and filename not in folders:
                folder = folders[2]
            elif file_extension in files_suf and filename not in folders:
                folder = folders[3]
            elif file_extension in archives_suf and filename not in folders:
                folder = folders[4]
            else:
                if filename in folders or file_extension == '':
                    continue
                else:
                    folder = folders[5]
            print(file)
            print(folder)
            path_to_new_folder = os.path.join(downloads_path, folder, file)
            os.replace(path_to_file, path_to_new_folder)
            print(f'to {folder}')
        except:
            pass

