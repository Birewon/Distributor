'''
About "Distributor" program:

This program sorts any files from the Downloads directory into any directory.
Using libraries: os
'''

import os, shutil
import func

downloads_path = r'C:\Users\Birewon\Downloads'

func.init_folders(downloads_path)
func.sorting(downloads_path)




