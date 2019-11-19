# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 07:31:58 2019

@author: yhine
"""

'''The goal of this app is to provide SST with tools to have increased accessibility within Orion'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
#from selenium.ebdriver.support.ui import WebDriverWait as wait
import time, os
import general_functions as gf
import pyperclip

page= "https://google.com"
orion= "http://w3.regsciweb.monsanto.com/Orion/OrionLogon"
view_container = 'http://w3.regsciweb.monsanto.com/Orion/screens/createContainer/plant/plant_view.jsp'
orion_request= 'http://w3.regsciweb.monsanto.com/Orion/screens/request/manageQueue/plant/manageQueue.jsp'
create_containers = 'http://w3.regsciweb.monsanto.com/Orion/screens/createContainer/plant/plant_create.jsp'

capabilities = {
          'browserName': 'chrome',
          'chromeOptions':  {
            'useAutomationExtension': False,
            'forceDevToolsScreenshot': True,
            'args': ['--start-maximized', '--disable-infobars']
          }
        }
#global variables
userID = os.getenv('username')
password = os.getenv('myorionpassword')
driver = webdriver.Chrome(desired_capabilities=capabilities)


def logon_orion():
    driver.get(orion)
#    driver.set_window_size(1000, 500)
    driver.find_element_by_name("j_username").clear()
    driver.find_element_by_name("j_username").send_keys(userID)
    driver.find_element_by_name("j_password").send_keys(password)
    driver.find_element_by_class_name("button").click()

def logon_with_password(user, user_pass):
    driver.get(orion)
#    driver.set_window_size(1000, 500)
    driver.find_element_by_name("j_username").clear()
    driver.find_element_by_name("j_username").send_keys(user)
    driver.find_element_by_name("j_password").send_keys(user_pass)
    driver.find_element_by_class_name("button").click()

def paste_container(IDs):
    #orionIDs is a list of orion ids needing to be viewed
    time.sleep(2)
    driver.get(view_container)
    for i in IDs:
        time.sleep(1)
        driver.find_element_by_id("containerSelectorTableContainerIdInput").send_keys(
                i, Keys.ENTER)
        time.sleep(2)

def paste_create_container(IDs):
    driver.get(create_containers)
    for i in IDs:
        driver.find_element_by_id("sourceContainerContainerIdInput").send_keys(
                i, Keys.ENTER)
        time.sleep(2)

def get_container_loc(IDs):
    # IDs are a list of container IDs
    #assumes page of view container with containers loaded is already pulled up in Chrome
    x = len(IDs)
    for i in range(x):
        container_id = IDs[i]
        storage_loc = driver.find_element_by_id('containerSelectorTable_storageLocation_{}'.format(i + 1)).text
        shelf = driver.find_element_by_id('containerSelectorTable_shelfNum_{}'.format(i + 1)).text
        box = driver.find_element_by_id('containerSelectorTable_boxNum_{}'.format(i + 1)).text
        treatment_result = check_treatment(i + 1)
        print('\n{} | Location: {} | Shelf: {} | Box: {} | Treated: {}'.format(container_id, storage_loc, shelf, box, treatment_result))

def check_treatment(count):
    result = driver.find_element_by_id('containerSelectorTable_seedTreatment_{}'.format(count)).text
    if result == 'None':
        return False
    elif result == 'none':
        return False
    elif result == u'\x20':
        return False
    else:
        return True

def get_requests():
    driver.get(orion_request)
    driver.find_element_by_id("pend").click()
    driver.find_element_by_id("ship").click()
    driver.find_element_by_id("prog").click()
    driver.find_element_by_id("appr").click()
    driver.find_element_by_id("updateButton").click()

def get_pending_requests():
    driver.get(orion_request)
    driver.find_element_by_id("pend").click()
    driver.find_element_by_id("ship").click()
    driver.find_element_by_id("updateButton").click()


def open_shipTrans():
#    find_shiptrans = driver.find_element_by_id('viewShipmentButton')
    driver.find_element_by_id('viewShipmentButton').click()
    time.sleep(1)
    #select all containers
    select = Select(driver.find_element_by_id('viewSamplesTopPageSelector'))
    select.select_by_value('all')

    driver.find_element_by_id('viewSamples_monNumbers_link').click()

    time.sleep(1)

    gf.select_all()
    gf.copy()

    time.sleep(1)


def search_shipTrans(regEx):
    '''Search shipTransfer form to find regular expression patterns and print the results'''
    text = str(pyperclip.paste())

    groups = []
    for group in regEx.findall(text):
        group = driver.find_element_by_id('requestID').text
        groups.append(group)

    if len(groups) == 0:
        request_ID = driver.find_element_by_id('requestID').text
        print('..\n{} has no samples at Warson'.format(request_ID))
    else:
        orion.get_container_loc(groups)

def get_display_of():
    time.sleep(2)

    display_of = driver.find_element_by_id('viewShipments_numSamples_1').text

    time.sleep(2)

    return display_of

def get_request_id(reqID):
    time.sleep(2)

    try:
        driver.find_element_by_id('requestId_{}'.format(reqID)).click()
    except NoSuchElementException:
        return False

def close():
    driver.close()












