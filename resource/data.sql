/* create database */
CREATE DATABASE IF NOT EXISTS Pur_Beurre;

/* Select database */
USE Pur_Beurre ;

/* Set timezone */
SET GLOBAL time_zone = '+1:00';

/* Create TABLE Category */
CREATE TABLE IF NOT EXISTS Category (
        id_category MEDIUMINT UNSIGNED AUTO_INCREMENT,
        name_category VARCHAR(150) NOT NULL,
        PRIMARY KEY (id_category),
        INDEX ind_name_category (name_category(20))
        )
        ENGINE=InnoDB;

/* Create TABLE Products */
CREATE TABLE IF NOT EXISTS Products (
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
        ENGINE=InnoDB;

/* Create TABLE Category_Products */
CREATE TABLE IF NOT EXISTS Category_Products (
        id_cat_tab MEDIUMINT UNSIGNED NOT NULL,
        id_pro_tab MEDIUMINT UNSIGNED NOT NULL,
        CONSTRAINT fk_id_category FOREIGN KEY (id_cat_tab) REFERENCES Category(id_category),
        CONSTRAINT fk_id_products FOREIGN KEY (id_pro_tab) REFERENCES Products(id_products)
        )
        ENGINE=InnoDB;

/* Create TABLE Substitut */
CREATE TABLE IF NOT EXISTS Substitut (
        id_sub_product MEDIUMINT UNSIGNED NOT NULL,
        id_substitution_product MEDIUMINT UNSIGNED NOT NULL,
        CONSTRAINT fk_id_sub_product FOREIGN KEY (id_sub_product) REFERENCES Products(id_products),
        CONSTRAINT fk_id_substitute_product FOREIGN KEY (id_substitution_product) REFERENCES Products(id_products)
        )
        ENGINE=InnoDB;