# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:49:37 2022

@author: idokadosh
"""
from AutomationAssignment import getDataFromQualitestWebPage
import pytest
import unittest

# Qualitest Conatct us system tests

#TDD input
myDictionary = {"firstNameField": "Ido",
              "lastNameField": "Kadosh",
              "companyNameField": "Qualitest",
              #Disccusion Topic
              "emailField":"IdoKadosh1@gmail.com",
              "phoneField": 524327985,
              #Location
              }
#Grouping
@pytest.mark.missingStringValues 
def test_Missing_FirstName():
    myDictionary['firstNameField']=""
    result = getDataFromQualitestWebPage(myDictionary)
    myDictionary['firstNameField']="Ido"
    assert result in "Please complete all required fields."
    
@pytest.mark.missingStringValues   
def test_Missing_LastName():
    myDictionary['lastNameField']=""
    result = getDataFromQualitestWebPage(myDictionary)
    myDictionary['lastNameField']="Kadosh"
    assert result in "Please complete all required fields."
@pytest.mark.missingStringValues  
def test_Missing_CompanyName():
    myDictionary['companyNameField']=""
    result = getDataFromQualitestWebPage(myDictionary)
    myDictionary['companyNameField']="Qualitest"
    assert result in "Please complete all required fields."
@pytest.mark.missingStringValues
def test_Missing_Email():
    myDictionary['emailField']="" 
    result = getDataFromQualitestWebPage(myDictionary)
    myDictionary['emailField']="IdoKadosh1@gmail.com"
    assert result in "Please complete all required fields."
    
@pytest.mark.unMarkingOption
def test_unMarkingLocation():
    result = getDataFromQualitestWebPage(myDictionary,False,True)
    assert result in "Please complete all required fields."
    
    
@pytest.mark.unMarkingOption   
def test_unMarkingDiscussionTopic():
    result = getDataFromQualitestWebPage(myDictionary,True,False)
    assert result in "Please complete all required fields."