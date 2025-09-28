# test_constructors_protein_powder.py
#
# Author: Ben Aylward
# MSE240: Assignment 1
# Sept 28 - 2025
# Unit tests for mutators 

#Input:
#Output: 

import unittest
from protein_powder import ProteinPowder

def make_typical():
    return ProteinPowder("Diesel", "Peanut Butter", False, 25.0, 2.0, 1.5, 121, 49.99)


class TestProteinPowderMutators(unittest.TestCase):

    def test_set_price_typical(self):
        """
        Unit: set_price
        Category: Typical
        Input: set_price(59.99)
        Output: 59.99
        """
        typical1 = make_typical()
        typical1.set_price(59.99)

        self.assertAlmostEqual(typical1.get_price(), 59.99)

    def test_set_price_unusual(self):
        """
        Unit: set_price
        Category: Unusual
        Input: set_price(10000.0)
        Output: 10000.0
        """
        unusual1 = make_typical()
        unusual1.set_price(10000.0)
        self.assertAlmostEqual(unusual1.get_price(), 10000.0)

    def test_set_price_error(self):
        """
        Unit: set_price
        Category: error
        Input: set_price(-5.0)
        Output: valueerror
        """
        error1 = make_typical()
        
        with self.assertRaises(ValueError):
            error1.set_price(-5.0)

    def test_set_price_type_error(self):
        """
        Unit: set_price
        Category: error
        Input: set_price("free")
        Output: typeerror
        """
        error2 = make_typical()

        with self.assertRaises(TypeError):
            error2.set_price("free")


