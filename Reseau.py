from Consommateur import *
from Central import *

reseau_messages = []

class Reseau:

    def __init__(self,consommateurs = [],centrales = [], noeuds = []):
        self.consommateurs = consommateurs
        self.centrales = centrales
        self.noeuds = noeuds
    def show_reseau_messages(self):
        
        pass

    def get_consommateurs(self):
        return self.consommateurs

    def get_centrales(self):
        return self.centrales

    def update_reseau(self):
        for elem in self.consommateurs:
            print(elem.consumption)
        self.show_reseau_messages()
    
    def add_central(self,new_central):
        self.centrales.append(new_central)
        reseau_messages.append(f'A new central has been added to the network : {new_central}')

    def add_consommateur(self,new_consommateur):
        self.consommateurs.append(new_consommateur)
        reseau_messages.append(f'A new consummer has been added to the network : {new_consommateur}')
        
    def add_noeud(self,new_noeud):
        self.noeuds.append(new_noeud)
        reseau_messages.append(f'A new noeud has been added to the network : {new_noeud}')