from ligne import *
import time 

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
            print(f'Energy of {self.name} updated from {self.energy}MW to {new_energy}MW')
            self.energy = new_energy
        else:
            self.energy = new_energy
        self.cost = new_energy/2
        if self.type == 'Nucleaire' or self.type == 'Gaz' :
            self.co2 = self.energy/10
        else:
            self.co2 = 0

    def on(self):
        self.status = True
        print(f"{self.name} is ON")    

    def off(self):
        self.status = False
        print(f"{self.name} is OFF")      
              
class Central_Solaire(Central):

    def __init__(self,energy,name,meteo, line= Line(100,"Ligne-Solaire"),type = 'Solaire',status= False):
        super().__init__(energy,name,line,type,status) 
        self.meteo = meteo
        

class Parc_Eolienne(Central_Solaire):

    def __init__(self,energy,name,meteo,line= Line(100,"Ligne-Eolienne"),type = 'Eolienne',status= False):
        super().__init__(energy,name,meteo,line,type,status) 
        
        
class Central_Nucleaire(Central):

    def __init__(self,energy,name,line= Line(100,"Ligne-Nucleaire"),type = 'Nucleaire',status= False):
        super().__init__(energy,name,line,type,status)
    
    def on(self):
        time.sleep(2)
        self.status = True
        print(f"{self.name} is ON")    

    def off(self):
        time.sleep(2)
        self.status = False
        print(f"{self.name} is OFF")      

class Central_Gaz(Central):
    
    def __init__(self,energy,name,line= Line(100,"Ligne-Gaz"),type = 'Gaz',status= False):
        super().__init__(energy,name,line,type,status)
        
class Stock(Central):
    
    def __init__(self,energy,stock,name,line= Line(300,"Ligne-Stock"),type = 'Stock',status= False):
        super().__init__(energy,0,0,name,line,type,status) #CO2 == 0
        self.stock = stock 

    def update(self,new_energy,new_demand):
        if  new_energy > new_demand :
            print("We are stocking energy ...")
            self.stock += new_energy - new_demand
            print(self.stock)
        else : 
            print("Ok")
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