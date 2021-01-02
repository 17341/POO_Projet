from Consommateur import *
from Central import *

distributeur_messages = []

class Distributeur:
    def __init__(self,list_demands = [],list_energy= [],input_line= Line(500,"Input-Distributeur"),output_line= Line(500,"Output-Distributeur")):
        self.list_demands = list_demands
        self.list_energy  = list_energy
        self.input_line = input_line
        self.output_line = output_line

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
            consommateur.update_consumption(r.randint(20,100))
            new_list_demands.append(consommateur.consumption)
        self.list_demands = new_list_demands
    
        for central in list_centrales:
            if central.type == "Eolienne" :
                central.check_meteo(meteos)
            elif central.type == "Solaire" :
                central.check_meteo(meteos)
            elif central.type != "Stock":
                central.update_infos(r.randint(20,100))
            else:
                pass
            new_list_energy.append(central.energy)
            
        self.list_energy  = new_list_energy

    def verify(self,stock):
        distributeur_messages.append(self.get_total('demands'))
        distributeur_messages.append(self.get_total('energy'))
        if self.get_total('demands') == self.get_total('energy') :
            distributeur_messages.append("Ok we have enough energy")
        elif self.get_total('demands') > self.get_total('energy') :
            distributeur_messages.append("WE NEED MORE ENERGY")
            stock.update(self.get_total('energy'),self.get_total('demands'))
        else :
            distributeur_messages.append("We will stock energy")
            stock.update(self.get_total('energy'),self.get_total('demands'))
