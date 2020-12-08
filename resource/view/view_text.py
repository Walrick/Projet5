#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.constants as constants


class ViewText:
    """ View class to communicate with the user """

    def display(self, data):
        """Display fonction"""

        if constants.TEXT_HEADER in data:
            for text in data[constants.TEXT_HEADER]:
                print(text)

        if constants.TEXT_ITEM_SELECT in data:
            for text in data[constants.TEXT_ITEM_SELECT]:
                print(text)

        if constants.LIST_ITEM_CATEGORY in data:
            for item in data[constants.LIST_ITEM_CATEGORY]:
                print(str(item[0]) + " : " + item[1])

        if constants.LIST_ITEM_PRODUCTS in data:
            for item in data[constants.LIST_ITEM_PRODUCTS]:
                print(str(item[0]) + " : " + item[1] +
                      ", Nutri-Score : " + item[3])

        if constants.LIST_ITEM_SUBSTITUT in data:
            for item in data[constants.LIST_ITEM_SUBSTITUT]:
                print(str(item[0]) + " : " + item[2] +
                      ", nombre de substitut : " + str(item[3]))

        if constants.LIST_ITEM_PRODUCTS_FOR_SUBSTITUT in data:
            for item in data[constants.LIST_ITEM_PRODUCTS_FOR_SUBSTITUT]:
                print(str(item[0]) + " : " + item[1] +
                      ", Nutri-Score : " + item[3])
                print("Magasin : " + item[4] + ", Trace : " +
                      item[5] + ", Allergène : " + item[6])
                print("URL : " + item[7])

        if constants.LIST_ITEM_SUBSTITUT_DISPLAY in data:
            for item in data[constants.LIST_ITEM_SUBSTITUT_DISPLAY]:
                print("Produit : " + item[1] +
                      ", Nutri-Score : " + item[2])
                print("Magasin : " + item[3] + ", Trace : " +
                      item[4] + ", Allergène : " + item[5])
                print("URL : " + item[6])

        if constants.TEXT_CORP in data:
            for text in data[constants.TEXT_CORP]:
                print(text)

        if constants.CHOICE_TEXT in data:
            print(data[constants.CHOICE_TEXT])

    def input(self):

        choice = input()
        return choice
