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
                "list_item_category": [
                    maj(data,"list_item_category")
                    ],
                    
                "text_corp": [
                    "L'utilisateur aura le choix de faire défiler les catégories",
                    "avec <z> ou <s> ou de revenir en arrière avec <a>.",
                    "Enfin, l'utilisateur pourra sélectionner une catégorie",
                    "avec le chiffre qui lui sera associé."]
            },
        
            constent.produit_list: {
                "text_header": [
                    "Catégorie sélectionner : ",
                    maj(data,"text_header"),
                    "Choisi parmi les produits :"
                ],
                "list_item_products": [
                    maj(data,"list_item_products")
                    ],
                "choise_text": "Faites votre choix",
                "text_corp": [
                    "L'utilisateur aura le choix de faire défiler les catégories",
                    "avec <z> ou <s> ou de revenir en arrière avec <a>.",
                    "Enfin, l'utilisateur pourra sélectionner une catégorie",
                    "avec le chiffre qui lui sera associé."]
            },
            
            constent.produit_selec: {
                "text_header": [
                    "Choisi parmi les produits :"
                    ],
                "text_item_selec": [
                    "Produit sélectionner :",
                    maj(data,"text_item_selec_1"),
                    maj(data,"text_item_selec_2"),
                    maj(data,"text_item_selec_3")
                    ],                
                "list_item_products": [
                    maj(data,"list_item_products")
                    ],
                "choise_text": "Faites votre choix"
            }
                    
        }
        
def maj(data,key):
    
    if key in data:
        return data[key]
    
