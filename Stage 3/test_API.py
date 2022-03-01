# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:15:23 2022

@author: idokadosh
"""
import unittest
import requests
import json
import pandas as pd

data = json.load(open('config.json'))

STATUS_ERROR_CODE = data['STATUS_ERROR_CODE']
STATUS_SUCCEEDED_CODE = data['STATUS_SUCCEEDED_CODE']

path = data['path_for_inputs_apitests']
df = pd.read_excel(path)



class TestApi(unittest.TestCase):
    
    def test_search_pet_by_id(self):
        pet_id = df.PetId[0]
        url = data['url_for_search_pet_by_id'] + str(pet_id)
        response = requests.get(url)
        self.assertEqual(response.status_code,STATUS_SUCCEEDED_CODE)
        
    def test_search_undefined_user(self):
        userName = df.UserName[0]
        url = data['url_for_search_undefined_user'] + userName
        response = requests.get(url)
        self.assertEqual(response.status_code,STATUS_ERROR_CODE)
    