#!/usr/bin/python3
# -*- coding: utf8 -*-

import mysql.connector

MYSQL_HOST = "localhost"
MYSQL_USER = "projet5"
MYSQL_PASSWORD = "projet5"

class Database ():
    
    def __init__(self):
        
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
        id_category SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
        name_category VARCHAR(150) NOT NULL,
        PRIMARY KEY (id_category)
        )
        ENGINE=InnoDB"""
        self.cursor.execute(querry)
        
        
        querry = """CREATE TABLE IF NOT EXISTS Products (
        id_products MEDIUMINT AUTO_INCREMENT NOT NULL,
        name_aliment VARCHAR(150) NOT NULL,
        category VARCHAR(150) NOT NULL,
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
        
        self.cursor.close()
        
    
    def save_category(self, category):
        
        
        
        querry = """INSERT INTO users (name, age) VALUES(%s, %s)"""
                                            
        self.cursor.execute(querry,
                            category)
        
        
        

        
        
        
