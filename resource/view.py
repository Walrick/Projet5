#!/usr/bin/python3
# -*- coding: utf8 -*-


class View ():
    
    """ View class to communicate with the user """
    
    def __init__ (self):
        
        pass
    
    def display (self, data):
        
        """Dispay fonction"""
        
        if "text_header" in data:
            for text in data["text_header"]:
                print(text)
                
        if "text_item_selec" in data:
            print(data["text_item_selec"][0], data["text_item_selec"][1], data["text_item_selec"][2], data["text_item_selec"][3])
                
        if "list_item_category" in data:
            for item in data["list_item_category"][0]:
                print(str(item[0]) + " : " +item[1])
                
        if "list_item_products" in data:
            for item in data["list_item_products"][0]:
                print(str(item[0]) + " : " +item[1]+ ", Nutri-Score : "+ item[3])            
                
        if "text_corp" in data :
            for text in data["text_corp"]:
                print(text)            
            
        if "choise_text" in data:
            print(data["choise_text"])
            choice = input()
            return choice