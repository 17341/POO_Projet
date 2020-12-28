from Consommateur import *
from Central import *

reseau_messages = []

class Reseau:

    def __init__(self,consommateurs = [],centrales = []):
        self.consommateurs = consommateurs
        self.centrales = centrales
    
    def show_reseau_messages(self):
        
        pass

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
    