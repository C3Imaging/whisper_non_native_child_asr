# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:28:19 2022

@author: j_ris
"""

#script to count stats in a dataset 


import os
from tqdm import tqdm
import scipy.io.wavfile as wav
import pandas as pd  


def file_path_name(dirname):
    file_paths = []  
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  
    return file_paths   


def listdirs(rootdir):
    path = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        path.append(d)
    return path    

#function to get duration of a folder 
def get_duartion_folder(dirn):
    dur=0
    count = 0
    files = file_path_name(dirn)
    for file in tqdm(files):                        # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension
        if (ext == '.wav'):  
            count = count+1
            (source_rate, source_sig) = wav.read(file)
            duration_seconds = len(source_sig) / float(source_rate)
            dur = dur+duration_seconds
    return float(dur),float(count)
    
def main(dirn):
    spk_name = listdirs(dirn)
    mins = []
    hrs = []
    spk = []
    utt = []
    for i in spk_name:
        ds,count = get_duartion_folder(i)
        print(i[-6:], "{:.2f}".format(ds/60),'(in mins) ', "{:.2f}".format(ds/60/60), '(in hours)\n')
        spk.append(str(i[-6:]))
        mins.append("{:.2f}".format(ds/60))
        hrs.append("{:.2f}".format(ds/60/60))
        utt.append(count)
    xl_dict = {'Speaker': spk, 'Minutes': mins, 'Hours': hrs, 'Utterances':utt}  
    #print(xl_dict)
    df = pd.DataFrame(xl_dict)
    df["Speaker"].str[1:].astype(float)
    df["Minutes"].str[1:].astype(float)
    df["Hours"].str[1:].astype(float)
    df.to_csv('speaker_stats.csv',mode='w+') 
    #return df      


if __name__ == "__main__":
    main()

#------------------------
# Use the code below to read the saved .csv files and provide statistical details of the dataset.

#load the csv with pandas and infer using pandas to display stats of the dataset.
x  = r"location/to/folder/"
folder_stats(x)
ss = pd.read_csv(r"speaker_stats.csv")
ss.describe(include='all')
    
ss['Minutes'].sum()
ss['Hours'].sum()
ss['Utterances'].sum()
ss['Minutes'].max()
ss['Hours'].max()
ss['Utterances'].max()
ss['Minutes'].min()
ss['Hours'].min()
ss['Utterances'].min()
ss['Speaker'][ss['Utterances'] == ss['Utterances'].max()] #where utterance is max, get those speakers. 