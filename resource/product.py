#!/usr/bin/python3
# -*- coding: utf8 -*-

class Product():
    
    def __init__(self, product_name, stores, allergens, traces, categories, _keywords, url, nutrition_grade_fr ):
        
        self.name = product_name
        self.stores = stores
        self.allergens = allergens
        self.traces = traces
        self.categories = categories
        self._keywords = _keywords
        self.url = url
        self.nutrition_grade_fr  = nutrition_grade_fr 
        
    def test():
        
        for name in products["products"]:
            if "nutrition_grade_fr" in name :
                self.products[index] = resource.product.Product(
                    name["product_name"],
                    name["stores"],
                    name["allergens"],
                    name["traces"],
                    name["categories"],
                    name["_keywords"],
                    name["url"],
                    name["nutrition_grade_fr"])
                index += 1    
            else :
                self.products[index] = resource.product.Product(
                    name["product_name"],
                    name["stores"],
                    name["allergens"],
                    name["traces"],
                    name["categories"],
                    name["_keywords"],
                    name["url"],
                    "Non applicable")
                index += 1           
