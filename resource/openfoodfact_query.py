#!/usr/bin/python3
# -*- coding: utf8 -*-

import requests
import resource.category
import resource.product

class OpenfoodfactQuery():
    
    """ Openfoodfact query class for launch the query """

    def __init__(self):
        
        """ build category """

        self.category = {}
        self.products = {}
        
        search = {
            'countries': 'France',
            'json': 1,
            }
        send = requests.get("https://fr.openfoodfacts.org/categories",  params=search)
        data = send.json()

        print("{} catégories importées".format(data["count"]))

        index = 0
        for name in data["tags"]:
            self.category[index] = resource.category.Category(
                name["name"],
                name["id"],
                name["url"],
                name["known"],
                name["products"]
                )
            index += 1

        data = {}
        
        self.products["defaut"] = resource.product.Product(
            "defaut name",
            "defaut purchase_places",
            "defaut allergens",
            "defaut traces",
            "defaut categories",
            "defaut _keywords",
            "defaut url",
            "defaut nutrition_grade_fr")        
            
    def product_requets_by_category(self, category_index, page, index):
        
        """build product by query in category"""
        
        base_url = "https://fr.openfoodfacts.org/cgi/search.pl"
        
        search = {
            'action': 'process',
            'tagtype_0': 'states', #which subject is selected (states)
            'tag_contains_0': 'contains',#contains or not
            'tag_0': "en:checked", #parameters to choose
            'tagtype_1': 'categories', 
            'tag_contains_1': 'contains',
            'tag_1': self.category[category_index].name,        
            'countries': 'France',
            'json': 1,
            'page': page
            }
        
        send = requests.get(base_url , params=search)
        products = send.json()
        
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
                
        return index
    
    
    def product_requets_by_product(self, product_index, page, index):
        
        """build product by query in product"""
        
        base_url = "https://fr.openfoodfacts.org/cgi/search.pl"
        
        search = {
            'action': 'process',
            'tagtype_0': 'states', #which subject is selected (states)
            'tag_contains_0': 'contains',#contains or not
            'tag_0': "en:checked", #parameters to choose
            'tagtype_1': 'categories', 
            'tag_contains_1': 'contains',
            'tag_1': self.category[category_index].name,        
            'countries': 'France',
            'json': 1,
            'page': page
            }
        
        send = requests.get(base_url , params=search)
        products = send.json()    