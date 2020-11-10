#!/usr/bin/python3
# -*- coding: utf8 -*-

import resource.api_requests
import resource.interface
import resource.constent


CHOISE = ""
CHOICE_1 = "1"
CHOICE_2 = "2"
CHOICE_QUIT = "3"   
CHOICE_a = "a"
CHOICE_z = "z"
CHOICE_s = "s"


class Main():
    
    def __init__(self):
        
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
                    self.api_requests.product_requets(self.api_requests.category[int(CHOISE)].ide,"/1")
                    self.constent.build_table(self.api_requests.products)  
                    self.table = "produit"
            if self.table == "produit":
                CHOISE = self.interface.display(self.constent.STATE[self.table])

                        

                

    

main = Main()
main.loop_master()
