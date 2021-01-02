from numpy.lib.function_base import diff
from ligne import *
import time
import pandas as pd
import random as r
from Consommateur import *
from Market import *
from Meteo import *

centrales_messages = []

class Central:
    def __init__(self,energy,name,line,type,status):
        self.energy = energy
        self.name = name
        self.type = type
        self.line = line
        self.status = status
        self.cost = energy/2
        if type == 'Nucleaire' or type == 'Gaz' :
            self.co2 = energy/10
        else:
            self.co2 = 0
        
    def print_infos(self):
        print(f'Name: {self.name}   Production: {self.energy}W   Cost: {self.cost}€   CO2: {self.co2}')

    def update_infos(self,new_energy):
        if new_energy != self.energy:
            centrales_messages.append(f'Energy of {self.name} updated from {self.energy}MW to {new_energy}MW')
        else:
            pass
        self.energy = new_energy
        self.line.power = self.energy - 10
        self.cost = new_energy/2
        if self.type == 'Nucleaire' or self.type == 'Gaz' :
            self.co2 = self.energy/10
        else:
            self.co2 = 0

    def on(self):
        self.status = True
        centrales_messages.append(f"{self.name} is ON")    

    def off(self):
        self.status = False
        centrales_messages.append(f"{self.name} is OFF")      
    
    def check(self):
        if self.energy == 0 :
            self.status = False
            centrales_messages.append(f'{self.name} has no energy')
        else:
            self.status = True
              
class Central_Solaire(Central):

    def __init__(self,energy,name, line= Line(100,"Ligne-Solaire"),type = 'Solaire',status= False):
        super().__init__(energy,name,line,type,status) 

    def check_meteo(self,meteo):
        if meteo.status == "Soleil":
            self.energy = meteo.temperature / 2
            self.line.power = self.energy - 10
        else:
            self.energy = 0
            self.line.power = self.energy

class Parc_Eolienne(Central):

    def __init__(self,energy,name,line= Line(100,"Ligne-Eolienne"),type = 'Eolienne',status= False):
        super().__init__(energy,name,line,type,status) 
        
    def check_meteo(self,meteo):
        if meteo.wind_speed < 120:
            if meteo.wind_speed > 15:
                self.energy =meteo.wind_speed/ 2
                self.line.power = self.energy - 10
                if (self.energy - 10) > 0 :
                    self.line.power = self.energy - 10
                else:
                    self.line.power = 0
            else:
                self.energy = 0
                self.line.power = self.energy
        else:
            self.energy = 0
            self.line.power = self.energy

class Central_Nucleaire(Central):

    def __init__(self,energy,name,line= Line(100,"Ligne-Nucleaire"),type = 'Nucleaire',status= False):
        super().__init__(energy,name,line,type,status)
    
    def on(self):
        time.sleep(2)
        self.status = True
        self.line.connexions += 1
        centrales_messages.append(f"{self.name} is ON")    

    def off(self):
        time.sleep(2)
        self.status = False
        self.line.connexions -= 1
        centrales_messages.append(f"{self.name} is OFF")      

class Central_Gaz(Central):
    
    def __init__(self,energy,name,line= Line(100,"Ligne-Gaz"),type = 'Gaz',status= False):
        super().__init__(energy,name,line,type,status)
        
class Stock(Central):
    
    def __init__(self,energy,stock,name,line= Line(300,"Ligne-Stock"),type = 'Stock',status= False,max_stock = 500,dissipateur = Dissipateur(0,0)):
        super().__init__(energy,name,line,type,status) #CO2 == 0
        self.stock = stock
        self.max_stock = max_stock
        self.dissipateur = dissipateur
        self.dissipateur.consumption = max_stock - stock
        self.can_dissipate = True

    def verify_stock(self):
        if self.stock < self.max_stock :
            self.can_dissipate = True
        else:
            self.can_dissipate = False

    def update(self,new_energy,new_demand):
        self.verify_stock()
        if (new_energy - new_demand) > 0 :
            quantity = (new_energy - new_demand) - (self.max_stock - self.stock)
            if self.can_dissipate :
                if self.dissipateur.update_production((self.max_stock - self.stock), new_energy - new_demand ):
                    self.stock = self.max_stock
                    self.can_dissipate = False
                elif self.stock <= self.max_stock:
                    if  new_energy > new_demand :
                        centrales_messages.append("We are stocking energy ...")
                        self.energy = new_energy - new_demand 
                        self.update_infos(self.energy)
                        self.line.power += 10
                        self.stock += self.energy
                        centrales_messages.append(self.energy)
                    else : 
                        self.line.power = 0
                        centrales_messages.append("Ok")
            else:
                self.line.power = 0
                our_market.quantity = quantity
                our_market.sell(quantity,best_market_sell(markets))
                show_market(markets)
            
        elif (new_energy - new_demand) < 0 :
            self.line.power = 0
            quantity = new_demand-new_energy 
            if self.stock >= quantity :
                self.stock -= quantity
                self.line.power = quantity
                centrales_messages.append(f"We took {quantity} [MW] of energy from our stock")
            else:
                
                our_market.buy(quantity,best_market_buy(markets))
                show_market(markets)
        else:
            pass  
        
def show_centrales(table):
    dict = {'Energy [MW]' : [],'Cost [€]' : [],'CO2 [g/kWh]' : [],'Name' : [],'Status' : []}
    for elem in table:
        if elem.type == "Solaire" :
            elem.line.check()
            elem.check()
            dict['Energy [MW]'].append(elem.energy)
            dict['Cost [€]'].append(elem.cost)
            dict['CO2 [g/kWh]'].append(elem.co2)
            dict['Name'].append(elem.name)
            dict['Status'].append(elem.status)
            
        elif elem.type == "Eolienne" :
            elem.line.check()
            elem.check()
            dict['Energy [MW]'].append(elem.energy)
            dict['Cost [€]'].append(elem.cost)
            dict['CO2 [g/kWh]'].append(elem.co2)
            dict['Name'].append(elem.name)
            dict['Status'].append(elem.status)

        elif elem.type != "Stock" :
            elem.line.check()
            elem.check()
            dict['Energy [MW]'].append(elem.energy)
            dict['Cost [€]'].append(elem.cost)
            dict['CO2 [g/kWh]'].append(elem.co2)
            dict['Name'].append(elem.name)
            dict['Status'].append(elem.status)

        else:
            elem.line.check()
            elem.check()
            dict['Energy [MW]'].append(elem.stock)
            dict['Cost [€]'].append(elem.cost)
            dict['CO2 [g/kWh]'].append(elem.co2)
            dict['Name'].append(elem.name)
            dict['Status'].append(elem.status)


    df = pd.DataFrame(dict)
    df.isnull()
    print("Centrales ")
    print(df)
    

"""
c1 = Central_Gaz(10,1,5,100)
c2 = Central_Nucleaire(70,1,5,100)
c3 = Central_Solaire(80,1,5,100)

centrales= [c1,c2,c3]

demande_total = c1.demands
energy_total = 0 

for central in centrales:
    energy_total += central.energy

s1 = Stock(0,0,0) #On crée une boite de stockage 
s1.update(energy_total,demande_total) #On regarde si la demande et la production d'energie ont changé
print(s1.stock) #Si la productton > demande on stock la difference dans S1

"""