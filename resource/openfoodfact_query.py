#!/usr/bin/python3
# -*- coding: utf8 -*-

import requests


class OpenFoodFactQuery:
    """ Openfoodfact query class for launch the query """
    BASE_URL = "https://fr.openfoodfacts.org/"

    def get_category(self):
        """
        Build category by query
        :return: [{"name": str, "url": str, "products": int,
         "known": int, "id": str},..]
        """

        search = {
            'countries': 'France',
            'json': 1,
        }
        send = requests.get(self.BASE_URL + "categories", params=search)
        category = send.json()

        return category["tags"]

    def product_requests_by_category(self, category, page):
        """
        Build product by query in category
        :param category: str
        :param page: int
        :return: [{"product_name": str,
                "stores": str,
                "nutrition_grade_fr": str,
                "traces: str,
                "allergens": str,
                "url": str,
                ... }..]
                Look complete documentation in OpenFooFact API
        """

        search = {
            'action': 'process',
            'tagtype_0': 'states',  # which subject is selected (states)
            'tag_contains_0': 'contains',  # contains or not
            'tag_0': "en:checked",  # parameters to choose
            'tagtype_1': 'categories',
            'tag_contains_1': 'contains',
            'tag_1': category,
            'countries': 'France',
            'json': 1,
            'page': page
        }

        send = requests.get(self.BASE_URL + "cgi/search.pl", params=search)
        products = send.json()

        return products["products"]
