#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.constent

      
class Model ():
    
    def __init__(self):
        
        pass
        
    def MAJ(self, data, start_list_item, end_list_item, item_select, constent):
        
        
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
                "list_item": [
                    (lambda : data.category)(),
                    (lambda : start_list_item)(),
                    (lambda : end_list_item)(),
                    ],
                    
                "text_corp": [
                    "L'utilisateur aura le choix de faire défiler les catégories",
                    "avec <z> ou <s> ou de revenir en arrière avec <a>.",
                    "Enfin, l'utilisateur pourra sélectionner une catégorie",
                    "avec le chiffre qui lui sera associé."]
            },
        
            constent.produit_list: {
                "text_header": [
                    "Choisi parmi les produits :"
                ],
                "list_item": [
                    (lambda : data.products)(),
                    (lambda : start_list_item)(),
                    (lambda : end_list_item)(),
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
                    "Produit sélectionner :"
                    ],
                "text_item_selec": [
                    (lambda : data.products[item_select].name)(),
                    (lambda : data.products[item_select].stores)(),
                    (lambda : data.products[item_select].nutrition_grade_fr)()
                    ],                
                "list_item": [
                    (lambda : data.products)(),
                    (lambda : start_list_item)(),
                    (lambda : end_list_item)(),
                    ],
                "choise_text": "Faites votre choix"
            }
                    
        }
        