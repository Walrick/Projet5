#!/usr/bin/python3
# -*- coding: utf8 -*-

import requests
import resource.category
import resource.product

class OpenFoodFactQuery():
    
    """ Openfoodfact query class for launch the query """

    def __init__(self):
        
        self.base_url = "https://fr.openfoodfacts.org/"
         
    def get_category(self):
        
        """ build category """

        search = {
            'countries': 'France',
            'json': 1,
            }
        send = requests.get(self.base_url + "categories",  params=search)
        category = send.json()
        
        return category["tags"]

            
    def product_requets_by_category(self, category, page):
        
        """build product by query in category"""

        search = {
            'action': 'process',
            'tagtype_0': 'states', #which subject is selected (states)
            'tag_contains_0': 'contains',#contains or not
            'tag_0': "en:checked", #parameters to choose
            'tagtype_1': 'categories', 
            'tag_contains_1': 'contains',
            'tag_1': category,        
            'countries': 'France',
            'json': 1,
            'page': page
            }
        
        send = requests.get(self.base_url + "cgi/search.pl" , params=search)
        products = send.json()  
        
        return products["products"]
        
  
                

    
