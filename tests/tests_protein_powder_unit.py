# protein_powder_unit_tests.py
#
# Author: Ben Aylward
# Email: baylward@uwaterloo.ca
# Student ID: 20945379 
# MSE240: Assignment 1
# Source code for ProteinPowder Class

from src.protein_powder import ProteinPowder
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
        #Note that the brand and flavour must be in the _AVALIBLE_BRANDS and _AVALIBLE_FLAVOURS set
        
        self._typical1 = ProteinPowder("Diesel","Peanut Butter",False, 25.0, 2.0, 1.5, 121, 49.99)
            


    
    def test_constructor(self):
        """"

    Constructor Test for Typical Scenario 

    Unit: __Init__
    Category: Typical
    Input: 
            _brand: "Diesel",
            _flavour:"Peanut Butter",
            _is_vegan: False,
            _protein_per_serving_grams: 25.0,
            _carbs_per_serving_grams: 2.0,
            _fats_per_serving_grams: 1.5,
            _calories_per_serving: 121
            _price: 49.99

    """ 
        typical1 = self._typical1

        self.assertIsNotNone(typical1) #checking if typical1 has any data

        expected_name = f"{self._typical1_data['_brand']} {self._typical1_data['_flavour']}"

        self.assertEqual(typical1.get_name(),expected_name)
        self.assertEqual(typical1.get_brand(),"Diesel")
        

