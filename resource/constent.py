#!/usr/bin/python3
# -*- coding: utf8 -*-


START_LIST_ITEM = 0
END_LIST_ITEM = 20



class Constent():
    
    def __init__(self):
        
        self.start_list_item = START_LIST_ITEM
        self.end_list_item = END_LIST_ITEM
    
    
    def build_table(self,data):
        
        
        self.STATE = {
            "choice error" : {
                "text_header" : [
                    "Ce choix n'est pas correct"]
                },
                
            "home" : {
                "text_header" : [
                    "1 : Sélectionner une catégorie",
                    "2 : Voir les produits substitués",
                    "3 : Quitter"],
                "choise_text" : "Faites votre choix"
                },
            
            "category" : {
                "text_header" : [
                    "Choisi parmi les catégories :"
                ],
                "choise_text" : "Faites votre choix",
                "list_item" : [
                    data, 
                    self.start_list_item, 
                    self.end_list_item],
                "text_corp" : [
                    "L'utilisateur aura le choix de faire défiler",
                    "avec <z> ou <s> les catégories",
                    "ou de revenir en arrière avec <a>.",
                    "Enfin, l'utilisateur pourra sélectionner une catégorie",
                    "avec le chiffre qui lui sera associé."]
                },
            "produit" : {
                "text_header" : [
                    "Choisi parmi les produits :"
                ],
                "list_item" : [
                    data, 
                    self.start_list_item, 
                    self.end_list_item],                
                }
            }        