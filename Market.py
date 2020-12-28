markets_messages = []

class Market:
    def __init__(self, pays, prix_de_vente, prix_achat, distance, quantity):
        self.pays = pays
        self.prix_de_vente=  prix_de_vente
        self.prix_achat = prix_achat
        self.distance = distance
        self.quantity = quantity

    def update_market(self, value, new_value):
        if value == 'pays':
            self.pays = new_value
            return self.pays
        if value == 'prix_de_vente':
            self.prix_de_vente = new_value
            return self.prix_de_vente
        if value == 'prix_achat':
            self.prix_achat = new_value
            return self.prix_achat
        if value == 'distance':
            self.distance = new_value
            return self.distance
        if value == 'quantity':
            self.quantity = new_value
            return self.quantity

    def sell(self,quantity,consommateur):
        if quantity > self.quantity :
            markets_messages.append("Error : U don't have enough supply!")
        else :
            self.update_market('quantity', self.quantity-quantity)
            consommateur.quantity += quantity

    def print_infos(self):
        markets_messages.append(self.pays, self.prix_de_vente, self.prix_achat, self.distance, self.quantity)
        
"""
cameroun = Market("Cameroun", 10, 19, 6000, 1000)
liban = Market("Liban", 100, 87, 600, 500)
markets = [cameroun,liban]

for elem in markets:
    elem.print_infos()
"""
def best_market(liste_markets):
    best_pays_buy= liste_markets[0].pays
    best_pays_sell = liste_markets[0].pays
    min_price = liste_markets[0].prix_de_vente
    max_price = liste_markets[0].prix_achat

    for elem in liste_markets:
        if elem.prix_de_vente < min_price:
            min_price = elem.prix_de_vente
            best_pays_sell = elem.pays
        if elem.prix_achat > max_price:
            max_price = elem.prix_achat
            best_pays_buy = elem.pays
    markets_messages.append("Le meilleur marché du moment est le : ....")   
    return(best_pays_sell,best_pays_buy)

