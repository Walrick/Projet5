#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.openfoodfact_query
import resource.model
import resource.view
import resource.constent
import resource.database

import threading

class Controller ():
    
    def __init__ (self):
        
        self.api_query = resource.openfoodfact_query.OpenFoodFactQuery()
        self.constent = resource.constent.Constent()
        self.view = resource.view.View()
        self.database = resource.database.Database()
        
    #    data = self.api_query.get_category()
     #   self.database.save_category(data)
     
    #    threading.Thread(target=maj_category, args=(self.api_query,self.database)).start()
        

        
        self.running = True
        self.product_select = "defaut"
        self.category_select = "defaut"
        self.page = 1
        self.table = "home"   
        self.start_list_item = 0
        self.end_list_item = 20
        
        self.model = resource.model.Model()
        self.model.MAJ(
            {
            },                        
            self.constent)  
            
        
    def control(self):
        
        while self.running :
        
            if self.table == self.constent.home:
                
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )
                if CHOISE == self.constent.choice_1:
                    self.table = self.constent.category_list
                    self.model.MAJ(
                        {
                            "list_item_category" : self.database.show_category(self.start_list_item, self.end_list_item)
                        },                        
                        self.constent)                      
                if CHOISE == self.constent.choice_2:
                    self.table = self.constent.substitut 
                    self.dic_substitut = build_dic_substitut(self.database.show_substitut(),self.database)
                    self.list_substitut = list_substitut(self.dic_substitut,self.start_list_item,self.end_list_item)
                        
                    self.model.MAJ(
                        {
                            "list_item_substitut" : self.list_substitut
                        },                        
                        self.constent)                    
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
                    self.model.MAJ(
                        {
                        },                        
                        self.constent)            
                elif CHOISE == self.constent.choice_s:
                    self.start_list_item += 20
                    self.end_list_item += 20
                    self.model.MAJ(
                        {
                            "list_item_category" : self.database.show_category(self.start_list_item, self.end_list_item)
                        },
                        self.constent)             
                elif CHOISE == self.constent.choice_z :
                    self.start_list_item -= 20
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.end_list_item -= 20
                    if self.end_list_item < 20:
                        self.end_list_item = 20
                    self.model.MAJ(
                        {
                            "list_item_category" : self.database.show_category(self.start_list_item, self.end_list_item)
                        },
                        self.constent) 
                else :
                    self.category_select = self.database.show_category(int(CHOISE), int(CHOISE))[0][1]
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.table = self.constent.produit_list
                    self.list_products = build_list_products(self.database.show_products(self.category_select), self.start_list_item, self.end_list_item)
                    self.model.MAJ(
                        {
                            "list_item_products": self.list_products,
                            "text_header" : self.category_select
                        },                        
                        self.constent)                   

            if self.table == self.constent.produit_list:
                
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )
                if CHOISE == self.constent.choice_a :
                    self.table = self.constent.category_list
                    self.page = 1
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.model.MAJ(
                        {
                            "list_item_category" : self.database.show_category(self.start_list_item, self.end_list_item)
                        },
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
                        {
                            "list_item_products": self.list_products,
                            "text_header" : self.category_select
                        },  
                        self.constent)  
                elif CHOISE == self.constent.choice_z :
                    self.page -= 1
                    if self.page < 1:
                        self.page = 1
                    self.end_list_item -= 20                    
                    self.start_list_item -= 20
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.list_products = build_list_products(self.database.show_products(self.category_select), self.start_list_item, self.end_list_item)
                    self.model.MAJ(
                        {
                            "list_item_products": self.list_products,
                            "text_header" : self.category_select
                        },  
                        self.constent) 
                else :
                    self.product_select = self.list_products[int(CHOISE)]
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.table = self.constent.produit_selec       
                    self.page = 1
                    self.list_products = build_list_products(self.database.show_products(self.category_select), self.start_list_item, self.end_list_item)
                    self.model.MAJ(
                        {
                            "list_item_products": self.list_products,
                            "text_item_selec_name" : self.product_select[1],
                            "text_item_selec_nutri-score" : self.product_select[3],
                            "text_item_selec_store" : self.product_select[4],
                            "text_item_selec_trace" : self.product_select[5],
                            "text_item_selec_allergens" : self.product_select[6],
                            "text_item_selec_url" : self.product_select[7],
                        },                          
                        self.constent)                     
                    
            if self.table == self.constent.produit_selec:
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )
                if CHOISE == self.constent.choice_a :
                    self.table = self.constent.produit_list
                    self.page = 1
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.list_products = build_list_products(self.database.show_products(self.category_select), self.start_list_item, self.end_list_item)
                    self.model.MAJ(
                        {
                            "list_item_products": self.list_products,
                            "text_header" : self.category_select
                        },  
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
                        {
                            "list_item_products": self.list_products,
                            "text_item_selec_name" : self.product_select[1],
                            "text_item_selec_nutri-score" : self.product_select[3],
                            "text_item_selec_store" : self.product_select[4],
                            "text_item_selec_trace" : self.product_select[5],
                            "text_item_selec_allergens" : self.product_select[6],
                            "text_item_selec_url" : self.product_select[7],
                        },  
                        self.constent)  
                elif CHOISE == self.constent.choice_z :
                    self.page -= 1
                    if self.page < 1:
                        self.page = 1
                    self.end_list_item -= 20                    
                    self.start_list_item -= 20
                    if self.start_list_item < 0:
                        self.start_list_item = 0
                    self.database.save_products(
                        self.api_query.product_requets_by_category(
                            self.category_select,
                            self.page))
                    self.list_products = build_list_products(self.database.show_products(self.category_select), self.start_list_item, self.end_list_item)
                    self.model.MAJ(
                        {
                            "list_item_products": self.list_products,
                            "text_item_selec_name" : self.product_select[1],
                            "text_item_selec_nutri-score" : self.product_select[3],
                            "text_item_selec_store" : self.product_select[4],
                            "text_item_selec_trace" : self.product_select[5],
                            "text_item_selec_allergens" : self.product_select[6],
                            "text_item_selec_url" : self.product_select[7],
                        }, 
                        self.constent)   
                else :
                    self.subtitut_select = self.list_products[int(CHOISE)]
                    self.database.save_substitut(self.subtitut_select[2], self.product_select[2])
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.table = self.constent.produit_list       
                    self.page = 1
                    self.list_products = build_list_products(self.database.show_products(self.category_select), self.start_list_item, self.end_list_item)
                    self.model.MAJ(
                        {
                            "list_item_products": self.list_products,
                            "text_header" : self.category_select
                        },                          
                        self.constent)                  
            
            if self.table == self.constent.substitut:
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )    
                if CHOISE == self.constent.choice_a :
                    self.table = self.constent.home
                    self.start_list_item = 0
                    self.end_list_item = 20  
                    self.model.MAJ(
                        {
                        },                        
                        self.constent)   
                    
                elif CHOISE == self.constent.choice_s:
                    self.end_list_item += 20                   
                    self.start_list_item += 20
                    self.list_substitut = list_substitut(self.dic_substitut,self.start_list_item,self.end_list_item)
                        
                    self.model.MAJ(
                        {
                            "list_item_substitut" : self.list_substitut
                        },                        
                        self.constent)    
                elif CHOISE == self.constent.choice_z :
                    self.end_list_item -= 20                    
                    self.start_list_item -= 20
                    if self.start_list_item < 0:
                        self.start_list_item = 0  
                    self.list_substitut = list_substitut(self.dic_substitut,self.start_list_item,self.end_list_item)
                        
                    self.model.MAJ(
                        {
                            "list_item_substitut" : self.list_substitut
                        },                        
                        self.constent)  
                else :           
                    
                    self.product_select = self.database.show_products_for_ID(self.dic_substitut[int(CHOISE)]["id_products"])[0]
                    self.start_list_item = 0
                    self.end_list_item = 20
                    self.table = self.constent.substitut_display 
                    self.list_products = list_substitut_display(self.database, self.dic_substitut, int(CHOISE))
                    self.model.MAJ(
                    {
                        "list_item_substitut_display": self.list_products,
                        "text_item_selec_name" : self.product_select[1],
                        "text_item_selec_nutri-score" : self.product_select[2],
                        "text_item_selec_store" : self.product_select[3],
                        "text_item_selec_trace" : self.product_select[4],
                        "text_item_selec_allergens" : self.product_select[5],
                        "text_item_selec_url" : self.product_select[6],
                    }, 
                    self.constent)                     
                    
                
            if self.table == self.constent.substitut_display:
                CHOISE = self.view.display(
                    self.model.state[self.table]
                )                
                if CHOISE == self.constent.choice_a :
                    self.table = self.constent.substitut
                    self.start_list_item = 0
                    self.end_list_item = 20  
                    self.list_substitut = list_substitut(self.dic_substitut,self.start_list_item,self.end_list_item)
                        
                    self.model.MAJ(
                        {
                            "list_item_substitut" : self.list_substitut
                        },                        
                        self.constent)                 
    

def build_list_products(data, start_list_item, end_list_item):
    
    list_products = []
    index = start_list_item
    counter = 0
    for products in data:
        if index == counter:
            # index, name_products, id_products, nutrition_grade, store, trace, allergens, url, 
            list_products.append( [index, products[1], products[0], products[2], products[3], products[4], products[5],products[6]])
            index += 1
        if end_list_item == counter:
            break
        counter += 1
        
    if len (list_products) <20:
        print("liste incomplete")
    return list_products

def build_dic_substitut(data,database):
    
    match = False
    index = 1
    dic_substitut = {}
    for item in data:
        #item = (id_substitut, id_substitué_product, id_substitution_product)
        for key in dic_substitut.keys():
            if str(item[1]) in dic_substitut[key]["id_products"]:
                substitut = database.show_products_for_ID(item[2])[0]
                dic_substitut[key]["nbr_substitut"] += 1
                dic_substitut[key]["substitut"].append([item[2], substitut[1]])
                match = True
                
            
        if not match :
            product = database.show_products_for_ID(item[1])[0]
            substitut = database.show_products_for_ID(item[2])[0]
            dic_substitut[index] = {
                "id_products" : str(item[1]),
                "name_products" : product[1],
                "nbr_substitut" : 1,
                "substitut" : [[item[2], substitut[1]]]
            }
        match = False
            
        index += 1
    return dic_substitut
            

def list_substitut(dic_substitut,start_list_item,end_list_item):
    
    list_substitut=[]
    
    index = start_list_item+1
    for key in dic_substitut.keys():
        if index == key:
            list_substitut.append( [key, dic_substitut[key]["name_products"], dic_substitut[key]["nbr_substitut"]])
            index += 1
        if end_list_item == key:
            break
    return list_substitut

def list_substitut_display(database, dic_substitut, id_products):
    
    list_substitut_display = []
    
    for item in dic_substitut[id_products]["substitut"]:
        
        products = database.show_products_for_ID(item[0])[0]
        list_substitut_display.append([products[1],products[2], products[3], products[4], products[5],products[6]])
        
    return list_substitut_display


"""
def maj_category(api_query,database ):
    
    data = api_query.get_category()
    database.save_category(data)
    
    """
    
    
    