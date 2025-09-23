#src/protein_powder.py

#class design 

#baylward@uwaterloo.ca
#20945379

class ProteinPowder:
    def __init__(self, _brand:str, _flavour: str, _price: float, _is_vegan:bool, 
                 _protein_per_serving_grams: float, _carbs_per_serving_grams: float, 
                 _fats_per_serving_grams: float, _calories_per_serving:int ):
        pass

#Accessors: 
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

    def get_avalible_flavours(self):
        pass

    def get_avalible_flavours(self):
        pass



#Mutators: 

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

#Calculated Accessors

    def get_calories_from_macros(self):
        pass

    def get_price_per_gram_protein(self):
        pass