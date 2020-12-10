from Consommateur import *
from Central import *

class Reseau:

    def __init__(self,consommateurs,centrales):
        self.consommateurs = consommateurs
        self.centrales = centrales
    
    def show_messages(self):
        
        pass

    def update_reseau(self):
        for elem in self.consommateurs:
            print(elem.get_consumption())
        self.show_messages()
    
    def add_central(self,new_central):
        self.centrales.append(new_central)
       

    def add_consommateur(self,new_consommateur):
        self.consommateurs.append(new_consommateur)
        