#!/usr/bin/python3
# -*- coding: utf8 -*-

import mysql.connector

MYSQL_HOST = "localhost"
MYSQL_USER = "projet5"
MYSQL_PASSWORD = "projet5"

class Database ():
    
    def __init__(self):
        
        """Manage the database """
        
        self.database = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            )
            
        self.cursor = self.database.cursor()    
        
        querry = """CREATE DATABASE IF NOT EXISTS on_test"""   
        self.cursor.execute(querry)
        querry = """USE on_test"""
        self.cursor.execute(querry)   
        
        
        querry = """CREATE TABLE IF NOT EXISTS Category ( 
        id_category MEDIUMINT UNSIGNED AUTO_INCREMENT NOT NULL,
        name_category VARCHAR(150) NOT NULL,
        PRIMARY KEY (id_category)
        )
        ENGINE=InnoDB"""
        self.cursor.execute(querry)
        
        
        querry = """CREATE TABLE IF NOT EXISTS Products (
        id_products MEDIUMINT AUTO_INCREMENT NOT NULL,
        name_products VARCHAR(150) NOT NULL,
        category VARCHAR(250) NOT NULL,
        store TEXT,
        nutrition_grade TEXT,
        trace TEXT,
        allergens TEXT,
        url TEXT,
        PRIMARY KEY (id_products)
        )
        ENGINE=InnoDB;"""
        self.cursor.execute(querry)
        
        querry = """CREATE TABLE IF NOT EXISTS Substitut (
        id_substitut MEDIUMINT AUTO_INCREMENT NOT NULL,
        name_substitut VARCHAR(150) NOT NULL,
        PRIMARY KEY (id_substitut)
        )
        ENGINE=InnoDB;"""
        self.cursor.execute(querry)
        
    
    def save_category(self, data):
        
        for category in data:
        
            if not ":" in category["name"] and len(category["name"])<150:
                querry = """SELECT name_category 
                FROM Category 
                WHERE name_category = %s"""
                self.cursor.execute(querry, (category["name"],))
                send = self.cursor.fetchall()
                if len(send) == 0:
                    
                    querry = """INSERT INTO Category ( name_category) VALUES( %s)"""
                                                        
                    self.cursor.execute(querry,
                                        (category["name"],))     
                    
                    self.database.commit()
                
    def show_category(self, start_list_item, end_list_item):
        
        querry = """SELECT id_category, name_category 
        FROM Category 
        WHERE id_category >= %s AND id_category <= %s"""
        self.cursor.execute(querry, (start_list_item,end_list_item))        
        data = self.cursor.fetchall()  
        
        return data

    def save_products(self, data):
        
        for products in data:
            
            querry = """SELECT name_products FROM Products WHERE name_products = %s"""
            self.cursor.execute(querry, (products["product_name"],))
            data = self.cursor.fetchall()
            if not "nutrition_grade_fr" in products :
                products["nutrition_grade_fr"] = "Non applicable"
            if len(data) == 0 and len(products["categories"]) < 250:
                
                querry = """INSERT INTO Products (
                name_products,
                category,
                store,
                nutrition_grade,
                trace,
                allergens,
                url) VALUES(%s, %s, %s, %s,%s, %s, %s)"""
                                                    
                self.cursor.execute(querry,
                                    (products["product_name"],
                                     products["categories"],
                                     products["stores"],
                                     products["nutrition_grade_fr"],
                                     products["traces"],
                                     products["allergens"],
                                     products["url"]))     
                
                self.database.commit()
        
        
    def show_products(self, category):
        
        querry = """SELECT id_products, name_products, nutrition_grade 
        FROM Products 
        WHERE category LIKE %s """
        self.cursor.execute(querry, ("%"+category+"%",))        
        data = self.cursor.fetchall()  
        return data 
    