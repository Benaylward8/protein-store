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
        #Note that the brand and flavour must be in the _AVALIBLE_BRANDS and _AVALIBLE_FLAVOURS set
        self._typical1 = ProteinPowder(

            _brand="Diesel",
            _flavour="Vanilla",
            _is_vegan=False,
            _protein_per_serving_grams=25.0,
            _carbs_per_serving_grams=2.0,
            _fats_per_serving_grams=1.5,
            _calories_per_serving=121,
            _price=49.99, )
        


    
    def test_constructor_basic_accesors_typical(self):
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

            Output: Class created succesfully

         """ 
        typical1 = self._typical1

        self.assertIsNotNone(typical1)
        self.assertEqual(type(typical1), ProteinPowder)

        #Accessors: Typical Scenario
        self.assertEqual(typical1.get_brand(), "Diesel")
        self.assertEqual(typical1.get_flavour(), "Vanilla")
        self.assertEqual(typical1.get_name(), "Diesel Vanilla")
        self.assertAlmostEqual(typical1.get_price(), 49.99)
        self.assertFalse(typical1.is_vegan())
        self.assertAlmostEqual(typical1.get_protein_per_serving_grams(), 25.0)
        self.assertAlmostEqual(typical1.get_carbs_per_serving_grams(), 2.0)
        self.assertAlmostEqual(typical1.get_fats_per_serving_grams(), 1.5)
        self.assertEqual(typical1.get_calories_per_serving(), 121)


    def test_constructor_invalid_brand(self): 
        """Tests constructor with a brand input that is not in _AVALIBLE_BRANDS
        Category: Error
        Input:  
                    _brand: "Rule1",
                    _flavour:"Peanut Butter",
                    _is_vegan: False,
                    _protein_per_serving_grams: 25.0,
                    _carbs_per_serving_grams: 2.0,
                    _fats_per_serving_grams: 1.5,
                    _calories_per_serving: 121
                    _price: 49.99

            Output: Raises ValueError
            """
        with self.assertRaises(ValueError):
            ProteinPowder("Rule1","Vanilla",False,25.0,2.0,1.5,121,49.99)
        

    def test_constructor_invalid_flavour(self): 
        """Tests constructor with a flavour input that is not in _AVALIBLE_FLAVOURs
        Category: Error
        Input:  
                    _brand: "Diesel",
                    _flavour:"Strawberry",
                    _is_vegan: False,
                    _protein_per_serving_grams: 25.0,
                    _carbs_per_serving_grams: 2.0,
                    _fats_per_serving_grams: 1.5,
                    _calories_per_serving: 121
                    _price: 49.99

            Output: Raises ValueError
            """
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel","Strawberry",False,25.0,2.0,1.5,121,49.99)

    def test_constructor_negative_price(self): 

        """Tests constructor with a negative price input 
        Category: Error
        Input:  
                    _brand: "Diesel",
                    _flavour:"Peanut Butter",
                    _is_vegan: False,
                    _protein_per_serving_grams: 25.0,
                    _carbs_per_serving_grams: 2.0,
                    _fats_per_serving_grams: 1.5,
                    _calories_per_serving: 121
                    _price: -42.98

            Output: Raises ValueError
            """
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel","Peanut Butter",False,25.0,2.0,1.5,121,-42.98)


    def test_constructor_is_vegan(self): 
        
        """Tests constructor with a string input for _is_vegan
        Category: Error
        Input:  
                    _brand: "Diesel",
                    _flavour:"Peanut Butter",
                    _is_vegan: "No",
                    _protein_per_serving_grams: 25.0,
                    _carbs_per_serving_grams: 2.0,
                    _fats_per_serving_grams: 1.5,
                    _calories_per_serving: 121
                    _price: 49.99

            Output: Raises TypeError
            """
        with self.assertRaises(TypeError):
            ProteinPowder("Diesel","Peanut Butter","No",25.0,2.0,1.5,121,49.99)

    def test_constructor_total_calories_positive(self): 
        """Tests constructor with a negative calories input 
        Category: Error
        Input:  
                    _brand: "Diesel",
                    _flavour:"Peanut Butter",
                    _is_vegan: "False",
                    _protein_per_serving_grams: 25.0,
                    _carbs_per_serving_grams: 2.0,
                    _fats_per_serving_grams: 1.5,
                    _calories_per_serving: 0
                    _price: 49.99

            Output: Raises ValueError
            """
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel","Peanut Butter",False,25.0,2.0,1.5,0,49.99)

    def test_constructor_macros_positive(self): 
        """Tests constructor with a negative proetin,carb,fat input 
        Category: Error
        Input:  
                    _brand: "Diesel",
                    _flavour:"Peanut Butter",
                    _is_vegan: "False",
                    _protein_per_serving_grams: 0,
                    _carbs_per_serving_grams: 0,
                    _fats_per_serving_grams: 0,
                    _calories_per_serving: 121
                    _price: 49.99

            Output: Raises ValueError
            """
        
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel","Peanut Butter",False,0,0,0,121,49.99)

    def test_constructor_macros_within_calories(self): 
        """Tests constructor with a  proetin,carb,fat input that doesnt equal the calories inputted
        Category: Error
        Input:  
                    _brand: "Diesel",
                    _flavour:"Peanut Butter",
                    _is_vegan: "False",
                    _protein_per_serving_grams: 0,
                    _carbs_per_serving_grams: 0,
                    _fats_per_serving_grams: 0,
                    _calories_per_serving: 121
                    _price: 49.99

            Output: Raises ValueError
            """
        with self.assertRaises(ValueError):
            ProteinPowder("Diesel","Peanut Butter",False,1.0,12.0,1.0,250,49.99)
            #These Macros are not within 10% of the calories 
            #(4cals per g of protein, 4cals per. gram of carbs, 9cals per gram of fats)
    
    