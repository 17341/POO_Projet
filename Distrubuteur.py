from Consommateur import *
from Central import *

class Distributeur:
    def __init__(self,list_demands = [],list_energy= []):
        self.list_demands = list_demands
        self.list_energy  = list_energy

    def get_total(self, list):
        if list == 'demands':
            total = sum(self.list_demands)
            return total 
        elif list == 'energy':
            total = sum(self.list_energy)
            return total 
        else :
            pass

    def update(self,list_consommateur,list_centrales):
        new_list_demands = []
        new_list_energy = []
        for consommateur in list_consommateur:
            new_list_demands.append(consommateur.consumption)
        self.list_demands = new_list_demands
        for central in list_centrales:
            new_list_energy.append(central.energy)
        self.list_energy  = new_list_energy

    def verify(self,stock):
        
        if self.get_total('demands') == self.get_total('energy') :
            print("Ok")
        elif self.get_total('demands') > self.get_total('energy') :
            print("WE NEED MORE ENERGY")
            #get_more_energy() #Si le total de demandes est plus grand que le max d'energy que peut fournir les centrales ensemble --> On achetera ...
        else :
            stock.update(self.get_total('energy'),self.get_total('demands'))