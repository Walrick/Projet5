#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.api_requests
import resource.interface
import resource.constent


CHOICE_1 = "1"
CHOICE_2 = "2"
CHOICE_QUIT = "3"   
CHOICE_a = "a"
CHOICE_z = "z"
CHOICE_s = "s"


class Main():
    
    def __init__(self):
        
        self.category_selec = ""
        self.index = 0
        self.page = "/1"
        self.table = "home"
        self.running = True
        self.api_requests = resource.api_requests.Api_requets()
        self.constent = resource.constent.Constent()
        self.interface = resource.interface.Interface()
        
        self.constent.build_table(self.api_requests.category)
        
    def loop_master(self):
        
        while self.running :
            
            if self.table == "home":
                CHOISE = self.interface.display(self.constent.STATE[self.table])
                if CHOISE == CHOICE_1:
                    self.table = "category"
                if CHOISE == CHOICE_2:
                    self.table = "substitut"        
                if CHOISE == CHOICE_QUIT:
                    self.running = False
                    
            if self.table == "category": 
                CHOISE = self.interface.display(self.constent.STATE[self.table])
                if CHOISE == CHOICE_a :
                    self.table = "home"
                    self.constent.start_list_item = 0
                    self.constent.end_list_item = 20                    
                elif CHOISE == CHOICE_s:
                    self.constent.start_list_item += 20
                    self.constent.end_list_item += 20
                    self.constent.build_table(self.api_requests.category)
                elif CHOISE == CHOICE_z :
                    self.constent.start_list_item -= 20
                    if self.constent.start_list_item < 1:
                        self.constent.start_list_item = 1
                    self.constent.end_list_item -= 20
                    if self.constent.end_list_item < 1:
                        self.constent.end_list_item = 20
                    self.constent.build_table(self.api_requests.category)   
                else :
                    try :
                        self.api_requests.product_requets(
                            self.api_requests.category[int(CHOISE)].ide,self.page,self.index)
                        self.category_selec = int(CHOISE)
                        self.constent.start_list_item = 1
                        self.constent.end_list_item = 20
                        self.constent.build_table(self.api_requests.products)  
                        self.table = "produit"
                    except : pass
                    
                    
            if self.table == "produit":
                CHOISE = self.interface.display(self.constent.STATE[self.table])
                if CHOISE == CHOICE_a :
                    self.table = "category"
                    self.page = "/1"
                    self.index = 0
                    self.constent.start_list_item = 0
                    self.constent.end_list_item = 20
                    self.constent.build_table(self.api_requests.category)
                elif CHOISE == CHOICE_s:
                    self.index += 20
                    self.page = page(self.page,1)
                    self.api_requests.product_requets(
                        self.api_requests.category[self.category_selec].ide,self.page,self.index)                    
                    self.constent.start_list_item += 20
                    self.constent.end_list_item += 20
                    self.constent.build_table(self.api_requests.products)
                elif CHOISE == CHOICE_z :
                    self.index -= 20
                    if self.index < 0:
                        self.index = 0
                    self.page = page(self.page,-1)
                    self.api_requests.product_requets(
                        self.api_requests.category[self.category_selec].ide,self.page,self.index)                      
                    self.constent.start_list_item -= 20
                    if self.constent.start_list_item < 1:
                        self.constent.start_list_item = 1
                    self.constent.end_list_item -= 20
                    if self.constent.end_list_item < 1:
                        self.constent.end_list_item = 20
                    self.constent.build_table(self.api_requests.products)  
                        
                        
def page(page, indice):
    
    page = list(page)
    del page[0]
    page = int("".join(page)) + indice
    page = ["/",str(page)]
    page = "".join(page)
    return page
    
    

                

    
if __name__ == '__main__':

    main = Main()
    main.loop_master()
