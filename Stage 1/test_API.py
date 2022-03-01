# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:15:23 2022

@author: idokadosh
"""
import unittest
import requests
import json



class TestApi(unittest.TestCase):
    
    def test_search_pet_by_id(self):
        pet_id = 1
        url = "https://petstore.swagger.io/v2/pet/1"
        response = requests.get(url)
        jsonResponse = response.json()
        self.assertEqual(pet_id,jsonResponse['id'])
        
    def test_search_user(self):
        userName = "blabla"
        url = "https://petstore.swagger.io/v2/user/blabla"
        response = requests.get(url)
        self.assertEqual(response.status_code,404)