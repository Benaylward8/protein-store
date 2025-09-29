# test_constructors_protein_powder.py
#
# Author: Ben Aylward
# MSE240: Assignment 1
# Sept 28 - 2025
# Unit tests for constructors 

#Input:
#Output: 

import unittest
from protein_powder import ProteinPowder

class TestProteinPowderConstructor(unittest.TestCase):


    def test_constructor_error_invalid_brand(self):
        """
        Unit: __init__
        Category: Error
        Input: brand not in class set
        Output: ValueError
        """
        with self.assertRaises(ValueError):
            ProteinPowder("Rule1", "Peanut Butter", False, 25.0, 2.0, 1.5, 121, 49.99)

    def test_constructor_error_invalid_flavour(self):
        """
        Unit: __init__
        Category: Error
        Input: flavour not in class set
        Output: ValueError
        """
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel", "Strawberry", False, 25.0, 2.0, 1.5, 121, 49.99)

    def test_constructor_error_negative_price(self):
        """
        Unit: __init__
        Category: Error
        Input: price < 0
        Output: ValueError
        """
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 1.5, 121, -42.98)

    def test_constructor_error_is_vegan_type(self):
        """
        Unit: __init__
        Category: Error
        Input: is_vegan is not bool
        Output: TypeError
        """
        with self.assertRaises(TypeError):
            ProteinPowder("Diesel", "Peanut Butter", "No", 25.0, 2.0, 1.5, 121, 49.99)

    def test_constructor_error_calories_positive(self):
        """
        Unit: __init__
        Category: Error
        Input: calories_per_serving = 0
        Output: ValueError
        """
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 1.5, 0, 49.99)

    def test_constructor_error_macros_positive(self):
        """
        Unit: __init__
        Category: Error
        Input: one or more of protein/carbs/fats <= 0
        Output: ValueError
        """
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel", "Peanut Butter", False, 0.0, 2.0, 1.5, 121, 49.99)
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 0.0, 1.5, 121, 49.99)
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 0.0, 121, 49.99)

    def test_constructor_unusual_calories_at_10_percent_bounds(self):
        """
        Unit: __init__
        Category: Unusual 
        Input: calories exactly at ±10% of macro cals
        Output: allowed
        """
        # the calories from macros are 122; ±10% rounded bounds are 110 and 134 inclusive
        ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 1.5, 110, 49.99)
        ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 1.5, 134, 49.99)

    def test_constructor_error_calories_outside_10_percent(self):
        """
        Unit: __init__
        Category: Error 
        Input: calories lower than 109 or higher than 135 for macros of 25/2/1.5
        Output: ValueError
        """
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 1.5, 108, 49.99)
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 1.5, 136, 49.99)


