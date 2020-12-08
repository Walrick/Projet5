#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.openfoodfact_query as openfoodfact_query
import resource.view.view_graphic as view_graphic
import resource.view.view_text as view_text
import resource.constants as constants
import resource.database as database


class Controller:

    def __init__(self, arg):

        self.api_query = openfoodfact_query.OpenFoodFactQuery()
        self.database = database.Database()

        commande = False
        for i in arg:
            if i == "-u" or i == "--update":
                print("update in progress")
                data = self.api_query.get_category()
                self.database.save_category(data)
                print("end of update")
            if i == "-t" or i == "--terminal":
                print("command line program")
                commande = True
                self.view = view_text.ViewText()

        if not commande:
            print("GUI program")
            self.view = view_graphic.ViewGraphic()

        # Init attribute
        self.running = True
        self.page = 1
        self.table = constants.HOME
        self.start_list_item = 0
        self.end_list_item = 20
        self.category_select_name = None
        self.category_select_id = None
        self.substitute_select_id = None
        self.product_select_id = None
        self.list_substitut = None
        self.product_select = None
        self.list_products = None

    def control(self):

        while self.running:

            if self.table == constants.HOME:

                self.view.display(constants.STATE[self.table])
                choice = self.view.input()
                if choice == constants.CHOICE_1:
                    self.table = constants.CATEGORY_LIST

                elif choice == constants.CHOICE_2:
                    self.table = constants.SUBSTITUT
                    self.list_substitut = self.database.get_substitut(
                        self.start_list_item,
                        self.end_list_item
                    )
                elif choice == constants.CHOICE_QUIT:
                    self.running = False

            if self.table == constants.CATEGORY_LIST:
                data = {
                    constants.LIST_ITEM_CATEGORY: self.database.get_category(
                        self.start_list_item, self.end_list_item)
                }
                dic_text = constants.STATE[self.table](data)
                self.view.display(dic_text)
                choice = self.view.input()

                if choice == constants.CHOICE_A:
                    self.table = constants.HOME
                    self.start_list_item = 0
                    self.end_list_item = 20
                elif choice == constants.CHOICE_S:
                    self.start_list_item += 20
                    self.end_list_item += 20
                elif choice == constants.CHOICE_Z:
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
                                self.database.get_category(
                                    int(choice), int(choice)
                                )[0][1]
                            self.category_select_id = int(choice)
                            self.database.save_products(
                                self.api_query.product_requests_by_category(
                                    self.category_select_name,
                                    self.page
                                )
                            )
                            self.start_list_item = 0
                            self.end_list_item = 20
                            self.table = constants.PRODUIT_LIST
                            self.list_products = self.database.get_products(
                                self.category_select_id,
                                self.start_list_item,
                                self.end_list_item,
                                "SHORT"
                            )
                    else:
                        print("mauvaise commande")

            if self.table == constants.PRODUIT_LIST:
                data = {
                    constants.LIST_ITEM_PRODUCTS: self.list_products,
                    constants.TEXT_HEADER: self.category_select_name
                }
                dic_text = constants.STATE[self.table](data)
                self.view.display(dic_text)
                choice = self.view.input()

                if choice == constants.CHOICE_A:
                    self.table = constants.CATEGORY_LIST
                    self.page = 1
                    self.start_list_item = 0
                    self.end_list_item = 20
                elif choice == constants.CHOICE_S:
                    self.page += 1
                    self.end_list_item += 20
                    self.start_list_item += 20
                    self.database.save_products(
                        self.api_query.product_requests_by_category(
                            self.category_select_name,
                            self.page
                        )
                    )
                    self.list_products = self.database.get_products(
                        self.category_select_id,
                        self.start_list_item,
                        self.end_list_item,
                        "SHORT"
                    )
                elif choice == constants.CHOICE_Z:
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
                        self.api_query.product_requests_by_category(
                            self.category_select_name,
                            self.page
                        )
                    )
                    self.list_products = self.database.get_products(
                        self.category_select_id,
                        self.start_list_item,
                        self.end_list_item,
                        "SHORT"
                    )
                elif choice is not None:
                    if choice.isdigit():
                        choice = int(choice)
                        if self.start_list_item <= choice \
                                <= len(self.list_products)-1:
                            id_choice = int(choice) - self.start_list_item
                            self.product_select_id = \
                                self.list_products[id_choice][2]
                            self.start_list_item = 0
                            self.end_list_item = 10
                            self.table = constants.PRODUIT_SELECT
                            self.page = 1
                            self.product_select = \
                                self.database.get_products_for_id(
                                    self.product_select_id
                                )[0]
                            self.list_products = self.database.get_products(
                                self.category_select_id,
                                self.start_list_item,
                                self.end_list_item,
                                "FULL"
                            )
                    else:
                        print("mauvaise commande")

            if self.table == constants.PRODUIT_SELECT:
                data = {
                    constants.LIST_ITEM_PRODUCTS:
                        self.list_products,
                    constants.TEXT_ITEM_SELECT_NAME:
                        self.product_select[1],
                    constants.TEXT_ITEM_SELECT_NUTRI_SCORE:
                        self.product_select[2],
                    constants.TEXT_ITEM_SELECT_STORE:
                        self.product_select[3],
                    constants.TEXT_ITEM_SELECT_TRACE:
                        self.product_select[4],
                    constants.TEXT_ITEM_SELECT_ALLERGENS:
                        self.product_select[5],
                    constants.TEXT_ITEM_SELECT_URL:
                        self.product_select[6]
                }
                dic_text = constants.STATE[self.table](data)
                self.view.display(dic_text)
                choice = self.view.input()

                if choice == constants.CHOICE_A:
                    self.table = constants.PRODUIT_LIST
                    self.page = 1
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.list_products = self.database.get_products(
                        self.category_select_id,
                        self.start_list_item,
                        self.end_list_item,
                        "SHORT"
                    )
                elif choice == constants.CHOICE_S:
                    self.page += 1
                    self.end_list_item += 10
                    self.start_list_item += 10
                    self.database.save_products(
                        self.api_query.product_requests_by_category(
                            self.category_select_name,
                            self.page
                        )
                    )
                    self.list_products = self.database.get_products(
                        self.category_select_id,
                        self.start_list_item,
                        self.end_list_item,
                        "FULL"
                    )
                elif choice == constants.CHOICE_Z:
                    self.page -= 1
                    if self.page < 1:
                        self.page = 1
                    self.end_list_item -= 10
                    self.start_list_item -= 10
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.database.save_products(
                        self.api_query.product_requests_by_category(
                            self.category_select_name,
                            self.page
                        )
                    )
                    self.list_products = self.database.get_products(
                        self.category_select_id,
                        self.start_list_item,
                        self.end_list_item,
                        "FULL"
                    )
                elif choice is not None:
                    if choice.isdigit():
                        choice = int(choice)
                        if self.start_list_item <= choice \
                                <= len(self.list_products)-1:
                            id_choice = int(choice) - self.start_list_item
                            self.substitute_select_id = \
                                self.list_products[id_choice][2]
                            self.database.save_substitut(
                                self.substitute_select_id,
                                self.product_select_id
                            )
                            self.start_list_item = 0
                            self.end_list_item = 10
                            self.table = constants.PRODUIT_LIST
                            self.page = 1
                            self.list_products = self.database.get_products(
                                self.category_select_id,
                                self.start_list_item,
                                self.end_list_item,
                                "SHORT"
                            )
                    else:
                        print("mauvaise commande")

            if self.table == constants.SUBSTITUT:
                data = {
                    constants.LIST_ITEM_SUBSTITUT: self.list_substitut
                }
                dic_text = constants.STATE[self.table](data)
                self.view.display(dic_text)
                choice = self.view.input()

                if choice == constants.CHOICE_A:
                    self.table = constants.HOME
                    self.start_list_item = 0
                    self.end_list_item = 20
                elif choice == constants.CHOICE_S:
                    self.end_list_item += 10
                    self.start_list_item += 10
                    self.list_substitut = self.database.get_substitut(
                        self.start_list_item,
                        self.end_list_item
                    )
                elif choice == constants.CHOICE_Z:
                    self.end_list_item -= 10
                    self.start_list_item -= 10
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.list_substitut = self.database.get_substitut(
                        self.start_list_item,
                        self.end_list_item
                    )
                elif choice is not None:
                    if choice.isdigit():
                        choice = int(choice)
                        if self.start_list_item <= choice \
                                <= len(self.list_substitut)-1:
                            id_choice = int(choice) - self.start_list_item
                            self.product_select_id = \
                                self.list_substitut[id_choice][1]
                            self.product_select = \
                                self.database.get_products_for_id(
                                    self.product_select_id
                                )[0]
                            self.start_list_item = 0
                            self.end_list_item = 20
                            self.table = constants.SUBSTITUT_DISPLAY
                            self.list_products = \
                                self.database.get_substitut_view(
                                    self.product_select_id,
                                    self.start_list_item,
                                    self.end_list_item
                                )
                    else:
                        print("mauvaise commande")

            if self.table == constants.SUBSTITUT_DISPLAY:
                data = {
                    constants.LIST_ITEM_SUBSTITUT_DISPLAY:
                        self.list_products,
                    constants.TEXT_ITEM_SELECT_NAME:
                        self.product_select[1],
                    constants.TEXT_ITEM_SELECT_NUTRI_SCORE:
                        self.product_select[2],
                    constants.TEXT_ITEM_SELECT_STORE:
                        self.product_select[3],
                    constants.TEXT_ITEM_SELECT_TRACE:
                        self.product_select[4],
                    constants.TEXT_ITEM_SELECT_ALLERGENS:
                        self.product_select[5],
                    constants.TEXT_ITEM_SELECT_URL:
                        self.product_select[6]
                }
                dic_text = constants.STATE[self.table](data)
                self.view.display(dic_text)
                choice = self.view.input()

                if choice == constants.CHOICE_A:
                    self.table = constants.SUBSTITUT
                    self.start_list_item = 0
                    self.end_list_item = 10
                    self.list_substitut = self.database.get_substitut(
                        self.start_list_item,
                        self.end_list_item
                    )
