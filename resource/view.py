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
            print(data["text_item_selec"][0], data["text_item_selec"][1], data["text_item_selec"][2])
                
        if "list_item" in data:
            for key in range(data["list_item"][1], data["list_item"][2]):
                print(str(key) + " : " +data["list_item"][0][key].name)
                
        if "text_corp" in data :
            for text in data["text_corp"]:
                print(text)            
            
        if "choise_text" in data:
            print(data["choise_text"])
            choice = input()
            return choice