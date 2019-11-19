# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:43:16 2019

@author: YHINE
"""

'''this file will act as a module to streamline simple tasks with the computer'''

#Modules
import pyautogui as p
#import time

def select_all():
    '''Highlights the whole page'''
    p.keyDown('ctrl')
    p.press('a')
    p.keyUp('ctrl')

def copy():
    '''Copies to clipboard through keyboard shortcut'''
    p.keyDown('ctrl')
    p.press('c')
    p.keyUp('ctrl')




































