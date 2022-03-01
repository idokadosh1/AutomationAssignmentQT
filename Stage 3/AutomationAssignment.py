# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:49:37 2022

@author: idokadosh
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def getDataFromQualitestWebPage(dict,clickLocation=True,clickDisccusionTopic=True):
    #Install Driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    #Specify Search URL 
    url = "https://qualitestgroup.com/contact-us/"
    driver.get(url)
    driver.implicitly_wait(5)
    
    inputElementFirstName = driver.find_element_by_css_selector('#firstname-34dd68e0-b077-4e95-9243-b861f3f2fd7d').send_keys(dict['firstNameField'])
    inputElementLastName = driver.find_element_by_css_selector('#lastname-34dd68e0-b077-4e95-9243-b861f3f2fd7d').send_keys(dict['lastNameField'])
    inputElementCompanyName = driver.find_element_by_css_selector('#company-34dd68e0-b077-4e95-9243-b861f3f2fd7d').send_keys(dict['companyNameField'])
    if (clickDisccusionTopic):
        clickRadioButton = driver.find_element_by_css_selector('#hsForm_34dd68e0-b077-4e95-9243-b861f3f2fd7d > fieldset:nth-child(4) > div > div > div > ul > li:nth-child(2) > label > span').click()
        driver.implicitly_wait(1)
    try:
        inputElementEmail = driver.find_element_by_css_selector('#secondary_email__c-34dd68e0-b077-4e95-9243-b861f3f2fd7d').send_keys(dict['emailField'])
    except: 
        print("No need to fill email address")
    inputElementPhone = driver.find_element_by_css_selector('#phone-34dd68e0-b077-4e95-9243-b861f3f2fd7d').send_keys(dict['phoneField'])
    if (clickLocation):
        inputElementLocation = driver.find_element_by_css_selector('#location-34dd68e0-b077-4e95-9243-b861f3f2fd7d > option:nth-child(6)').click()
    driver.find_element_by_css_selector('#hsForm_34dd68e0-b077-4e95-9243-b861f3f2fd7d > div > div.actions > input').click()
    return(driver.find_element_by_css_selector('#hsForm_34dd68e0-b077-4e95-9243-b861f3f2fd7d > div.hs_error_rollup > ul > li > label').get_attribute("innerText")) 
    


