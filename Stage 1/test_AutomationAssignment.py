# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:49:37 2022

@author: idokadosh
"""
from AutomationAssignment import getDataFromQualitestWebPage
import pytest
import unittest
import pandas as pd
# Qualitest Conatct us system tests


myDictionary = {"firstNameField": "",
               "lastNameField": "",
               "companyNameField": "",
               #Disccusion Topic
               "emailField":"",
               #"phoneField": None,
               #Location
               }
#DDT input
path = (r'C:\Users\idoka\input.xlsx')
df = pd.read_excel(path)


#Grouping
@pytest.mark.missingStringValues 
def test_Missing_FirstName():
    firstNameInput = df.FName[0]
    myDictionary['firstNameField'] = firstNameInput
    result = getDataFromQualitestWebPage(myDictionary)
    assert result in "Please complete all required fields."
    
@pytest.mark.missingStringValues   
def test_Missing_LastName():
    lastNameInput = df.LName[1]
    myDictionary['lastNameField'] = lastNameInput
    result = getDataFromQualitestWebPage(myDictionary)
    assert result in "Please complete all required fields."
