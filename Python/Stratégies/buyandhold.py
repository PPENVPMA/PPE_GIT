# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:09:35 2019

@author: Pierre
import os


"""
######################################### INISTIALISATION ######################@
import numpy as np
import matplotlib.pyplot as plt

### BROKER
b1= Broker("BoursoramaDecouverte",(0,500,1.99,0,501,10**10,0,0.006))
b2= Broker("BoursoramaClassic", (0,5000,5.5,0,5001,10**10,0,0.0048))


#### NICOLAS

u1=User("Macé", "Nicolas")
p1= Portfolio(b1, 0.30, 0.15,10000)

s1=Stock("NATIXIS_SPOT",6.95,"€")
s2=Stock("CAC_SPOT",5365.83,"P")

i1=Investment(s1,100,"7/02/2019",6.95)
i2=Investment(s2,10,"07/02/2019",5365.83)

p1.add_ptf_investment(i1)
#p1.add_ptf_investment(i2)


def strat_buy_and_hold(start,Nb_Obs, periode):
    L_investments=p1.get_ptf_list_investments()
    
    for jour in range(start,Nb_Obs+start,periode):
        print("Jour " +str(jour))
        for investment in L_investments:
            investment.set_investment_cost(data.iloc[start][investment.get_investment_asset().get_asset_ISIN()])
            cout_investment = investment.get_investment_cost()
            
            prix_actif= data.iloc[jour][investment.get_investment_asset().get_asset_ISIN()]
            investment.get_investment_asset().set_asset_price(prix_actif)
            p1.comp_ptf_PnL()
            
            print(investment.get_investment_asset().get_asset_ISIN()+": Spot t0 :"+ str(cout_investment) + " Spot :" + str(investment.get_investment_asset().get_asset_price()))
        print("PnL de :"+ str(p1.get_ptf_PnL())+"\n")

            
            
strat_buy_and_hold(60,70,1)


