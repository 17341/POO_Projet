import pandas as pd
import random as r

markets_messages = []


class Market:
    def __init__(self, pays, prix_de_vente, prix_achat, distance, quantity,combustible_prix):
        self.pays = pays
        self.prix_de_vente=  prix_de_vente
        self.prix_achat = prix_achat
        self.distance = distance
        self.quantity = quantity
        self.combustible_prix = combustible_prix
    def update_market(self, new_sell, new_buy,new_quantiy,new_combustible_prix):
        self.prix_de_vente=  new_sell
        self.prix_achat = new_buy
        self.quantity = new_quantiy
        self.combustible_prix = new_combustible_prix

    def sell(self,quantity,consommateur):
        if quantity > self.quantity :
            markets_messages.append("Error : U don't have enough supply!")
        else :
            self.quantity -= quantity
            consommateur.quantity += quantity
            markets_messages.append(f"We sold {quantity}[MW] to {consommateur.pays}")

    def buy(self,quantity,vendeur):
        if quantity > vendeur.quantity :
            markets_messages.append(f"Error : {vendeur.pays} don't have enough supply!")
            self.buy_fuel(markets,quantity)
        else :
            vendeur.quantity -= quantity
            self.quantity += quantity
            markets_messages.append(f"We bought {quantity}[MW] from {vendeur.pays}")

    def buy_fuel(self,liste_markets,demand):
        demand_m3 = demand/10
        best_vendeur = liste_markets[0]
        min_price = liste_markets[0].prix_de_vente
        for elem in liste_markets:
            if elem.pays != "ECAM":
                if elem.combustible_prix  < min_price:
                    min_price = elem.combustible_prix 
                    best_vendeur = elem  
        markets_messages.append(f"We bought fuel from {best_vendeur.pays} for {best_vendeur.combustible_prix *demand_m3} €")

    def  print_infos(self):
        markets_messages.append(self.pays, self.prix_de_vente, self.prix_achat, self.distance, self.quantity)


def best_market_sell(liste_markets):
    best_pays_sell = liste_markets[0]
    max_price = liste_markets[0].prix_achat

    for elem in liste_markets:
        if elem.pays != "ECAM":
            if elem.prix_de_vente > max_price:
                max_price = elem.prix_de_vente
                best_pays_sell = elem
    
    return(best_pays_sell)

def best_market_buy(liste_markets):
    best_pays_buy= liste_markets[0]
    min_price = liste_markets[0].prix_de_vente
   
    for elem in liste_markets:
        if elem.pays != "ECAM":
            
            if elem.prix_achat < min_price:
                min_price = elem.prix_achat
                best_pays_buy = elem  
         
    return(best_pays_buy)


def show_market(table):
    
    dict = {'Country' : [],'Quantity [MW]' : [],'Distance' : [],'Sell [€/MW]' : [],'Buy [€/MW]' : [], "Fuel price [€/m3]" : []}
    for elem in table:         
        dict['Country'].append(elem.pays)
        dict['Quantity [MW]'].append(elem.quantity)
        dict['Distance'].append(elem.distance)
        dict['Sell [€/MW]'].append(elem.prix_de_vente)
        dict['Buy [€/MW]'].append(elem.prix_achat)
        dict["Fuel price [€/m3]"].append(elem.combustible_prix)
        elem.update_market(r.randint(50,200),r.randint(10,100),elem.quantity,r.randint(10,100))

    df = pd.DataFrame(dict)
    df.isnull()
    markets_messages.append("Markets ")
    markets_messages.append(df)

cameroun = Market("Cameroun", 10, 19, 6000, 1000,10)
liban = Market("Liban", 100, 87, 600, 500,23)
our_market= Market("ECAM", 100, 87, 0, 0,7)
markets = [cameroun,liban,our_market]