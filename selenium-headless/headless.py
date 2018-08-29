#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error
# Author : 
# Date: 
# About: 

'''

ref:
    
'''
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

driver = webdriver.Chrome(executable_path=os.path.abspath("C:\chromedriver_win32\chromedriver.exe"),   chrome_options=chrome_options)


def get_random_int(start, end):
    return random.randint(start, end)

def get_li_info_from_page(driver, li_dev_url):
    
    driver.get(li_dev_url)
    
    # sleep for random seconds
    time.sleep(get_random_int(5, 10))
    
    wait = WebDriverWait(driver, 100)
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'org-top-card-module__company-descriptions')))
    
    for elm in driver.find_elements_by_css_selector(".org-top-card-module__company-descriptions"):print(elm.text)
    
        
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'org-about-us-organization-description')))
    
    for elm1 in driver.find_elements_by_css_selector(".org-about-us-organization-description"):print(elm1.text)
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'org-about-company-module__show-details-button'))).click()
    
    time.sleep(3)
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'org-about-company-module__about-us-extra-left-column')))
    
    for elm2 in driver.find_elements_by_css_selector(".org-about-company-module__about-us-extra-left-column"):print(elm2.text)
    
    
    
    
    
            

def login_and_create_base(li_links):

    # Google Chrome 
    # driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    
    driver.get('https://linkedin.com')
    
        
    #type and find
    search = driver.find_element_by_name('session_key').send_keys('***********')    
    driver.find_element_by_name('session_password').send_keys('********')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    
    for link in li_links:        
        print(link)
       
        get_li_info_from_page(driver, link)
        
        print('------------------------------------------------------------------------------------------------')
        print('\n')
         
    print("Done!!")    

    driver.quit()

li_links= [
     'https://www.linkedin.com/company/10785480/'
]

login_and_create_base(li_links)