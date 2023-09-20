
# -*- coding: utf-8 -*-
"""

@author: j_ris
"""

# Script to preprocess myst dataset and store the data in the same way it is read
# This code also copy all the transcriptions in Myst (in .trn format) and store them in .txt format

import os
import shutil
import scipy.io.wavfile as wav
from tqdm import tqdm
import re
import string

def file_path_name(dirname):
    file_paths = []  
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  
    return file_paths    

# Read the transcription .trn file 
def convert_txt(file):
    (filepath, ext) = os.path.splitext(file)       
    filepath = filepath + ".trn"
    filehandle = open(filepath, 'r')
    while True:
    # read a single line
        line = filehandle.readline()
        line = re.sub("<[^>]+>","",line)    #removes everthing between '<' and '>' 
        line = line.translate(str.maketrans('', '', string.punctuation))  #removes all the punctuations 
        line = re.sub(' +', ' ', line)
        if not line:
            break
        return line.lower()

# path to directories
DIRNAME = r'D:\myst'
OUTPUTFILE = r'D:\myst_cleaned'


os.mkdir(OUTPUTFILE)
def main():
    files = file_path_name(DIRNAME)                 # get all file-paths of all files in dirname and subdirectories
    for file in tqdm(files):                        # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension
        file_name = os.path.basename(file)
        srt = filepath+'.trn'
        new_path = OUTPUTFILE  + os.path.dirname(file)[len(DIRNAME):] #CHANGE THIS ACCORDING TO USE        
        if (ext == '.wav' and (os.path.exists(srt))):  
            os.makedirs(new_path, exist_ok=True)
            text= convert_txt(file) 
            text_label =  new_path+'\\'+file_name[0:-4]+ '.txt' #file_name name can be changed if directory structure changes. 
            (source_rate, source_sig) = wav.read(file)
            duration_seconds = len(source_sig) / float(source_rate)             #duration of wav file
            if(duration_seconds>5 and duration_seconds<45.5):
                with open(text_label, 'a') as f:        # write results to file 
                    f.write(text)  #save text data in the TTS dataset format
                    f.close()
                    shutil.copy(file, new_path)   


