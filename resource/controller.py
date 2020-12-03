#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.openfoodfact_query
import resource.view
import resource.constant as constant
import resource.database

import sys


class Controller:

    def __init__(self):

        self.api_query = resource.openfoodfact_query.OpenFoodFactQuery()
        self.database = resource.database.Database()

        commande = False
        for i in sys.argv:
            if i == "-up":
                print("update")
                data = self.api_query.get_category()
                self.database.save_category(data)
            if i == "-terminal":
                print("prog en ligne de commande")
                commande = True
                self.view = resource.view.View("command")

        if not commande:
            print("prog en interface graphique")
            self.view = resource.view.View("graphic")

        self.running = True

        self.page = 1
        self.table = constant.HOME
        self.start_list_item = 0
        self.end_list_item = 20

    def control(self):

        while self.running:

            if self.table == constant.HOME:

                choice = self.view.display(
                    constant.state[self.table]
                )
                if choice == constant.CHOICE_1:
                    self.table = constant.CATEGORY_LIST

                elif choice == constant.CHOICE_2:
                    self.table = constant.SUBSTITUT
                    self.list_substitut = self.database.show_substitut(
                        self.start_list_item,
                        self.end_list_item
                    )
                elif choice == constant.CHOICE_QUIT:
                    self.running = False

            if self.table == constant.CATEGORY_LIST:
                data = {
                    "list_item_category": self.database.show_category(
                        self.start_list_item, self.end_list_item)
                }
                dic_text = constant.state[self.table](data)
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
                elif choice is not None:
                    if choice.isdigit():
                        choice = int(choice)
                        if self.start_list_item <= choice \
                                <= self.end_list_item:
                            self.category_select_name = \
                                self.database.show_category(
                                    int(choice), int(choice)
                                )[0][1]
                            self.category_select_id = int(choice)
                            self.database.save_products(
                                self.api_query.product_requets_by_category(
                                    self.category_select_name,
                                    self.page
                                )
                            )
                            self.start_list_item = 0
                            self.end_list_item = 20
                            self.table = constant.PRODUIT_LIST
                            self.list_products = self.database.show_products(
                                self.category_select_id,
                                self.start_list_item,
                                self.end_list_item,
                                "SHORT"
                            )
                    else:
                        print("mauvaise commande")

            if self.table == constant.PRODUIT_LIST:
                data = {
                    "list_item_products": self.list_products,
                    "text_header": self.category_select_name
                }
                dic_text = constant.state[self.table](data)
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
                            self.category_select_name,
                            self.page
                        )
                    )
                    self.list_products = self.database.show_products(
                        self.category_select_id,
                        self.start_list_item,
                        self.end_list_item,
                        "SHORT"
                    )
                elif choice == constant.CHOICE_Z:
                    self.page -= 1
                    if self.page < 1:
                        self.page = 1
                    self.end_list_item -= 20
                    if self.end_list_item < 20:
                        self.end_list_item = 20
                    self.start_list_item -= 20
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select_name,
                            self.page
                        )
                    )
                    self.list_products = self.database.show_products(
                        self.category_select_id,
                        self.start_list_item,
                        self.end_list_item,
                        "SHORT"
                    )
                elif choice is not None:
                    if choice.isdigit():
                        choice = int(choice)
                        if self.start_list_item <= choice \
                                <= self.end_list_item:
                            id = int(choice) - self.start_list_item
                            self.product_select_id = self.list_products[id][2]
                            self.start_list_item = 0
                            self.end_list_item = 10
                            self.table = constant.PRODUIT_SELEC
                            self.page = 1
                            self.product_select = \
                                self.database.show_products_for_id(
                                    self.product_select_id
                                )[0]
                            self.list_products = self.database.show_products(
                                self.category_select_id,
                                self.start_list_item,
                                self.end_list_item,
                                "FULL"
                            )
                    else:
                        print("mauvaise commande")

            if self.table == constant.PRODUIT_SELEC:
                data = {
                    "list_item_products": self.list_products,
                    "text_item_selec_name": self.product_select[1],
                    "text_item_selec_nutri-score": self.product_select[2],
                    "text_item_selec_store": self.product_select[3],
                    "text_item_selec_trace": self.product_select[4],
                    "text_item_selec_allergens": self.product_select[5],
                    "text_item_selec_url": self.product_select[6]
                }
                dic_text = constant.state[self.table](data)
                choice = self.view.display(dic_text)
                if choice == constant.CHOICE_A:
                    self.table = constant.PRODUIT_LIST
                    self.page = 1
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.list_products = self.database.show_products(
                        self.category_select_id,
                        self.start_list_item,
                        self.end_list_item,
                        "SHORT"
                    )
                elif choice == constant.CHOICE_S:
                    self.page += 1
                    self.end_list_item += 10
                    self.start_list_item += 10
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select_name,
                            self.page
                        )
                    )
                    self.list_products = self.database.show_products(
                        self.category_select_id,
                        self.start_list_item,
                        self.end_list_item,
                        "FULL"
                    )
                elif choice == constant.CHOICE_Z:
                    self.page -= 1
                    if self.page < 1:
                        self.page = 1
                    self.end_list_item -= 10
                    self.start_list_item -= 10
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select_name,
                            self.page
                        )
                    )
                    self.list_products = self.database.show_products(
                        self.category_select_id,
                        self.start_list_item,
                        self.end_list_item,
                        "FULL"
                    )
                elif choice is not None:
                    if choice.isdigit():
                        choice = int(choice)
                        if self.start_list_item <= choice \
                                <= self.end_list_item:
                            id = int(choice) - self.start_list_item
                            self.subtitut_select_id = self.list_products[id][2]
                            self.database.save_substitut(
                                self.subtitut_select_id,
                                self.product_select_id
                            )
                            self.start_list_item = 0
                            self.end_list_item = 10
                            self.table = constant.PRODUIT_LIST
                            self.page = 1
                            self.list_products = self.database.show_products(
                                self.category_select_id,
                                self.start_list_item,
                                self.end_list_item,
                                "SHORT"
                            )
                    else:
                        print("mauvaise commande")

            if self.table == constant.SUBSTITUT:
                data = {
                    "list_item_substitut": self.list_substitut
                }
                dic_text = constant.state[self.table](data)
                choice = self.view.display(dic_text)
                if choice == constant.CHOICE_A:
                    self.table = constant.HOME
                    self.start_list_item = 0
                    self.end_list_item = 20
                elif choice == constant.CHOICE_S:
                    self.end_list_item += 10
                    self.start_list_item += 10
                    self.list_substitut = self.database.show_substitut(
                        self.start_list_item,
                        self.end_list_item
                    )
                elif choice == constant.CHOICE_Z:
                    self.end_list_item -= 10
                    self.start_list_item -= 10
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.list_substitut = self.database.show_substitut(
                        self.start_list_item,
                        self.end_list_item
                    )
                elif choice is not None:
                    if choice.isdigit():
                        choice = int(choice)
                        if self.start_list_item <= choice \
                                <= self.end_list_item:
                            id = int(choice) - self.start_list_item
                            self.product_select_id = self.list_substitut[id][1]
                            self.product_select = \
                                self.database.show_products_for_id(
                                    self.product_select_id
                                )[0]
                            self.start_list_item = 0
                            self.end_list_item = 20
                            self.table = constant.SUBSTITUT_DISPLAY
                            self.list_products = \
                                self.database.show_substitut_view(
                                    self.product_select_id,
                                    self.start_list_item,
                                    self.end_list_item
                                )
                    else:
                        print("mauvaise commande")

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
                dic_text = constant.state[self.table](data)
                choice = self.view.display(dic_text)
                if choice == constant.CHOICE_A:
                    self.table = constant.SUBSTITUT
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.list_substitut = self.database.show_substitut(
                        self.start_list_item,
                        self.end_list_item
                    )
