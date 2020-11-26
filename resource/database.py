#!/usr/bin/python3
# -*- coding: utf8 -*-

import mysql.connector

MYSQL_HOST = "localhost"
MYSQL_USER = "projet5"
MYSQL_PASSWORD = "projet5"


class Database:

    def __init__(self):

        """Manage the database """

        self.database = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
        )

        self.cursor = self.database.cursor()

        query = """CREATE DATABASE IF NOT EXISTS Pur_Beurre"""
        self.cursor.execute(query)
        query = """USE Pur_Beurre"""
        self.cursor.execute(query)
        query = """SET GLOBAL time_zone = '+1:00'; """
        self.cursor.execute(query)

        query = """CREATE TABLE IF NOT EXISTS Category ( 
        id_category MEDIUMINT UNSIGNED AUTO_INCREMENT,
        name_category VARCHAR(150) NOT NULL,
        PRIMARY KEY (id_category),
        INDEX ind_name_category (name_category(20))
        )
        ENGINE=InnoDB;"""
        self.cursor.execute(query)


        query = """CREATE TABLE IF NOT EXISTS Products (
        id_products MEDIUMINT UNSIGNED AUTO_INCREMENT,
        name_products VARCHAR(150) NOT NULL,
        store TEXT,
        nutrition_grade TEXT,
        trace TEXT,
        allergens TEXT,
        url TEXT,
        PRIMARY KEY (id_products),
        INDEX ind_name_products (name_products(20))
        )
        ENGINE=InnoDB;"""
        self.cursor.execute(query)

        query = """CREATE TABLE IF NOT EXISTS Category_Products ( 
                id_cat_tab MEDIUMINT UNSIGNED NOT NULL,
                id_pro_tab MEDIUMINT UNSIGNED NOT NULL,
                CONSTRAINT fk_id_category FOREIGN KEY (id_cat_tab) REFERENCES Category(id_category),
                CONSTRAINT fk_id_products FOREIGN KEY (id_pro_tab) REFERENCES Products(id_products)
                )
                ENGINE=InnoDB;"""
        self.cursor.execute(query)

        query = """CREATE TABLE IF NOT EXISTS Substitut (
        id_sub_product MEDIUMINT UNSIGNED NOT NULL,
        id_substitution_product MEDIUMINT UNSIGNED NOT NULL,
        CONSTRAINT fk_id_sub_product FOREIGN KEY (id_sub_product) REFERENCES Products(id_products),
        CONSTRAINT fk_id_substitute_product FOREIGN KEY (id_substitution_product) REFERENCES Products(id_products)
        )
        ENGINE=InnoDB;"""
        self.cursor.execute(query)

    def save_category(self, data):

        for category in data:

            if ":" not in category["name"] and len(category["name"]) < 150:
                query = """SELECT name_category 
                FROM Category 
                WHERE name_category = %s"""
                self.cursor.execute(query, (category["name"],))
                send = self.cursor.fetchall()
                if len(send) == 0:
                    query = """INSERT INTO Category ( name_category) VALUES( %s)"""

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
            # Check if products is in the table Products
            query = """SELECT name_products FROM Products WHERE name_products = %s"""
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
                    url) VALUES(%s, %s, %s, %s,%s, %s, %s)"""

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
                    query = """SELECT id_category FROM Category WHERE name_category = %s"""
                    self.cursor.execute(query, (item_cat,))
                    id_cat = self.cursor.fetchall()
                    query = """SELECT id_products FROM Products WHERE name_products = %s"""
                    self.cursor.execute(query, (products["product_name"],))
                    id_prod = self.cursor.fetchall()
                    query = """INSERT INTO Category_Products ( 
                    id_cat_tab,
                    id_pro_tab) VALUES(%s, %s)"""
                    self.cursor.execute(query,
                                        (id_cat,
                                         id_prod))

                    self.database.commit()

    def show_products(self, category):

        query = """SELECT 
            id_products,
            name_products,
            nutrition_grade,
            store,
            trace,
            allergens,
            url
            FROM Products 
            WHERE category LIKE %s """
        self.cursor.execute(query, ("%" + category + "%",))
        data = self.cursor.fetchall()
        return data

    def show_products_for_ID(self, ID):

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
        self.cursor.execute(query, (ID,))
        data = self.cursor.fetchall()
        return data

    def save_substitut(self, id_substitution_product, id_substitué_product):

        query = """
            SELECT id_substitué_product, id_substitution_product
            FROM Substitut 
            WHERE id_substitué_product = %s and id_substitution_product = %s"""
        self.cursor.execute(query, (id_substitué_product, id_substitution_product))
        data = self.cursor.fetchall()
        if len(data) == 0:
            query = """INSERT INTO Substitut (
                id_substitué_product,
                id_substitution_product
                ) 
                VALUES(%s, %s)"""

            self.cursor.execute(query,
                                (id_substitué_product,
                                 id_substitution_product))

            self.database.commit()

    def show_substitut(self):

        query = """SELECT id_substitut, id_substitué_product, id_substitution_product
            FROM Substitut 
            """
        self.cursor.execute(query, )
        data = self.cursor.fetchall()

        return data
