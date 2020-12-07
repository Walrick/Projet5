#!/usr/bin/python3
# -*- coding: utf8 -*-

CHOICE_1 = "1"
CHOICE_2 = "2"
CHOICE_QUIT = "3"
CHOICE_A = "a"
CHOICE_Z = "z"
CHOICE_S = "s"

HOME = "HOME"
CATEGORY_LIST = "CATEGORY_LIST"
SUBSTITUT = "SUBSTITUT"
PRODUIT_LIST = "PRODUIT_LIST"
PRODUIT_SELECT = "PRODUIT_SELECT"
SUBSTITUT_DISPLAY = "SUBSTITUT_DISPLAY"

TEXT_HEADER = "text_header"
CHOICE_TEXT = "choice_text"
LIST_ITEM_CATEGORY = "list_item_category"
TEXT_CORP = "text_corp"
LIST_ITEM_PRODUCTS = "list_item_products"
TEXT_ITEM_SELECT = "text_item_select"
LIST_ITEM_PRODUCTS_FOR_SUBSTITUT = "list_item_products_for_substitut"
LIST_ITEM_SUBSTITUT_DISPLAY = "list_item_substitut_display"
LIST_ITEM_SUBSTITUT = "list_item_substitut"
TEXT_ITEM_SELECT_NAME = "text_item_select_name"
TEXT_ITEM_SELECT_NUTRI_SCORE = "text_item_select_nutri-score"
TEXT_ITEM_SELECT_STORE = "text_item_select_store"
TEXT_ITEM_SELECT_TRACE = "text_item_select_trace"
TEXT_ITEM_SELECT_ALLERGENS = "text_item_select_allergens"
TEXT_ITEM_SELECT_URL = "text_item_select_url"

STATE = {
    HOME: {
        TEXT_HEADER: [
            "1 : Sélectionner une catégorie",
            "2 : Voir les produits substitués",
            "3 : Quitter"
        ],
        CHOICE_TEXT: "Faites votre choix"
    },

    CATEGORY_LIST: lambda data: {
        TEXT_HEADER: [
            "Choisi parmi les catégories :"
        ],
        CHOICE_TEXT: "Faites votre choix",
        LIST_ITEM_CATEGORY: data.get(LIST_ITEM_CATEGORY, []),
        TEXT_CORP: [
            "Pour faire défiler les catégories : <s> pour avancer,"
            "<z> pour remonter ou revenir en arrière avec <a>.",
            "Pour voir une catégorie, sélectionner la",
            "avec le chiffre qui lui est associé."]
    },
    PRODUIT_LIST: lambda data: {
        TEXT_HEADER: [
            "Catégorie sélectionner : ",
            data.get(TEXT_HEADER, []),
            "Choisi parmi les produits :"
        ],
        LIST_ITEM_PRODUCTS: data.get(LIST_ITEM_PRODUCTS, []),
        CHOICE_TEXT: "Faites votre choix",
        TEXT_CORP: [
            "Pour faire défiler les produits : <s> pour avancer,",
            "<z> pour remonter ou revenir en arrière avec <a>.",
            "Pour voir un produit, sélectionner le",
            "avec le chiffre qui lui est associé."
        ]
    },
    PRODUIT_SELECT: lambda data: {
        TEXT_HEADER: [
            "Choisi parmi les produits :"
        ],
        TEXT_ITEM_SELECT: [
            "Produit sélectionner : " + data.get(TEXT_ITEM_SELECT_NAME, []),
            "Nutri-score : " + data.get(TEXT_ITEM_SELECT_NUTRI_SCORE, []),
            "Magasin : " + data.get(TEXT_ITEM_SELECT_STORE, []),
            "Trace : " + data.get(TEXT_ITEM_SELECT_TRACE, []),
            "Allergens : " + data.get(TEXT_ITEM_SELECT_ALLERGENS, []),
            "URL : " + data.get(TEXT_ITEM_SELECT_URL, [])
        ],
        LIST_ITEM_PRODUCTS_FOR_SUBSTITUT: data.get(LIST_ITEM_PRODUCTS, []),
        CHOICE_TEXT: "Faites votre choix",
        TEXT_CORP: [
            "Pour faire défiler les produits : <s> pour avancer,",
            "<z> pour remonter ou revenir en arrière avec <a>.",
            "Pour voir un produit et le rentrer en substitut,",
            "sélectionner le avec le chiffre qui lui est associé."]
    },

    SUBSTITUT: lambda data: {
        TEXT_HEADER: [
            "Choisi parmi les produits pour voir leurs substituts :"
        ],
        LIST_ITEM_SUBSTITUT: data.get(LIST_ITEM_SUBSTITUT, []),
        CHOICE_TEXT: "Faites votre choix",
        TEXT_CORP: [
            "Pour faire défiler les produits : <s> pour avancer,",
            "<z> pour remonter ou revenir en arrière avec <a>.",
            "Pour sélectionner un produit et voir les substituts,",
            "sélectionner le avec le chiffre qui lui est associé."]
    },
    SUBSTITUT_DISPLAY: lambda data: {
        TEXT_ITEM_SELECT: [
            "Produit sélectionner : " + data.get(TEXT_ITEM_SELECT_NAME, []),
            "Nutri-score : " + data.get(TEXT_ITEM_SELECT_NUTRI_SCORE, []),
            "Magasin : " + data.get(TEXT_ITEM_SELECT_STORE, []),
            "Trace : " + data.get(TEXT_ITEM_SELECT_TRACE, []),
            "Allergens : " + data.get(TEXT_ITEM_SELECT_ALLERGENS, []),
            "URL : " + data.get(TEXT_ITEM_SELECT_URL, [])
        ],
        LIST_ITEM_SUBSTITUT_DISPLAY: data.get(
            LIST_ITEM_SUBSTITUT_DISPLAY, []),
        CHOICE_TEXT: "Faites votre choix",
        TEXT_CORP: [
            "<a> pour revenir en arrière."]
    },
}
