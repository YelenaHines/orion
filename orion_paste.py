# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:39:24 2019

@author: YHINE
"""
import re
import time
import datetime
import pyperclip
import Orion_functions as orion
import logging
#import pandas as pd

'''This program is designed to find contianer ID patterns from the 
clipboard, and then launch google chrome > orion > 
view containers to view each match'''

orionLotRegex = re.compile(r'\d{8}-\d{3,4}')
mqtIdentifier = re.compile('^2019')
#display_of = re.compile(r'of \d+')

text = str(pyperclip.paste())

matches = []
def runTest():    
    for groups in orionLotRegex.findall(text):
        if mqtIdentifier.search(groups) == None:
            matches.append(groups)

    orion.logon_orion()
    orion.paste_container(matches)
    
    print('\nResults --')
    orion.get_container_loc(matches)
#    num_containers = orion.get_total_num_of_containers()
    print('\nTotal matches: {}'.format(len(matches)))
    
    orion.close()
    
    return len(matches)

if __name__ == '__main__':
    start_time = time.time()
    actual = runTest()
    end_time = time.time()
    duration = end_time - start_time
    print('\nDuration: {}s'.format(duration))
    
    with open('orion_paste_log.txt', 'r') as f:
        time = datetime.datetime.today()
        logging.basicConfig(filename=f.name, level=logging.INFO)
        logging.info('\n{}: Duration time of viewing {} containers in Orion: {}s'
                     .format(time, actual, duration))

#    df = pd.read_csv('logging_orion.csv')
#    df['Date'] = datetime.date.today()
#    df['Time'] = time.time()
#    df['Run Time Duration'] = str(duration) + 's'
#    df['Number of Containers'] = n
#    df.to_csv('logging_orion.csv')
    











