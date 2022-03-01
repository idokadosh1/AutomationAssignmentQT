# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:49:37 2022

@author: idokadosh
"""
from AutomationAssignment import getDataFromQualitestWebPage
import pytest
import unittest
import json
import pandas as pd

# Qualitest Conatct us system tests
#TODO: load Dictionary from config file 
#TDD input parser 


data = json.load(open('config.json'))
#TODO: load path from config file 
path = data['path_for_inputs_uitests']
df = pd.read_excel(path)

myDictionary = json.load(open('dictionary.json'))

# Grouping
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