#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.openfoodfact_query
import resource.model as model
import resource.view
import resource.constant as constant
import resource.database


class Controller:

    def __init__(self):

        self.api_query = resource.openfoodfact_query.OpenFoodFactQuery()
        self.view = resource.view.View()
        self.database = resource.database.Database()

        data = self.api_query.get_category()
        self.database.save_category(data)

        self.running = True
        self.product_select = "defaults"
        self.category_select = "defaults"
        self.page = 1
        self.table = constant.HOME
        self.start_list_item = 0
        self.end_list_item = 20

    def control(self):

        while self.running:

            if self.table == constant.HOME:

                choice = self.view.display(
                    model.state[self.table]
                )
                if choice == constant.CHOICE_1:
                    self.table = constant.CATEGORY_LIST

                if choice == constant.CHOICE_2:
                    self.table = constant.SUBSTITUT
                    self.dic_substitut = build_dic_substitut(
                        self.database.show_substitut(), self.database)
                    self.list_substitut = list_substitut(
                        self.dic_substitut,
                        self.start_list_item,
                        self.end_list_item
                    )
                if choice == constant.CHOICE_QUIT:
                    self.running = False

            if self.table == constant.CATEGORY_LIST:
                data = {
                    "list_item_category": self.database.show_category(
                        self.start_list_item, self.end_list_item)
                }
                dic_text = model.state[self.table](data)
                choice = self.view.display(dic_text)
                if choice == constant.CHOICE_A:
                    self.table = constant.HOME
                    self.start_list_item = 0
                    self.end_list_item = 20
                elif choice == constant.CHOICE_S:
                    self.start_list_item += 20
                    self.end_list_item += 20
                elif choice == constant.CHOICE_Z:
                    self.start_list_item -= 20
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.end_list_item -= 20
                    if self.end_list_item < 20:
                        self.end_list_item = 20
                else:
                    self.category_select = self.database.show_category(
                        int(choice), int(choice))[0][1]
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.table = constant.PRODUIT_LIST
                    self.list_products = build_list_products(
                        self.database.show_products(self.category_select),
                        self.start_list_item, self.end_list_item)

            if self.table == constant.PRODUIT_LIST:
                data = {
                    "list_item_products": self.list_products,
                    "text_header": self.category_select
                }
                dic_text = model.state[self.table](data)
                choice = self.view.display(dic_text)
                if choice == constant.CHOICE_A:
                    self.table = constant.CATEGORY_LIST
                    self.page = 1
                    self.start_list_item = 0
                    self.end_list_item = 20
                elif choice == constant.CHOICE_S:
                    self.page += 1
                    self.end_list_item += 20
                    self.start_list_item += 20
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.list_products = build_list_products(
                        self.database.show_products(self.category_select),
                        self.start_list_item, self.end_list_item)
                elif choice == constant.CHOICE_Z:
                    self.page -= 1
                    if self.page < 1:
                        self.page = 1
                    self.end_list_item -= 20
                    self.start_list_item -= 20
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.list_products = build_list_products(
                        self.database.show_products(self.category_select),
                        self.start_list_item, self.end_list_item)
                else:
                    self.product_select = self.list_products[int(choice)]
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.table = constant.PRODUIT_SELEC
                    self.page = 1
                    self.list_products = build_list_products(
                        self.database.show_products(self.category_select),
                        self.start_list_item, self.end_list_item)

            if self.table == constant.PRODUIT_SELEC:
                data = {
                    "list_item_products": self.list_products,
                    "text_item_selec_name": self.product_select[1],
                    "text_item_selec_nutri-score": self.product_select[3],
                    "text_item_selec_store": self.product_select[4],
                    "text_item_selec_trace": self.product_select[5],
                    "text_item_selec_allergens": self.product_select[6],
                    "text_item_selec_url": self.product_select[7]
                }
                dic_text = model.state[self.table](data)
                choice = self.view.display(dic_text)
                if choice == constant.CHOICE_A:
                    self.table = constant.PRODUIT_LIST
                    self.page = 1
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.list_products = build_list_products(
                        self.database.show_products(self.category_select),
                        self.start_list_item, self.end_list_item)
                elif choice == constant.CHOICE_S:
                    self.page += 1
                    self.end_list_item += 20
                    self.start_list_item += 20

                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.list_products = build_list_products(
                        self.database.show_products(self.category_select),
                        self.start_list_item, self.end_list_item)
                elif choice == constant.CHOICE_Z:
                    self.page -= 1
                    if self.page < 1:
                        self.page = 1
                    self.end_list_item -= 20
                    self.start_list_item -= 20
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.list_products = build_list_products(
                        self.database.show_products(self.category_select),
                        self.start_list_item, self.end_list_item)
                else:
                    self.subtitut_select = self.list_products[int(choice)]
                    self.database.save_substitut(
                        self.subtitut_select[2], self.product_select[2])
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.table = constant.PRODUIT_LIST
                    self.page = 1
                    self.list_products = build_list_products(
                        self.database.show_products(self.category_select),
                        self.start_list_item, self.end_list_item)

            if self.table == constant.SUBSTITUT:
                data = {
                    "list_item_substitut": self.list_substitut
                }
                dic_text = model.state[self.table](data)
                choice = self.view.display(dic_text)
                if choice == constant.CHOICE_A:
                    self.table = constant.HOME
                    self.start_list_item = 0
                    self.end_list_item = 20
                elif choice == constant.CHOICE_S:
                    self.end_list_item += 20
                    self.start_list_item += 20
                    self.list_substitut = list_substitut(
                        self.dic_substitut,
                        self.start_list_item,
                        self.end_list_item)
                elif choice == constant.CHOICE_Z:
                    self.end_list_item -= 20
                    self.start_list_item -= 20
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.list_substitut = list_substitut(
                        self.dic_substitut,
                        self.start_list_item,
                        self.end_list_item)
                else:
                    self.product_select = self.database.show_products_for_ID(
                        self.dic_substitut[int(choice)]["id_products"])[0]
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.table = constant.SUBSTITUT_DISPLAY
                    self.list_products = list_substitut_display(self.database, self.dic_substitut, int(choice))

            if self.table == constant.SUBSTITUT_DISPLAY:
                data = {
                    "list_item_substitut_display": self.list_products,
                    "text_item_selec_name": self.product_select[1],
                    "text_item_selec_nutri-score": self.product_select[2],
                    "text_item_selec_store": self.product_select[3],
                    "text_item_selec_trace": self.product_select[4],
                    "text_item_selec_allergens": self.product_select[5],
                    "text_item_selec_url": self.product_select[6]
                }
                dic_text = model.state[self.table](data)
                choice = self.view.display(dic_text)
                if choice == constant.CHOICE_A:
                    self.table = constant.SUBSTITUT
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.list_substitut = list_substitut(
                        self.dic_substitut,
                        self.start_list_item,
                        self.end_list_item)


def build_list_products(data, start_list_item, end_list_item):
    list_products = []
    index = start_list_item
    counter = 0
    for products in data:
        if index == counter:
            # index, name_products, id_products, nutrition_grade, store, trace, allergens, url, 
            list_products.append(
                [index, products[1], products[0], products[2], products[3], products[4], products[5], products[6]])
            index += 1
        if end_list_item == counter:
            break
        counter += 1

    if len(list_products) < 20:
        print("liste incomplete")
    return list_products


def build_dic_substitut(data, database):
    match = False
    index = 1
    dic_substitut = {}
    for item in data:
        # item = (id_substitut, id_substitué_product, id_substitution_product)
        for key in dic_substitut.keys():
            if str(item[1]) in dic_substitut[key]["id_products"]:
                substitut = database.show_products_for_ID(item[2])[0]
                dic_substitut[key]["nbr_substitut"] += 1
                dic_substitut[key]["substitut"].append([item[2], substitut[1]])
                match = True

        if not match:
            product = database.show_products_for_ID(item[1])[0]
            substitut = database.show_products_for_ID(item[2])[0]
            dic_substitut[index] = {
                "id_products": str(item[1]),
                "name_products": product[1],
                "nbr_substitut": 1,
                "substitut": [[item[2], substitut[1]]]
            }
        match = False

        index += 1
    return dic_substitut


def list_substitut(dic_substitut, start_list_item, end_list_item):
    list_substitut = []

    index = start_list_item + 1
    for key in dic_substitut.keys():
        if index == key:
            list_substitut.append([key, dic_substitut[key]["name_products"], dic_substitut[key]["nbr_substitut"]])
            index += 1
        if end_list_item == key:
            break
    return list_substitut


def list_substitut_display(database, dic_substitut, id_products):
    list_substitut_display = []

    for item in dic_substitut[id_products]["substitut"]:
        products = database.show_products_for_ID(item[0])[0]
        list_substitut_display.append([products[1], products[2], products[3], products[4], products[5], products[6]])

    return list_substitut_display


"""
def maj_category(api_query,database ):
    
    data = api_query.get_category()
    database.save_category(data)
    
    """
