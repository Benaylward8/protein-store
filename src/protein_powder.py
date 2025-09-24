# protein_powder.py
#
# Author: Ben Aylward
# Email: baylward@uwaterloo.ca
# Student ID: 20945379 
# MSE240: Assignment 1
# Source code for ProteinPowder Class



class ProteinPowder:
    """ProteinPowder
        A class for an object: a tub of Protein Powder, for an online store
     """
    
    #Class Constants (THESE DO NOT CHANGE PER OBJECT)

    _AVALIBLE_BRANDS = {'Diesel','Biox', 'Raw', 'PVL','Ghost','Mutant'}
    _AVALIBLE_FLAVOURS = {'Peanut Butter', 'Vanilla', 'Chocolate', 'Cookies & Cream'}

    #Initialization of the object
    
    def __init__( self, _brand:str, _flavour: str, _is_vegan: bool, 
                 _protein_per_serving_grams: float, _carbs_per_serving_grams: float, 
                 _fats_per_serving_grams: float, _calories_per_serving:int, 
                 _price: float =49.99 ):
        """
        _brand: The brand of protein powder (must be in _AVALIBLE_BRANDS)
        _flavour: The flavour of protein powder (must be in _AVALIBLE_FLAVOURS)
        _price: The price of the tub of protein powder in $ CAD, defaults to 49.99 unless specifed (on sale)
        _is_vegan: booloan specifiyng if the proetiun powder is vegan 
        _protein_per_serving_grams: the amount of protein in a single serving, in grams
        _carbs_per_serving_grams: the amount of carbs in a single serving, in grams
        _fats_per_serving_grams: the amount of fats in a single serving, in grams
        _calories_per_serving: the amount of calories in a single serving, in kcals
        """
        pass

#Accessors: See Test Plan and Specification Doc for details 
    def get_name(self):
        pass

    def get_brand(self): 
        pass

    def get_flavour(self): 
        pass

    def get_price(self):
        pass

    def is_vegan(self):
        pass

    def get_protein_per_serving_grams(self):
        pass

    def get_carbs_per_serving_grams(self):
        pass

    def get_fats_per_serving_grams(self):
        pass

    def get_calories_per_serving(self):
        pass

    def get__AVALIBLE_FLAVOURS(self):
        pass

    def get_AVALIBLE_BRANDS(self):
        pass



#Mutators: See Test Plan and Specification Doc for details 

    def set_brand(self, new_brand:str):
        pass

    def set_flavour(self, new_flavour:str):
        pass

    def set_price(self, new_price:str):
        pass

    def set_is_vegan(self, flag:bool):
        pass 

    def set_protein_per_serving_grams(self, grams:float):
        pass

    def set_carbs_per_serving_grams(self, grams:float):
        pass

    def set_fats_per_serving_grams(self, grams:float):
        pass

    def set_calories_per_serving(self, kcal:int):
        pass

#Calculated Accessors: See Test Plan and Specification Doc for details 

    def get_calories_from_macros(self):
        pass

    def get_price_per_gram_protein(self):
        pass