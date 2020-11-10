#!/usr/bin/python3
# -*- coding: utf8 -*-

import requests
import resource.category
import resource.product

class Api_requets():
    
    def __init__(self):
        
        self.category = {}
        self.products = {}
        send = requests.get("https://fr.openfoodfacts.org/categories.json")
        data = send.json()
        
        print("{} catégories importées".format(data["count"]))
        
        index = 0
        for name in data["tags"]:
            self.category[index] = resource.category.Category(
                name["name"],
                name["id"],
                name["url"],
                name["known"],
                name["products"],
                index)
            index += 1
        
        data = {}
        
    def product_requets(self,category_index,page):
        
        index = 0
        send = requests.get(self.category[category_index].url+page+".json")
        products = send.json()
        for name in products["products"]:
            self.products[index] = resource.product.Product(
                name["product_name"],
                name["states"],
                name["allergens"],
                name["traces"],
                name["categories"],
                name["_keywords"],
                name["url"],
                name["countries"])   
            index += 1
        
        
        
       