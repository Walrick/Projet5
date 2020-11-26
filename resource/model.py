#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.constant as constant

state = {
    constant.HOME: {
        "text_header": [
            "1 : Sélectionner une catégorie",
            "2 : Voir les produits substitués",
            "3 : Quitter"
        ],
        "choise_text": "Faites votre choix"
    },
        
    constant.CATEGORY_LIST: lambda data: {
        "text_header": [
            "Choisi parmi les catégories :"
            ],
        "choise_text": "Faites votre choix",
        "list_item_category": data.get("list_item_category","" ),
        "text_corp": [
            "Pour faire défiler les catégories : <s> pour avancer,"
            "<z> pour remonter ou revenir en arrière avec <a>.",
            "Pour sélectionner une catégorie, sélectionner le",
            "avec le chiffre qui lui est associé."]
    },
    constant.PRODUIT_LIST: lambda data : {
        "text_header": [
            "Catégorie sélectionner : ",
            data.get("text_header", ""),
            "Choisi parmi les produits :"
        ],
        "list_item_products": data.get("list_item_products",""),
        "choise_text": "Faites votre choix",
        "text_corp": [
            "Pour faire défiler les produits : <s> pour avancer,",
            "<z> pour remonter ou revenir en arrière avec <a>.",
            "Pour sélectionner un produit, sélectionner le",
            "avec le chiffre qui lui est associé."
        ]
    },
    constant.PRODUIT_SELEC: lambda data : {
        "text_header": [
            "Choisi parmi les produits :"
        ],
        "text_item_selec": [
            "Produit sélectionner : " + data.get("text_item_selec_name",""),
            "Nutri-score : " + data.get("text_item_selec_nutri-score",""),
            "Magasin : " + data.get("text_item_selec_store",""),
            "Trace : " + data.get("text_item_selec_trace",""),
            "Allergens : " + data.get("text_item_selec_allergens",""),
            "URL : " + data.get("text_item_selec_url","")
        ],
        "list_item_products_for_substitut": data.get("list_item_products",""),
        "choise_text": "Faites votre choix",
        "text_corp": [
            "Pour faire défiler les produits : <s> pour avancer,",
            "<z> pour remonter ou revenir en arrière avec <a>.",
            "Pour sélectionner un produit et le rentrer en substitut,",
            "sélectionner le avec le chiffre qui lui est associé."]
    },
            
    constant.SUBSTITUT: lambda data : {
        "text_header": [
            "Choisi parmi les produits pour voir leurs substituts :"
        ],
        "list_item_substitut" : data.get("list_item_substitut",""),
        "choise_text": "Faites votre choix",
        "text_corp": [
            "Pour faire défiler les produits : <s> pour avancer,",
            "<z> pour remonter ou revenir en arrière avec <a>.",
            "Pour sélectionner un produit et voir les substituts,",
            "sélectionner le avec le chiffre qui lui est associé."]
    },
    constant.SUBSTITUT_DISPLAY: lambda data : {
        "text_item_selec": [
            "Produit sélectionner : " + data.get("text_item_selec_name",""),
            "Nutri-score : " + data.get("text_item_selec_nutri-score",""),
            "Magasin : " + data.get("text_item_selec_store",""),
            "Trace : " + data.get("text_item_selec_trace",""),
            "Allergens : " + data.get("text_item_selec_allergens",""),
            "URL : " + data.get("text_item_selec_url","")
        ],
        "list_item_substitut_display": data.get("list_item_substitut_display",""),
        "choise_text": "Faites votre choix",
        "text_corp": [
            "Pour faire défiler les produits : <s> pour avancer,",
            "<z> pour remonter ou revenir en arrière avec <a>."]
    },
                    
}
        

    
