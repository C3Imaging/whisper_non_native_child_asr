# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:13:32 2022

@author: rjain
"""


# VCTK data preparation scripts for MyST dataset

test_folder = r"E:\LibriTTS\dev-clean" 
#output_vctk1=r"E:\Scripts\vctk_prep\vctk_step1.txt"
#output_vctk2=r"E:\Scripts\vctk_prep\vctk_step2.txt"
output_myst_multi1 = r"D:\MyST\myst-v0.4.0-7ee1f59\myst-v0.4.0-7ee1f59\myst_dataprep.txt"
output_myst_multi2 = r"D:\MyST\myst-v0.4.0-7ee1f59\myst-v0.4.0-7ee1f59\myst_main.txt"
myst=r"D:\MyST\myst-v0.4.0-7ee1f59\myst-v0.4.0-7ee1f59\MyST_TTS_5_45.5"
test_txt =r"D:\Speech_Datasets\LibriTTS\test1.txt"
test_txt2 = r"D:\Speech_Datasets\LibriTTS\test2.txt" 


import os
from tqdm import tqdm
import shutil
import scipy.io.wavfile as wav
from pathlib import Path

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
    filehandle = open(file, 'r')
    while True:
    # read a single line
        line = filehandle.readline()
        line = line.strip()
        if not line:
            break
        return line.lower()
    

def preprocess_libriTTS_for_myst_step1():
    files = file_path_name(myst) 
    for file in tqdm(files):                        # execute for each file
        (filepath, ext) = os.path.splitext(file) # get the file extension
        if ext == '.wav':
            txt_file = file[0:-4]+ '.txt'
            a = convert_txt(txt_file)
            print(a)             # result is returned to a
            with open(test_txt, 'a') as f:        # write results to file 
                f.write(file + "|" + a + '\n') 
    

def preprocess_libriTTS_for_fastpitch_step2():
    files = file_path_name(myst) 
    for file in tqdm(files):                        # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension
        base_name = os.path.basename(file)
        pitch_path = r'pitch/' + base_name[:-4] + '.pt'
        if ext == '.wav':
            txt_file = file[0:-4]+ '.normalized.txt'
            a = convert_txt(txt_file)
            print(a)             # result is returned to a
            if a != "":
                with open(test_txt2, 'a') as f:        # write results to file 
                    f.write(file + "|" + pitch_path + "|" + a + '\n')

speaker_folder = r"D:\MyST\myst-v0.4.0-7ee1f59\myst-v0.4.0-7ee1f59\MyST_TTS_5_45.5"
from collections import OrderedDict

def create_dictionary_multispeaker():
    #speaker_list contains path to folder which contains all subfolders as individual speakers
    subfolders = [ f.name for f in os.scandir(speaker_folder) if f.is_dir() ]
    list_ids = [{v: k for k, v in enumerate(OrderedDict.fromkeys(subfolders))}[n] for n in subfolders]
    dict_speaker = dict(zip(subfolders, list_ids))
    return dict_speaker


#step3 - create a multispeaker with speaker ID, mels and pitch
def multispeaker_step1():
    #need mels pitch speakerid
    #create a dictionary of original speaker ids likined with required speaker ids
    files = file_path_name(myst) 
    speaker_dict = create_dictionary_multispeaker()
    for file in tqdm(files):                        # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension     
        if ext == '.wav':                           # only interested if extension is '.wav'
            txt_file = file[0:-4]+ '.txt'
            a = convert_txt(txt_file)    
            path1 = Path(os.path.dirname(file))
            parent_folder = os.path.abspath(os.path.join(path1, os.pardir))
            dirname=os.path.basename(parent_folder)
            print(a)
            print(dirname)               # result is returned to a
            if a is not None:
                with open(output_myst_multi1, 'a') as f:        # write results to file 
                    f.write(file + "|" + a + "|" + str(speaker_dict[dirname]) +  '\n')       

def multispeaker_step2():
    #need mels pitch speakerid
    #create a dictionary of original speaker ids likined with required speaker ids
    files = file_path_name(myst) 
    speaker_dict = create_dictionary_multispeaker()
    for file in tqdm(files):                        # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension
        base_name = os.path.basename(file)
        #mel_path = r'mels/' + base_name[:-4] + '.pt'
        pitch_path = r'pitch/' + base_name[:-4] + '.pt'
        if ext == '.wav':                           # only interested if extension is '.wav'
            txt_file = file[0:-4]+ '.txt'
            a = convert_txt(txt_file)  
            path1 = Path(os.path.dirname(file))
            parent_folder = os.path.abspath(os.path.join(path1, os.pardir))
            dirname=os.path.basename(parent_folder)
            print(a)               # result is returned to a
            if a is not None:
                with open(output_myst_multi2, 'a') as f:        # write results to file 
                    f.write(file + "|" + pitch_path + "|" + a + "|" + str(speaker_dict[dirname]) +  '\n')       
