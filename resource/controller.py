#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.openfoodfact_query
import resource.model
import resource.view
import resource.constent
import resource.database


class Controller ():
    
    def __init__ (self):
        
        self.api_query = resource.openfoodfact_query.OpenfoodfactQuery()
        self.constent = resource.constent.Constent()
        self.view = resource.view.View()
        self.database = resource.database.Database()
        
        data = self.api_query.get_category()
        
        self.database.save_category(data)

        
        self.running = True
        self.product_select = "defaut"
        self.category_select = "defaut"
        self.index = 0
        self.page = 1
        self.table = "home"   
        self.start_list_item = 1
        self.end_list_item = 20
        
        self.model = resource.model.Model()
        self.model.MAJ(
            self.database.show_category(self.start_list_item, self.end_list_item),
            self.constent)
            
        
    def control(self):
        
        while self.running :
        
            if self.table == self.constent.home:
                
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )
                if CHOISE == self.constent.choice_1:
                    self.table = self.constent.category_list
                if CHOISE == self.constent.choice_2:
                    self.table = self.constent.substitut        
                if CHOISE == self.constent.choice_quit:
                    self.running = False
                    
            if self.table == self.constent.category_list : 
                
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )
                if CHOISE == self.constent.choice_a :
                    self.table = self.constent.home
                    self.start_list_item = 1
                    self.end_list_item = 20  
                    self.model.MAJ(
                        self.database.show_category(self.start_list_item, self.end_list_item),
                        self.constent)            
                elif CHOISE == self.constent.choice_s:
                    self.start_list_item += 20
                    self.end_list_item += 20
                    self.model.MAJ(
                        self.database.show_category(self.start_list_item, self.end_list_item),
                        self.constent)             
                elif CHOISE == self.constent.choice_z :
                    self.start_list_item -= 20
                    if self.start_list_item < 1:
                        self.start_list_item = 1
                    self.end_list_item -= 20
                    if self.end_list_item < 20:
                        self.end_list_item = 20
                    self.model.MAJ(
                        self.database.show_category(self.start_list_item, self.end_list_item),
                        self.constent) 
                else :
                    self.category_select = self.database.show_category(int(CHOISE), int(CHOISE))[0][1]
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.start_list_item = 1
                    self.end_list_item = 20
                    self.table = self.constent.produit_list
                    self.list_products = build_list_products(self.database.show_products(self.category_select), self.start_list_item, self.end_list_item)
                    self.model.MAJ(
                        self.list_products,
                        self.constent)                   

            if self.table == self.constent.produit_list:
                
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )
                if CHOISE == self.constent.choice_a :
                    self.table = self.constent.category_list
                    self.page = 1
                    self.start_list_item = 1
                    self.end_list_item = 20
                    self.model.MAJ(
                        self.database.show_category(self.start_list_item, self.end_list_item),
                        self.constent) 
                elif CHOISE == self.constent.choice_s:
                    self.page += 1
                    self.end_list_item += 20                   
                    self.start_list_item += 20
                    
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.list_products = build_list_products(self.database.show_products(self.category_select), self.start_list_item, self.end_list_item)
                    self.model.MAJ(
                        self.list_products,
                        self.constent)  
                elif CHOISE == self.constent.choice_z :
                    self.page -= 1
                    if self.page < 1:
                        self.page = 1
                    self.end_list_item -= 20                    
                    self.start_list_item -= 20
                    if self.start_list_item < 1:
                        self.start_list_item = 1
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.list_products = build_list_products(self.database.show_products(self.category_select), self.start_list_item, self.end_list_item)
                    self.model.MAJ(
                        self.list_products,
                        self.constent) 
                else :
                    self.product_select = self.list_products[int(CHOISE)][1]
                    self.start_list_item = 1
                    self.end_list_item = 20
                    self.table = self.constent.produit_selec       
                    self.page = 1

                    self.list_products = build_list_products(self.database.show_products(self.category_select), self.start_list_item, self.end_list_item)
                    self.model.MAJ(
                        self.list_products,
                        self.constent)                     
                    
            if self.table == self.constent.produit_selec:
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )
                if CHOISE == self.constent.choice_a :
                    self.table = self.constent.produit_list
                    self.page = 1
                    self.index = 0
                    self.start_list_item = 1
                    self.end_list_item = 20
                    self.model.MAJ(self.api_query, self.start_list_item, self.end_list_item, self.product_select,
            self.constent)
    

def build_list_products(data, start_list_item, end_list_item):
    
    list_products = []
    index = start_list_item
    counter = 1
    for products in data:
        if index == counter:
            list_products.append( [index, products[1], products[0]])
            index += 1
        counter += 1
        if end_list_item == counter:
            break
    if len (list_products) <19:
        print("liste incomplete")
    return list_products


    
    
    
    