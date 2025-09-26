# protein_powder.py
#
# Author: Ben Aylward
# Email: baylward@uwaterloo.ca
# Student ID: 20945379 
# MSE240: Assignment 1
# Source code for ProteinPowder Class



class ProteinPowder:
    """
    ProteinPowder
    A class for an object: a tub of Protein Powder, for an online store
    """
    
    #Class Constants (THESE DO NOT CHANGE PER OBJECT)

    _AVAILABLE_BRANDS = {'Diesel','Biox', 'Raw', 'PVL','Ghost','Mutant'}
    _AVAILABLE_FLAVOURS = {'Peanut Butter', 'Vanilla', 'Chocolate', 'Cookies & Cream'}

    #Initialization of the object
    
    def __init__( self, _brand:str, _flavour: str, _is_vegan: bool, 
                 _protein_per_serving_grams: float, _carbs_per_serving_grams: float, 
                 _fats_per_serving_grams: float, _calories_per_serving:int, 
                 _price: float =49.99 ):
        """
        _brand: The brand of protein powder (must be in _AVALIBLE_BRANDS)
        _flavour: The flavour of protein powder (must be in _AVALIBLE_FLAVOURS)
        _is_vegan: booloan specifiyng if the proetiun powder is vegan 
        _protein_per_serving_grams: the amount of protein in a single serving, in grams
        _carbs_per_serving_grams: the amount of carbs in a single serving, in grams
        _fats_per_serving_grams: the amount of fats in a single serving, in grams
        _calories_per_serving: the amount of calories in a single serving, in kcals
        _price: The price of the tub of protein powder in $ CAD, defaults to 49.99 unless specifed (on sale)
        """
        if _brand not in self._AVAILABLE_BRANDS:
            raise ValueError("Brand not in stock")
        
        if _flavour not in self._AVAILABLE_FLAVOURS:
            raise ValueError("Flavour not in stock")
        
        if _price < 0 : 
            raise ValueError("Price Can not be a negative value")
        
        if not isinstance(_is_vegan, bool):
            raise TypeError("_is_vegan must be entered as a bool")
        
        if _calories_per_serving <= 0 : 
            raise ValueError("Calories must be greater than 1")
        
        if _protein_per_serving_grams <= 0 :
            raise ValueError("protein must be greater than 1")
        
        if _carbs_per_serving_grams <= 0 :
            raise ValueError("carbohydrates must be greater than 1")
        
        if _fats_per_serving_grams <= 0 :
            raise ValueError("fats must be greater than 1")
        
        #checking to see if the macros add up to within 10% of the calories (allowing for nutrition label varience) 
        macros = (_protein_per_serving_grams*4)+(_carbs_per_serving_grams*4)+(_fats_per_serving_grams*9)
        lower_threshold = round(macros*0.9)
        upper_threshold = round(macros*1.1)
        
        if _calories_per_serving > upper_threshold:
            raise ValueError
        
        if _calories_per_serving < lower_threshold: 
            raise ValueError

        self._brand  = _brand
        self._flavour = _flavour
        self._is_vegan = bool(_is_vegan)

        self._protein_per_serving_grams = float(_protein_per_serving_grams)
        self._carbs_per_serving_grams   = float(_carbs_per_serving_grams)
        self._fats_per_serving_grams    = float(_fats_per_serving_grams)
        self._calories_per_serving      = int(_calories_per_serving)

        self._price = float(_price)

        #creates name 
        self._name  = f"{self._brand} {self._flavour}"


#Accessors: See Test Plan and Specification Doc for details 
    def get_name(self):
        return self._name

    def get_brand(self): 
        return self._brand

    def get_flavour(self): 
        return self._flavour

    def get_price(self):
        return self._price

    def is_vegan(self):
        return self._is_vegan

    def get_protein_per_serving_grams(self):
        return self._protein_per_serving_grams

    def get_carbs_per_serving_grams(self):
        return self._carbs_per_serving_grams

    def get_fats_per_serving_grams(self):
        return self._fats_per_serving_grams

    def get_calories_per_serving(self):
        return self._calories_per_serving


#returns copy of the class constants so that the user cannot change the original values
    def get__AVAILABLE_FLAVOURS(self):
        return set(self._AVAILABLE_FLAVOURS)

    def get_AVAILABLE_BRANDS(self):
        return set(self._AVAILABLE_BRANDS)



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