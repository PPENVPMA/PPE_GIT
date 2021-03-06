#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:46:09 2019

@author: mithurangajendran
"""

class User:
    #__user_lastname = None
    #__user_firstname = None
    #__user_risk = None
    
    def __init__(self,user_lastname, user_firstname):
        self.__user_lastname = user_lastname
        self.__user_firstname = user_firstname
        self.__user_risk = None
        self.__user_list_portfolio= list()
        
    def __repr__(self):
        return '{user_lastname: '+self.__user_lastname+\
                ', user_firstname: '+\
                self.__user_firstname+\
                ', user_risk: '+str(self.__user_risk)+\
                ', user_list_portfolio:'+ str(self.__user_list_portfolio)+'}'
        
# ACCESSEURS        
    
    def get_user_lastname(self):
        return self.__user_lastname 
    
    def get_user_firstname(self):
        return self.__user_firstname 
    
    def get_user_risk(self):
        return self.__user_risk 
    
    def get_user_list_portfolio(self):
        return self.get_user_list_portfolio
    
    
    def set_user_lastname(self, user_lastname):
        self.__user_lastname = user_lastname
    
    def set_user_firstname(self, user_firstname):
        self.__user_firstname = user_firstname
    
    def set_user_risk(self, user_risk):
        self.__user_risk = user_risk   

    def set_user_list_portfolio(self, user_list_portfolio):
        self.__user_list_portfolio=user_list_portfolio   

# METHODES
        
    def add_user_list_portfolio(self,user_portfolio):
        self.__user_list_portfolio.append(user_portfolio)
        
