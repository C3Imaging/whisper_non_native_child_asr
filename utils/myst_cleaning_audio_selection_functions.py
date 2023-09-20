# -*- coding: utf-8 -*-
"""

@author: Rishabh Jain
"""
# Code is better replicable in Spyder and similar tools
#directory =  r'add_path'
#new_directory = r'add_path'

# If dir does not exist otherwise delete next line
# os.mkdir(new_directory)
# os.path.exists(os.path.splitext(wav_name)[0]+".trn")

import os
import shutil
import scipy.io.wavfile as wav


#Copy all the .wav files where .trn subtitle file exists 
# note: amount of for loops can be increased or decreased depending on the structure of directory. 
def copy_wav():
    for file_name in os.listdir(directory):  #Look into sub-folders into directory
        sub_dir_path = directory + '/' + file_name  #look into subfolders in subfolders/ 
        if (os.path.isdir(sub_dir_path)):
            for wav_name in os.listdir(sub_dir_path):
                wavfile = os.path.join(sub_dir_path, wav_name)
                #print(wavfile)
                #(source_rate, source_sig) = wav.read(wavfile)
                #duration_seconds = len(source_sig) / float(source_rate)
                srt = os.path.join(sub_dir_path, os.path.splitext(wav_name)[0]+".trn")
                if (wav_name[-4:] == '.wav') and (os.path.exists(srt)) :
                    wavfile = os.path.join(sub_dir_path, wav_name)
                    (source_rate, source_sig) = wav.read(wavfile) #duration of the clip 
                    duration_seconds = len(source_sig) / float(source_rate)
                    if(duration_seconds>2):
                        filepath = os.path.join(sub_dir_path, wav_name)
                        shutil.copy(filepath, new_directory)
                        shutil.copy(srt, new_directory)

#CORRECT one - copy_wav

copy_wav()

#Copy all the .wav files and .trn subtitle file where .trn file exists 
# This allows to select all the files from the MyST dataset where transcription file exists. 
def copy_wav_trn():
    for file_name in os.listdir(directory):
        sub_dir_path = directory + '/' + file_name
        #print(sub_dir_path)
        if (os.path.isdir(sub_dir_path)):
            for wav_name in os.listdir(sub_dir_path):
                #print(wav_name)
                srt = os.path.join(sub_dir_path, os.path.splitext(wav_name)[0]+".trn")
                #print(srt)
                if (wav_name[-4:] == '.wav') and (os.path.exists(srt)) :
                    filepath = os.path.join(sub_dir_path, wav_name)
                    #print(filepath)
                    shutil.copy(filepath, new_directory)
                    shutil.copy(srt, new_directory)



########################################## version 2
# This version contains length of audio file as parameter to select the audio files between required length
directory =  r'add path'
new_directory = r'add path'               

from tqdm import tqdm

# Code to select all the .wav files and corresponding .trn files  
# note: amount of for loops can be increased or decreased depending on the structure of directory. 
# This is because we only require data which is transcribed and we can ignore the untranscribed data for TTS models for now.                  
def copy_wav2():
    for maindir in tqdm(os.listdir(directory)):                                             #Look into sub-folders inside main directory
        submain = directory + '/' + maindir                                                 #Location of sub_dir
        for file_name in os.listdir(submain):                                               #look into subfolders in subfolders/ 
            sub_dir_path = submain + '/' + file_name                                        #location of sub_dir
            if (os.path.isdir(sub_dir_path)):                                               #check for subfolders in subfolders/ 
                for wav_name in os.listdir(sub_dir_path):                                   #for loop for subdir
                    wavfile = os.path.join(sub_dir_path, wav_name)                          #location of wav file
                    srt = os.path.join(sub_dir_path, os.path.splitext(wav_name)[0]+".trn")  #location of .trn file
                    if (wav_name[-4:] == '.wav') and (os.path.exists(srt)) :                #check for wav and trn file
                        wavfile = os.path.join(sub_dir_path, wav_name)                      #Getting the location of wave file
                        (source_rate, source_sig) = wav.read(wavfile)                       #reading the wav file
                        duration_seconds = len(source_sig) / float(source_rate)             #duration of wav file
                        if(duration_seconds>3 and duration_seconds<20):                     #check for duration length 
                            #filepath = os.path.join(sub_dir_path, wav_name)                #Getting the location of wave file 
                            shutil.copy(wavfile, new_directory)                             #Copy all the wav file to the destination folder
                            shutil.copy(srt, new_directory)                                 #Copy all the srt files to the destination folder 
                         #Directory of target folder with .wav audio files 
