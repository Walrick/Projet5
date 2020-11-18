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
