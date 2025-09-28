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
    
    def test_set_brand_typical(self):
        """
        Unit: set_brand
        Category: typical
        Input: set_brand("Mutant")
        Output: 
        get_brand = "Mutant"
        get_name = "Mutant Peanut Butter"

        """
        typical2 = make_typical()
        typical2.set_brand("Mutant")

        self.assertEqual(typical2.get_brand(),"Mutant")
        self.assertEqual(typical2.get_name(),"Mutant Peanut Butter")

    def test_set_brand_error(self):
        """
        Unit: set_brand
        Category: error
        Input: set_brand("")
        Output: ValueError
        """
        error3 = make_typical()

        with self.assertRaises(ValueError):
            error3.set_brand("")

    def test_set_brand_error2(self):
        """
        Unit: set_brand
        Category: error
        Input: set_brand("Rule1") # a brand that is not in the set "_AVALIBLE_BRANDS"
        Output: ValueError
        """
        error4 = make_typical()

        with self.assertRaises(ValueError):
            error4.set_brand("Rule1")


    def test_set_flavour_typical(self):
        """
        Unit: set_flavour
        Category: typical
        Input: set_flavour("Chocolate")
        Output: 
        get_flavour = "Diesel"
        get_name = "Diesel Chocolate"

        """
        typical3 = make_typical()
        typical3.set_flavour("Chocolate")

        self.assertEqual(typical3.get_flavour(),"Chocolate")
        self.assertEqual(typical3.get_name(),"Diesel Chocolate")

    def test_set_flavour_error(self):
        """
        Unit: set_flavour
        Category: error
        Input: set_flavour("")
        Output: ValueError

        """
        error5 = make_typical()
        
        with self.assertRaises(ValueError):
            error5.set_flavour("")

    def test_set_flavour_error2(self):
        """
        Unit: set_flavour
        Category: error
        Input: set_flavour("Strawberry") #flavour not in _AVALIBLE_FLAVOURS
        Output: ValueError
        """
        error6 = make_typical()

        with self.assertRaises(ValueError):
            error6.set_flavour("Strawberry")

    def test_set_is_vegan_typical(self):
        """
        Unit: set_is_vegan
        Category: typical
        Input: set_is_vegan(True)
        Output: _is_vegan = True (changes from false)
        """
        typical4 = make_typical() 
        typical4.set_is_vegan(True)
        
        self.assertTrue(typical4.is_vegan())
    
    def test_set_is_vegan_unusual(self):
        """
        Unit: set_is_vegan
        Category: unusual
        Input: set_is_vegan(False) (already is set false)
        Output: _is_vegan = False (no change)
        """
        typical5 = make_typical() 
        typical5.set_is_vegan(False)
        
        self.assertFalse(typical5.is_vegan())

    def test_set_is_vegan_error(self):
        """
        Unit: set_is_vegan
        Category: error
        Input: is_vegan("yes") 
        Output: TypeError
        """
        error7 = make_typical() 
        with self.assertRaises(TypeError):
            error7.set_is_vegan("yes")

    def test_set_protein_per_serving_grams_typical(self):
        """
        Unit: set_protein_per_serving_grams
        Category: typical
        Input: set_protein_per_serving_grams(30.0) 
        Output: get_protein_per_serving_grams = 30.0
        """

        typical6 = make_typical()
        typical6.set_protein_per_serving_grams(30.0)
        
        self.assertAlmostEqual(typical6.get_protein_per_serving_grams(),30.0)

    def test_set_protein_per_serving_grams_unusual(self):
        """
        Unit: set_protein_per_serving_grams
        Category: unusual
        Input: set_protein_per_serving_grams(300.0) 
        Output: get_protein_per_serving_grams= 300.0
        """

        unusual2 = make_typical()
        unusual2.set_protein_per_serving_grams(300.0)
        
        self.assertAlmostEqual(unusual2.get_protein_per_serving_grams(),300.0)

    def test_set_protein_per_serving_grams_error(self):
        """
        Unit: set_protein_per_serving_grams
        Category: error
        Input: set_protein_per_serving_grams(-25.0) 
        Output: ValueError
        """

        error8 = make_typical()
        with self.assertRaises(ValueError):
            error8.set_protein_per_serving_grams(-25.0)
        
    def test_set_protein_per_serving_grams_error2(self):
        """
        Unit: set_protein_per_serving_grams
        Category: error
        Input: set_protein_per_serving_grams(0.0) 
        Output: ValueError
        """

        error9 = make_typical()
        with self.assertRaises(ValueError):
            error9.set_protein_per_serving_grams(0.0)
        
    def test_set_protein_per_serving_grams_error3(self):
        """
        Unit: set_protein_per_serving_grams
        Category: error
        Input: set_protein_per_serving_grams("25") 
        Output: TypeError
        """

        error10 = make_typical()
        with self.assertRaises(TypeError):
            error10.set_protein_per_serving_grams("25")

    def test_set_carbs_per_serving_grams_typical(self):
        """
        Unit: set_carbs_per_serving_grams
        Category: typical
        Input: set_carbs_per_serving_grams(30.0) 
        Output: get_carbs_per_serving_grams = 30.0
        """

        typical7 = make_typical()
        typical7.set_carbs_per_serving_grams(30.0)
        
        self.assertAlmostEqual(typical7.get_carbs_per_serving_grams(),30.0)

    def test_set_carbs_per_serving_grams_unusual(self):
        """
        Unit: set_carbs_per_serving_grams
        Category: unusual
        Input: set_carbs_per_serving_grams(300.0) 
        Output: get_carbs_per_serving_gram= 300.0
        """

        unusual3 = make_typical()
        unusual3.set_carbs_per_serving_grams(300.0)
        
        self.assertAlmostEqual(unusual3.get_carbs_per_serving_grams(),300.0)

    def test_set_carbs_per_serving_grams_error(self):
        """
        Unit: set_carbs_per_serving_grams
        Category: error
        Input: set_carbs_per_serving_grams(-25.0) 
        Output: ValueError
        """

        error11 = make_typical()
        with self.assertRaises(ValueError):
            error11.set_carbs_per_serving_grams(-25.0)
        
    def test_set_carbs_per_serving_grams_error2(self):
        """
        Unit: set_carbs_per_serving_grams
        Category: error
        Input: set_carbs_per_serving_grams(0.0) 
        Output: ValueError
        """

        error12 = make_typical()
        with self.assertRaises(ValueError):
            error12.set_carbs_per_serving_grams(0.0)
        
    def test_set_carbs_per_serving_grams_error3(self):
        """
        Unit: set_carbs_per_serving_grams
        Category: error
        Input: set_carbs_per_serving_grams("25") 
        Output: TypeError
        """

        error13 = make_typical()
        with self.assertRaises(TypeError):
            error13.set_carbs_per_serving_grams("25")
    
    def test_set_fats_per_serving_grams_typical(self):
        """
        Unit: set_fats_per_serving_grams
        Category: typical
        Input: set_fats_per_serving_grams(30.0) 
        Output: get_fats_per_serving_grams = 30.0
        """

        typical8 = make_typical()
        typical8.set_fats_per_serving_grams(30.0)
        
        self.assertAlmostEqual(typical8.get_fats_per_serving_grams(),30.0)

    def test_set_fats_per_serving_grams_unusual(self):
        """
        Unit: set_fats_per_serving_grams
        Category: unusual
        Input: set_fats_per_serving_grams(300.0) 
        Output: get_fats_per_serving_gram= 300.0
        """

        unusual4 = make_typical()
        unusual4.set_fats_per_serving_grams(300.0)
        
        self.assertAlmostEqual(unusual4.get_fats_per_serving_grams(),300.0)

    def test_set_fats_per_serving_grams_error(self):
        """
        Unit: set_fats_per_serving_grams
        Category: error
        Input: set_fats_per_serving_grams(-25.0) 
        Output: ValueError
        """

        error14 = make_typical()
        with self.assertRaises(ValueError):
            error14.set_fats_per_serving_grams(-25.0)
        
    def test_set_fats_per_serving_grams_error2(self):
        """
        Unit: set_fats_per_serving_grams
        Category: error
        Input: set_fats_per_serving_grams(0.0) 
        Output: ValueError
        """

        error15 = make_typical()
        with self.assertRaises(ValueError):
            error15.set_fats_per_serving_grams(0.0)
        
    def test_set_fats_per_serving_grams_error3(self):
        """
        Unit: set_fats_per_serving_grams
        Category: error
        Input: set_fats_per_serving_grams("25") 
        Output: TypeError
        """

        error16 = make_typical()
        with self.assertRaises(TypeError):
            error16.set_fats_per_serving_grams("25")

    def test_set_calories_per_serving_typical(self):
        """
        Unit: set_calories_per_serving
        Category: Typiical
        Input: set_calories_per_serving(125) 
        Output: 125 (within the 10% variance allowed)
        """
        typical9 = make_typical()

        typical9.set_calories_per_serving(125)
        self.assertEqual(typical9.get_calories_per_serving(), 125)

    def test_set_calories_per_serving_unusual(self):
        """
        Unit: set_calories_per_serving
        Category: Unusual
        Input: set_calories_per_serving(110)  (excatly 10% variance from macros)
        Output: 110 (passes)
        """
        unusual5 = make_typical()

        unusual5.set_calories_per_serving(110)
        self.assertEqual(unusual5.get_calories_per_serving(), 110)

    def test_set_calories_per_serving_error1(self):
        """
        Unit: set_calories_per_serving
        Category: error
        Input: set_calories_per_serving(0) 
        Output: ValueError
        """
        error17 = make_typical()
        with self.assertRaises(ValueError):
            error17.set_calories_per_serving(0)

    def test_set_calories_per_serving_error2(self):
        """
        Unit: set_calories_per_serving
        Category: error
        Input: set_calories_per_serving(109)  (ouside allowed range of macros)
        Output: ValueError
        """
        error18 = make_typical()
        with self.assertRaises(ValueError):
            error18.set_calories_per_serving(109)

    def test_set_calories_per_serving_error3(self):
        """
        Unit: set_calories_per_serving
        Category: error
        Input: set_calories_per_serving(120.5) 
        Output: TypeError
        """
        error19 = make_typical()
        with self.assertRaises(TypeError):
            error19.set_calories_per_serving(120.5)
