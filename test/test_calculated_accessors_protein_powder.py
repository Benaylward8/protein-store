# test_calculated_accessors_protein_powder.py
#
# Author: Ben Aylward
# MSE240: Assignment 1
# Sept 28 - 2025
# Unit tests for calculated accessors 

#Input:
#Output: 

import unittest
from protein_powder import ProteinPowder

class TestProteinPowderCalculatedAccessors(unittest.TestCase):

    def test_get_calories_from_macros_typical(self):
        """
        Unit: get_calories_from_macros
        Category: Typical
        Input: macros protein:25, carbs:2, fats:1.5
        Output: 4*25 + 4*2 + 9*1.5 = 121.5 -> round -> 122
        """
        typical1 = ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 1.5, 121, 49.99)
        self.assertEqual(typical1.get_calories_from_macros(), 122)
    
    def test_get_calories_from_macros_unusual_rounds_down(self):
        """
        Unit: get_calories_from_macros
        Category: Unusual (rounding just below .5)
        Input: protein:20.0 , carbs: 0.6225, fats:2 , macro cals = 100.49 → rounds down to 100
        Output: 100
        """
        unusual1 = ProteinPowder("Diesel", "Vanilla", False, 20.0, 0.6225, 2, 100, 49.99)
        self.assertEqual(unusual1.get_calories_from_macros(), 100)

    def test_get_calories_from_macros_unusual_rounds_up(self):
        """
        Unit: get_calories_from_macros
        Category: Unusual (rounding exactly .5)
        Input: protein:20.0 , carbs: 0.6275, fats:2 , macro cals = 100.51 → rounds up to 101
        Output: 101
        """
        unusual2 = ProteinPowder("Diesel", "Vanilla", False, 20.0, 0.6275, 2, 101, 49.99)
        self.assertEqual(unusual2.get_calories_from_macros(), 101)

    def test_get_price_per_gram_protein_typical(self):
        """
        Unit: get_price_per_gram_protein
        Category: Typical
        Input: price 50.0, protein 25.0 g
        Output: 2.0
        """
        typical2 = ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 1.5, 121, 50.0)
        self.assertAlmostEqual(typical2.get_price_per_gram_protein(), 2.0)

    def test_get_price_per_gram_protein_unusual_high_price(self):
        """
        Unit: get_price_per_gram_protein
        Category: Unusual
        Input: large price
        Output: ratio still computed 
        """
        unusual3 = ProteinPowder("Diesel", "Vanilla", False, 25.0, 2.0, 1.5, 121, 10000.0)
        self.assertAlmostEqual(unusual3.get_price_per_gram_protein(), 10000.0 / 25.0)

    # Error for dividing by zero isn't here because constructor already restricts protein <= 0.

