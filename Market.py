import pandas as pd
import random as r

markets_messages = []

class Market:
    def __init__(self, pays, prix_de_vente, prix_achat, distance, quantity):
        self.pays = pays
        self.prix_de_vente=  prix_de_vente
        self.prix_achat = prix_achat
        self.distance = distance
        self.quantity = quantity

    def update_market(self, new_sell, new_buy,new_quantiy):
        self.prix_de_vente=  new_sell
        self.prix_achat = new_buy
        self.quantity = new_quantiy

    def sell(self,quantity,consommateur):
        if quantity > self.quantity :
            markets_messages.append("Error : U don't have enough supply!")
        else :
            self.update_market(self.prix_de_vente,self.prix_achat,self.quantity-quantity)
            consommateur.quantity += quantity
            print(f"We sold {quantity} to {consommateur.pays}")

    def print_infos(self):
        markets_messages.append(self.pays, self.prix_de_vente, self.prix_achat, self.distance, self.quantity)


def best_market(liste_markets):
    best_pays_buy= liste_markets[0].pays
    best_pays_sell = liste_markets[0].pays
    min_price = liste_markets[0].prix_de_vente
    max_price = liste_markets[0].prix_achat

    for elem in liste_markets:
        if elem.prix_de_vente > max_price:
            max_price = elem.prix_de_vente
            best_pays_sell = elem
        if elem.prix_achat < min_price:
            min_price = elem.prix_achat
            best_pays_buy = elem   
    return(best_pays_sell,best_pays_buy)


def show_market(table):
    
    dict = {'Country' : [],'Quantity [MW]' : [],'Distance' : [],'Sell [€]' : [],'Buy [€]' : []}
    for elem in table:         
        dict['Country'].append(elem.pays)
        dict['Quantity [MW]'].append(elem.quantity)
        dict['Distance'].append(elem.distance)
        dict['Sell [€]'].append(elem.prix_de_vente)
        dict['Buy [€]'].append(elem.prix_achat)
        elem.update_market(r.randint(50,200),r.randint(10,100),elem.quantity)

    df = pd.DataFrame(dict)
    df.isnull()
    print("Markets ")
    print(df)
    
    
"""
cameroun = Market("Cameroun", 10, 19, 6000, 1000)
liban = Market("Liban", 100, 87, 600, 500)
markets = [cameroun,liban]

show_market(markets)
show_market(markets)
"""