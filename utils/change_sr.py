# -*- coding: utf-8 -*-
"""

@author: rjain
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:50:48 2022

@author: rjain
"""

#FFMPEG Data Convertion - MyST 

DIRNAME = r"path to directory"
OUTPUTFILE = r"path to output directory"

import os
from tqdm import tqdm
import shutil
import subprocess

def file_path_name(dirname):
    file_paths = []  
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  
    return file_paths    

os.mkdir(OUTPUTFILE)
def change_sr():
    files = file_path_name(DIRNAME)                 # get all file-paths of all files in dirname and subdirectories
    for file in tqdm(files):                        # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension
        file_name = os.path.basename(file)
        new_path = OUTPUTFILE  + os.path.dirname(file)[len(DIRNAME):] #CHANGE THIS ACCORDING TO USE- change in directory name according to folder structure       
        if (ext == '.wav' ):  
            wav_label =  new_path+'\\'+file_name[0:-4]+ '.wav' 
            txt_file = file[0:-4]+ '.txt'
            print(new_path)
            print(wav_label)
            print(file)
            os.makedirs(new_path, exist_ok=True)
            #subprocess.call(f"sox \"{file}\" -c 1 -r 22050 -b 16 \"{wav_label}\"", shell=True) 
            subprocess.call(f"ffmpeg -i \"{file}\" -ar 16000 \"{wav_label}\"", shell=True) # change to above commented code if using sox instead of ffmpeg
            print("Running sox : " + file)
            shutil.copy(txt_file, new_path)
            print('Text Copied')

if __name__ == "__main__":
    change_sr()