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
        
        self.running = True
        self.product_select = "defaut"
        self.category_select = "defaut"
        self.index = 0
        self.page = 1
        self.table = "home"   
        self.start_list_item = 0
        self.end_list_item = 20
        
        self.model = resource.model.Model()
        self.model.MAJ(
            self.api_query,
            self.start_list_item,
            self.end_list_item,
            self.product_select,
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
                    self.start_list_item = 0
                    self.end_list_item = 20      
                    self.model.MAJ(self.api_query, self.start_list_item, self.end_list_item, self.product_select,
            self.constent)
                elif CHOISE == self.constent.choice_s:
                    self.start_list_item += 20
                    self.end_list_item += 20
                    self.model.MAJ(self.api_query, self.start_list_item, self.end_list_item, self.product_select,
            self.constent)
                elif CHOISE == self.constent.choice_z :
                    self.start_list_item -= 20
                    if self.start_list_item < 1:
                        self.start_list_item = 1
                    self.end_list_item -= 20
                    if self.end_list_item < 1:
                        self.end_list_item = 20
                    self.model.MAJ(self.api_query, self.start_list_item, self.end_list_item, self.product_select,
            self.constent)
                else :
                    self.end_list_item = self.api_query.product_requets_by_category(
                        int(CHOISE),self.page,self.index)
                    self.category_select = int(CHOISE)
                    self.start_list_item = 1
                    self.table = self.constent.produit_list
                    self.model.MAJ(self.api_query, self.start_list_item, self.end_list_item, self.product_select,
            self.constent)
                    
            if self.table == self.constent.produit_list:
                
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )
                if CHOISE == self.constent.choice_a :
                    self.table = self.constent.category_list
                    self.page = 1
                    self.index = 0
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.model.MAJ(self.api_query, self.start_list_item, self.end_list_item, self.product_select,
            self.constent)
                elif CHOISE == self.constent.choice_s:
                    self.index += 20
                    self.page += 1
                    self.end_list_item = self.api_query.product_requets_by_category(
                        self.category_select,self.page,self.index)                    
                    self.start_list_item += 20
                    self.model.MAJ(self.api_query, self.start_list_item, self.end_list_item, self.product_select,
            self.constent)
                elif CHOISE == self.constent.choice_z :
                    self.index -= 20
                    if self.index < 0:
                        self.index = 0
                    self.page -= 1
                    if self.page < 1:
                        self.page = 1
                    self.end_list_item = self.api_query.product_requets_by_category(
                        self.category_select,self.page,self.index)                      
                    self.start_list_item -= 20
                    if self.start_list_item < 1:
                        self.start_list_item = 1
                    self.model.MAJ(self.api_query, self.start_list_item, self.end_list_item, self.product_select,
            self.constent)
                else :
                    self.product_select = int(CHOISE)
                    self.start_list_item = 1
                    self.end_list_item = 20
                    self.table = self.constent.produit_selec       
                    self.page = 1
                    self.model.MAJ(self.api_query, self.start_list_item, self.end_list_item, self.product_select,
            self.constent)
                    
            if self.table == self.constent.produit_selec:
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )
                if CHOISE == self.constent.choice_a :
                    self.table = self.constent.produit_list
                    self.page = 1
                    self.index = 0
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.model.MAJ(self.api_query, self.start_list_item, self.end_list_item, self.product_select,
            self.constent)
    
    
    