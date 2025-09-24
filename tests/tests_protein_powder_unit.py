# protein_powder_unit_tests.py
#
# Author: Ben Aylward
# Email: baylward@uwaterloo.ca
# Student ID: 20945379 
# MSE240: Assignment 1
# Source code for ProteinPowder Class

from protein_powder import ProteinPowder
import unittest

class TestProteinPowder(unittest.TestCase):

    """ 
    
    TestProetinPowder
    
    Unit tests for the ProteinPowder Class
    
    """
    def setUp(self): 
        """
        
        Setting up test cases before each test

        Creates a new ProteinPowder object for multiple tests

        """
        #Typical1: Creating a valid ProteinPowder object
        #Note that the brand and flavour must be in the _AVALIBLE_BRANDS and _AVALIBLE_FLAVOURS

        self._typical1_data = {
            "_brand": "Diesel",
            "_flavour":"Peanut Butter",
            "_price": 49.99, # Default price (optinal)
            "_is_vegan": False,
            "_protein_per_serving_grams": 25.0,
            "_carbs_per_serving_grams": 2.0,
            "_fats_per_serving_grams": 1.5,
            "_calories_per_serving": 121
            }
        
        self._typical1 = ProteinPowder(
            _brand = self._typical1_data["_brand"],
            _flavour = self._typical1_data["_flavour"],
            _is_vegan = self._typical1_data ["_is_vegan"],
            _price = self._typical1_data ["_price"],
            protein_per_serving_grams = self._typical1_data["_protein_per_serving_grams"],
            _carbs_per_serving_grams = self._typical1_data["_carbs_per_serving_grams"],
            _fats_per_serving_grams = self._typical1_data[ "_fats_per_serving_grams"],
            _calories_per_serving = self._typical1_data[ "_calories_per_serving"]
        )


    """"

    Constructor Test for Typical Scenario 

    """
    def test_constructor(self): 
        typical1 = self._typical1

        self.assertIsNotNone(typical1) #checking if typical1 has any data
        self.assertEqual(typical1, ProteinPowder)

        expected_name = f"{self._typical1_data['_brand']} {self._typical1_data['_flavour']}"

        self.assertEqual(typical1.get_name(),expected_name)
        self.assertEqual(typical1.get_brand(),"Diesel")
        

