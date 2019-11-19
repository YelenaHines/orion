# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:13:33 2019

@author: YHINE
"""

'''This program is designed to find and report any container IDs that are located at the Warson Warehouse, according to the Orion database'''

import re, time
import Orion_functions as orion
from selenium.webdriver import ActionChains


#global variables
driver = orion.driver
actions = ActionChains(driver)

# Regular expressions
warsonRegex = re.compile(r'(w|W)arson')

orion.logon_orion()
orion.get_pending_requests()

time.sleep(5)

numTotalRequests = driver.find_element_by_id('requestCount').text

list_requests = []

if __name__ == '__main__':
    start_time = time.time()
    
    for i in range(1, int(numTotalRequests) + 1):
        list_requests.append('requestQueue_requestId_{}'.format(i))
    
    for j in list_requests:
        time.sleep(1)
        driver.find_element_by_id(j).click()
        time.sleep(3)
        orion.open_shipTrans()
        time.sleep(3)
        orion.search_shipTrans(warsonRegex)
        orion.get_pending_requests()
        time.sleep(4)

    print('...scanning complete...')
    end_time = time.time()
    duration = end_time - start_time
    print('Duration: {}s'.format(duration))

    orion.close()



