from Consommateur import *
from Central import *

distributeur_messages = []

class Distributeur:
    def __init__(self,name,list_demands = [],list_energy= []):
        self.list_demands = list_demands
        self.list_energy  = list_energy
        self.name = name
        self.input_line = Line(100,"Input-"+name)
        self.output_line = Line(100,"Output-"+name)

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
            consommateur.update_consumption(r.randint(0,200))
            new_list_demands.append(consommateur.consumption)
        self.list_demands = new_list_demands
    
        for central in list_centrales:
            if central.type == "Eolienne" :
                central.check_meteo(meteos)
            elif central.type == "Solaire" :
                central.check_meteo(meteos)
            elif central.type != "Stock":
                central.update_infos(r.randint(0,200))
            else:
                pass
            new_list_energy.append(central.energy)
            
        self.list_energy  = new_list_energy

    def verify(self,stock):
        if self.get_total('demands') == self.get_total('energy') :
            distributeur_messages.append("Ok we have enough energy")
        elif self.get_total('demands') > self.get_total('energy') :
            stock.update(self.get_total('energy'),self.get_total('demands'))
        else :
            stock.update(self.get_total('energy'),self.get_total('demands'))
