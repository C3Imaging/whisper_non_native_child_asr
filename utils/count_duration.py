# -*- coding: utf-8 -*-
"""

@author: rjain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: rjain
"""

#----------------------------------------------------------------------------
# To generate range of duration for different audio files range 


def file_path_name(dirname):
    file_paths = []  
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  
    return file_paths   


DIRNAME = r'add_path'


def countdir(DIRNAME):
    dt = {'0-5':0,'5-10':0,'10-20':0,'20-30':0,'30-40':0,'40-50':0,'50-60':0,'60-70':0,'70-80':0,'80-90':0,'90-100':0,'100 above': 0}
    x = 0
    y=y1=y2=y3=y4=y5=y6=y7=y8=y9=y10=y11=0
    files = file_path_name(DIRNAME)                 # get all file-paths of all files in dirname and subdirectories
    for file in tqdm(files):                        # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension
        if (ext == '.wav'):  
            (source_rate, source_sig) = wav.read(file)
            duration_seconds = len(source_sig) / float(source_rate) #duration of wav file
            if (duration_seconds > 0) and (duration_seconds <5) : 
                dt['0-5'] = dt['0-5'] + 1 
                y = y + duration_seconds
            elif (duration_seconds > 5) and (duration_seconds <10) : 
                dt['5-10'] = dt['5-10'] + 1
                y1 = y1 + duration_seconds
            elif (duration_seconds > 10) and (duration_seconds <20) : 
                dt['10-20'] = dt['10-20'] + 1
                y2 = y2 + duration_seconds
            elif (duration_seconds > 20) and (duration_seconds <26) :
                dt['20-30'] = dt['20-30'] + 1
                y3 = y3 + duration_seconds
            elif (duration_seconds > 30) and (duration_seconds <40) : 
                dt['30-40'] = dt['30-40'] + 1
                y4 = y4 + duration_seconds
                print(file)
            elif (duration_seconds > 40) and (duration_seconds <50) : 
                dt['40-50'] = dt['40-50'] + 1
                y5 = y5 + duration_seconds
                print(file)
            elif (duration_seconds > 50) and (duration_seconds <60) : 
                dt['50-60'] = dt['50-60'] + 1
                y6 = y6 + duration_seconds
                print(file)
            elif (duration_seconds > 60) and (duration_seconds <70) : 
                dt['60-70'] = dt['60-70'] + 1
                y7 = y7 + duration_seconds
                print(file)
            elif (duration_seconds > 70) and (duration_seconds <80) : 
                dt['70-80'] = dt['70-80'] + 1
                y8 = y8 + duration_seconds
                print(file)
            elif (duration_seconds > 80) and (duration_seconds <90) : 
                dt['80-90'] = dt['80-90'] + 1
                y9 = y9 + duration_seconds
                print(file)
            elif (duration_seconds > 90) and (duration_seconds <100) : 
                dt['90-100'] = dt['90-100'] + 1
                y10 = y10 + duration_seconds
                print(file)
            elif (duration_seconds > 100) : 
                dt['100 above'] = dt['100 above']+1 
                y11 = y11 + duration_seconds
                print(file)
            x = x+duration_seconds
            #print(duration_seconds)
    
    print('Total Duration ==', x/60, '(in Minutes) ==', x/60/60, '(in hour)')
    print('Count range in seconds for each range \n', dt)
    print('Duration 0-5 ==', y/60, '(in Minutes) ==', y/60/60, '(in hour) \n')
    print('Duration 5-10 ==', y1/60, '(in Minutes) ==', y1/60/60, '(in hour)\n')
    print('Duration 10-20 ==', y2/60, '(in Minutes) ==', y2/60/60, '(in hour)\n')
    print('Duration 20-30 ==', y3/60, '(in Minutes) ==', y3/60/60, '(in hour)\n')
    print('Duration 30-40 ==', y4/60, '(in Minutes) ==', y4/60/60, '(in hour)\n')
    print('Duration 40-50 ==', y5/60, '(in Minutes) ==', y5/60/60, '(in hour)\n')
    print('Duration 50-60 ==', y6/60, '(in Minutes) ==', y6/60/60, '(in hour)\n')
    print('Duration 60-70 ==', y7/60, '(in Minutes) ==', y7/60/60, '(in hour)\n')
    print('Duration 70-80 ==', y8/60, '(in Minutes) ==', y8/60/60, '(in hour)\n')
    print('Duration 80-90 ==', y9/60, '(in Minutes) ==', y9/60/60, '(in hour)\n')
    print('Duration 90-100 ==', y10/60, '(in Minutes) ==', y10/60/60, '(in hour)\n')
    print('Duration 100 above ==', y11/60, '(in Minutes) ==', y11/60/60, '(in hour)\n')

    

#----------------------- Duration each speaker -----------------
# path to single directoy for respective speakers. 

def duration(DIRNAME): 
    x = 0
    files = file_path_name(DIRNAME) 
    for file in files:                        # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension
        if (ext == '.wav'):  
            (source_rate, source_sig) = wav.read(file)
            duration_seconds = len(source_sig) / float(source_rate)
            x = x+duration_seconds
    return x/60


