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
            for text in data["text_item_selec"]:
                print(text)
                
        if "list_item_category" in data:
            for item in data["list_item_category"]:
                print(str(item[0]) + " : " +item[1])
                
        if "list_item_products" in data:
            for item in data["list_item_products"]:
                print(str(item[0]) + " : " +item[1]+ ", Nutri-Score : "+ item[3])      
                
        if "list_item_substitut" in data:
            for item in data["list_item_substitut"]:
                print(str(item[0]) + " : " +item[1]+ ", nombre de substitut : "+ str(item[2]))    
                
        if "list_item_products_for_substitut" in data:
            for item in data["list_item_products_for_substitut"]:
                print(str(item[0]) + " : " +item[1]+ ", Nutri-Score : "+ item[3])          
                print("Magasin : " + item[4] + ", Trace : " + item[5] + ", Allergène : "+ item[6])  
                print("URL : " + item[7] ) 
                
        if "list_item_substitut_display" in data:
            for item in data["list_item_substitut_display"]:
                print("Produit : "+ item[0] + ", Nutri-Score : "+ item[1])          
                print("Magasin : " + item[2] + ", Trace : " + item[3] + ", Allergène : "+ item[4])  
                print("URL : " + item[5] )                 
                
        if "text_corp" in data :
            for text in data["text_corp"]:
                print(text)            
            
        if "choise_text" in data:
            print(data["choise_text"])
            choice = input()
            return choice