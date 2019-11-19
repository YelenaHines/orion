# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 07:31:58 2019

@author: ksclar1
"""

# The goal of this app is to allow SSMT to login each day and execute the pending request search in ORION

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select

import time
import os
#import tkinter



page= "https://google.com"

orion= "http://w3.regsciweb.monsanto.com/Orion/OrionLogon"

orion_request= "http://w3.regsciweb.monsanto.com/Orion/screens/request/manageQueue/plant/manageQueue.jsp" 

userID = os.getenv('username')
    
#userID=input ("Enter_your_userID_followed_by_enter:")

#password=input ("Enter_your_password_followed_by_enter:")
password = os.getenv('myorionpassword')
#driver = webdriver.Ie()
capabilities = {
          'browserName': 'chrome',
          'chromeOptions':  {
            'useAutomationExtension': False,
            'forceDevToolsScreenshot': True,
            'args': ['--start-maximized', '--disable-infobars']
          }
        }
driver = webdriver.Chrome(desired_capabilities=capabilities)
#driver = webdriver.Chrome()

driver.get(orion)
    
#clear the username
driver.find_element_by_name("j_username").clear()

driver.find_element_by_name("j_username").send_keys(userID)

driver.find_element_by_name("j_password").send_keys(password)

driver.find_element_by_class_name("button").click()

driver.get(orion_request)

time.sleep(0.5)

driver.find_element_by_id("pend").click()

driver.find_element_by_id("ship").click()

driver.find_element_by_id("prog").click()

driver.find_element_by_id("appr").click()

driver.find_element_by_id("updateButton").click()












