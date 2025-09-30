# tests_accessors.py
#
# Author: Ben Aylward
# MSE240: Assignment 1
# Sept 28 - 2025
# Unit tests for accessors 

#Input:
#Output: 

import unittest
from protein_powder import ProteinPowder

def typical_case():
    return ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 1.5, 121, 49.99)

class TestProteinPowderAccessors(unittest.TestCase):

    def setUp(self):
        self.typical1 = typical_case()

    def test_basic_getters_typical(self):
        """
        Unit: all accessors
        Category: Typical 
        Input: typical_case scenario
        Output: getters return expeceted values
        
        """
        typical1 = self.typical1
        self.assertIsNotNone(typical1)
        self.assertEqual(type(typical1), ProteinPowder)

        #Accessors: Typical Scenario
        self.assertEqual(typical1.get_brand(), "Diesel")
        self.assertEqual(typical1.get_flavour(), "Peanut Butter")
        self.assertEqual(typical1.get_name(), "Diesel Peanut Butter")
        self.assertAlmostEqual(typical1.get_price(), 49.99)
        self.assertFalse(typical1.is_vegan())
        self.assertAlmostEqual(typical1.get_protein_per_serving_grams(), 25.0)
        self.assertAlmostEqual(typical1.get_carbs_per_serving_grams(), 2.0)
        self.assertAlmostEqual(typical1.get_fats_per_serving_grams(), 1.5)
        self.assertEqual(typical1.get_calories_per_serving(), 121)

    def test_get_name_after_set_brand(self):
        """
        Unit: get_brand
        Category: Typical 
        Input: set_brand("Mutant")
        Output: get_name() = "Mutant Peanut Butter"
        
        """
        typical1 = self.typical1
        typical1.set_brand("Mutant")
        self.assertEqual(typical1.get_name(), "Mutant Peanut Butter")

    def test_get_name_after_set_flavour(self):
        """
        Unit: get_flavour
        Category: Typical 
        Input: set_flavour("Vanilla") 
        Output: get_name() = "Diesel Vanilla"
        
        """
        typical1 = self.typical1
        typical1.set_flavour("Vanilla")
        self.assertEqual(typical1.get_name(), "Diesel Vanilla")





