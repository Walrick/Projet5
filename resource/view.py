#!/usr/bin/python3
# -*- coding: utf8 -*-





class View:
    """ View class to communicate with the user """

    def __init__(self, view_type):

        self.view_type = view_type




    def display(self, data):

        """Dispay fonction"""

        if self.view_type == "graphic" :

            pass



        else :

            if "text_header" in data:
                for text in data["text_header"]:
                    print(text)

            if "text_item_selec" in data:
                for text in data["text_item_selec"]:
                    print(text)

            if "list_item_category" in data:
                for item in data["list_item_category"]:
                    print(str(item[0]) + " : " + item[1])

            if "list_item_products" in data:
                for item in data["list_item_products"]:
                    print(str(item[0]) + " : " + item[1] + ", Nutri-Score : " + item[3])

            if "list_item_substitut" in data:
                for item in data["list_item_substitut"]:
                    print(str(item[0]) + " : " + item[2] + ", nombre de substitut : " + str(item[3]))

            if "list_item_products_for_substitut" in data:
                for item in data["list_item_products_for_substitut"]:
                    print(str(item[0]) + " : " + item[1] + ", Nutri-Score : " + item[3])
                    print("Magasin : " + item[4] + ", Trace : " + item[5] + ", Allergène : " + item[6])
                    print("URL : " + item[7])

            if "list_item_substitut_display" in data:
                for item in data["list_item_substitut_display"]:
                    print("Produit : " + item[1] + ", Nutri-Score : " + item[2])
                    print("Magasin : " + item[3] + ", Trace : " + item[4] + ", Allergène : " + item[5])
                    print("URL : " + item[6])

            if "text_corp" in data:
                for text in data["text_corp"]:
                    print(text)

            if "choise_text" in data:
                print(data["choise_text"])
                choice = input()
                return choice


