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
        PRIMARY KEY (id_category),
        UNIQUE INDEX (name_category)
        )
        ENGINE=InnoDB;"""
        
        self.cursor.execute(querry)
        
        querry = """CREATE TABLE IF NOT EXISTS Products (
        id_aliment SMALLINT AUTO_INCREMENT NOT NULL,
        name_aliment VARCHAR(150) NOT NULL,
        category VARCHAR(150) NOT NULL,
        store TEXT,
        nutrition_grade TEXT NOT NULL,
        trace TEXT,
        allergens TEXT,
        url TEXT,
        )
        ENGINE = InnoDB;"""
        
        self.cursor.execute(querry)
        
        
        
        c.execute('create table comptes (id INTEGER PRIMARY KEY,pseudo VARCHAR(50), credit INTEGER)[ENGINE = INNODB]')
        # Inserer deux lignes de données
        c.execute('insert into comptes values (1,"Adam","1000")')
        c.execute('insert into comptes values (2,"Billy","250")')
        c.execute('insert into comptes values (3,"Charly","125")')
        
        self.conn.commit()
    
        # Fermer le curseur
        c.close()
        
        
        
