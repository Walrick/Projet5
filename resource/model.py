#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.constent

      
class Model ():
    
    def __init__(self):
        
        pass
        
    def MAJ(self, data, constent):
        
        
        self.state = {

            constent.home: {
                "text_header": [
                    "1 : Sélectionner une catégorie",
                    "2 : Voir les produits substitués",
                    "3 : Quitter"],
                "choise_text": "Faites votre choix"
            },
        
            constent.category_list: {
                "text_header": [
                    "Choisi parmi les catégories :"
                ],
                "choise_text": "Faites votre choix",
                "list_item_category": maj(data,"list_item_category"),
                    
                "text_corp": [
                    "Pour faire défiler les catégories : <s> pour avancer,"
                    "<z> pour remonter ou revenir en arrière avec <a>.",
                    "Pour sélectionner une catégorie, sélectionner le",
                    "avec le chiffre qui lui est associé."]
            },
        
            constent.produit_list: {
                "text_header": [
                    "Catégorie sélectionner : ",
                    maj(data,"text_header"),
                    "Choisi parmi les produits :"
                ],
                "list_item_products": maj(data,"list_item_products"),
                    
                "choise_text": "Faites votre choix",
                "text_corp": [
                    "Pour faire défiler les produits : <s> pour avancer,",
                    "<z> pour remonter ou revenir en arrière avec <a>.",
                    "Pour sélectionner un produit, sélectionner le",
                    "avec le chiffre qui lui est associé."]
            },
            
            constent.produit_selec: {
                "text_header": [
                    "Choisi parmi les produits :"
                    ],
                "text_item_selec": [
                    "Produit sélectionner : " + maj(data,"text_item_selec_name"),
                    "Nutri-score : " + maj(data,"text_item_selec_nutri-score"),
                    "Magasin : " + maj(data,"text_item_selec_store"),
                    "Trace : " + maj(data,"text_item_selec_trace"),
                    "Allergens : " + maj(data,"text_item_selec_allergens"),
                    "URL : " + maj(data,"text_item_selec_url")
                    ],                
                "list_item_products_for_substitut": maj(data,"list_item_products"),
                "choise_text": "Faites votre choix",
                "text_corp": [
                    "Pour faire défiler les produits : <s> pour avancer,",
                    "<z> pour remonter ou revenir en arrière avec <a>.",
                    "Pour sélectionner un produit et le rentrer en substitut,",
                    "sélectionner le avec le chiffre qui lui est associé."]             
            },
            
            constent.substitut: {
                "text_header": [
                    "Choisi parmi les produits pour voir leurs substituts :"
                    ],
                "list_item_substitut" : maj(data,"list_item_substitut"),
                "choise_text": "Faites votre choix",
                "text_corp": [
                    "Pour faire défiler les produits : <s> pour avancer,",
                    "<z> pour remonter ou revenir en arrière avec <a>.",
                    "Pour sélectionner un produit et voir les substituts,",
                    "sélectionner le avec le chiffre qui lui est associé."]  
            },
            constent.substitut_display: {
                "text_item_selec": [
                    "Produit sélectionner : " + maj(data,"text_item_selec_name"),
                    "Nutri-score : " + maj(data,"text_item_selec_nutri-score"),
                    "Magasin : " + maj(data,"text_item_selec_store"),
                    "Trace : " + maj(data,"text_item_selec_trace"),
                    "Allergens : " + maj(data,"text_item_selec_allergens"),
                    "URL : " + maj(data,"text_item_selec_url")
                    ],   
                "list_item_substitut_display": maj(data,"list_item_substitut_display"),
                "choise_text": "Faites votre choix",
                "text_corp": [
                    "Pour faire défiler les produits : <s> pour avancer,",
                    "<z> pour remonter ou revenir en arrière avec <a>."]  
            },                
                    
        }
        
def maj(data,key):
    
    if key in data:
        return data[key]
    else :
        return ""
    
