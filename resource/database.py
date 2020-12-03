#!/usr/bin/python3
# -*- coding: utf8 -*-

import mysql.connector
import os


class Database:
    def __init__(self):

        """Manage the database """

        # Get variable for connect in the database
        MYSQL_HOST = os.environ.get('MYSQL_HOST')
        MYSQL_USER = os.environ.get('MYSQL_USER')
        MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')

        # Connect database
        self.database = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
        )

        # Set cursor
        self.cursor = self.database.cursor()

        # Execute command in data.sql
    #    query = """SOURCE C:\users\jerem\documents\projet_openclassroom\projet_5\programme\resource\init.sql;"""
        sql = open("resource/init.sql").read()
        sql_parts = sql.split(";")
        for query in sql_parts:
            self.cursor.execute(query)

    def save_category(self, data):

        for category in data:
            # Check if the category is good
            if ":" not in category["name"] and len(category["name"]) < 150:
                query = """SELECT name_category
                FROM Category
                WHERE name_category = %s"""
                self.cursor.execute(query, (category["name"],))
                send = self.cursor.fetchall()
                # check if the category already exists
                if len(send) == 0:
                    query = """
                    INSERT INTO Category ( name_category) VALUES( %s)"""

                    self.cursor.execute(query,
                                        (category["name"],))

                    self.database.commit()

    def show_category(self, start_list_item, end_list_item):

        query = """SELECT id_category, name_category
        FROM Category
        WHERE id_category >= %s AND id_category <= %s"""
        self.cursor.execute(query, (start_list_item, end_list_item))
        data = self.cursor.fetchall()

        return data

    def save_products(self, data):

        for products in data:
            # Check if products already exists
            query = """
            SELECT name_products FROM Products WHERE name_products = %s"""
            self.cursor.execute(query, (products["product_name"],))
            data = self.cursor.fetchall()
            if "nutrition_grade_fr" not in products:
                products["nutrition_grade_fr"] = "Non applicable"
            if len(data) == 0 and len(products["categories"]) < 250:
                # fill the table Products
                query = """INSERT INTO Products (
                    name_products,
                    store,
                    nutrition_grade,
                    trace,
                    allergens,
                    url) VALUES(%s, %s, %s, %s,%s, %s)"""

                self.cursor.execute(query,
                                    (products["product_name"],
                                     products["stores"],
                                     products["nutrition_grade_fr"],
                                     products["traces"],
                                     products["allergens"],
                                     products["url"]))

                self.database.commit()

                # fill the table Category_Products
                categories = products["categories"].split(",")
                for item_cat in categories:
                    if item_cat[0] == " ":
                        item = list(item_cat)
                        del item[0]
                        item_cat = "".join(item)

                    query = """
                        SELECT id_category
                        FROM Category
                        WHERE name_category LIKE %s"""
                    self.cursor.execute(query, (item_cat,))
                    id_ca = self.cursor.fetchall()
                    if len(id_ca) > 0:
                        id_cat = id_ca[0][0]
                    else:
                        id_cat = 0

                    query = """
                        SELECT id_products
                        FROM Products
                        WHERE name_products LIKE %s"""
                    self.cursor.execute(query, (products["product_name"],))
                    id_pro = self.cursor.fetchall()
                    if len(id_pro) > 0:
                        id_prod = id_pro[0][0]
                    else:
                        id_prod = 0

                    if id_cat > 0 and id_prod > 0:
                        query = """INSERT INTO Category_Products (
                            id_cat_tab,
                            id_pro_tab) VALUES(%s, %s)"""
                        self.cursor.execute(query,
                                            (id_cat, id_prod))

                        self.database.commit()

    def show_products(
            self,
            id_category,
            start_list_item,
            end_list_item,
            length):

        limit = end_list_item - start_list_item
        query = """select
            id_products,
            name_products,
            nutrition_grade,
            store,
            trace,
            allergens,
            url
            FROM Category_Products
            LEFT OUTER JOIN products p
                ON p.id_products = category_products.id_pro_tab
            WHERE id_cat_tab = %s
            LIMIT %s
            OFFSET %s"""
        self.cursor.execute(query, (id_category, limit, start_list_item))
        data = self.cursor.fetchall()

        # Add a index for display
        list_products = []
        index = start_list_item
        if length == "SHORT":
            for i, products in enumerate(data):
                # index, name_products, id_products, nutrition_grade
                list_products.append(
                    [i + start_list_item,
                     products[1],
                     products[0],
                     products[2]])

        if length == "FULL":
            for products in data:
                list_products.append(
                    [index,  # index
                     products[1],  # name_products
                     products[0],  # id_products
                     products[2],  # nutrition_grade
                     products[3],  # store
                     products[4],  # trace
                     products[5],  # allergens
                     products[6]])  # url
                index += 1

        return list_products

    def show_products_for_id(self, id_prod):

        query = """SELECT
            id_products,
            name_products,
            nutrition_grade,
            store,
            trace,
            allergens,
            url
            FROM Products
            WHERE id_products = %s """
        self.cursor.execute(query, (id_prod,))
        data = self.cursor.fetchall()
        return data

    def save_substitut(self, id_substitution_product, id_product):

        query = """
            SELECT id_sub_product, id_substitution_product
            FROM Substitut
            WHERE id_sub_product = %s and id_substitution_product = %s"""
        self.cursor.execute(query, (id_product, id_substitution_product))
        data = self.cursor.fetchall()
        if len(data) == 0:
            query = """INSERT INTO Substitut (
                id_sub_product,
                id_substitution_product
                )
                VALUES(%s, %s)"""

            self.cursor.execute(query,
                                (id_product,
                                 id_substitution_product))

            self.database.commit()

    def show_substitut(self, start_list_item, end_list_item):
        limit = end_list_item - start_list_item

        query = """
            SELECT
            id_products,
            name_products,
            COUNT(id_products)
            FROM substitut
            LEFT JOIN products p
                ON p.id_products = substitut.id_sub_product
            GROUP BY id_products
            LIMIT %s
            OFFSET %s"""
        self.cursor.execute(query, (limit, start_list_item))
        data = self.cursor.fetchall()

        # Add a index for display
        list_products = []
        index = start_list_item
        for item in data:
            # index, id_products, name_products, COUNT(id_products)
            list_products.append(
                [index, item[0], item[1], item[2]])
            index += 1

        return list_products

    def show_substitut_view(self, product_id, start_list_item, end_list_item):
        limit = end_list_item - start_list_item

        query = """
            SELECT
                id_products,
                name_products,
                nutrition_grade,
                store,
                trace,
                allergens,
                url
            FROM substitut
            LEFT JOIN products p
                on p.id_products = substitut.id_substitution_product
            WHERE id_sub_product = %s
            LIMIT %s
            OFFSET %s"""
        self.cursor.execute(query, (product_id, limit, start_list_item))
        data = self.cursor.fetchall()
        return data
