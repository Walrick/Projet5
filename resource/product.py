#!/usr/bin/python3
# -*- coding: utf8 -*-

class Product():
    
    def __init__(self, product_name, states, allergens, traces, categories, _keywords, url, countries):
        
        self.name = product_name
        self.states = states
        self.allergens = allergens
        self.traces = traces
        self.categories = categories
        self._keywords = _keywords
        self.url = url
        self.countries = countries
