class Central:
    
    def __init__(self,energy,cost,co2,name,type):
        self.energy = energy
        self.cost = cost
        self.co2 = co2
        self.name = name
        self.type = type

    def print_infos(self):
        print(f'Name: {self.name}   Production: {self.energy}W   Cost: {self.cost}€   CO2: {self.co2}')

    def update_infos(self,new_energy,new_cost,new_co2):
        self.energy = new_energy
        self.cost = new_cost
        self.co2 = new_co2

       
class Central_Solaire(Central):

    def __init__(self,energy,cost,meteo,name,type = 'Solaire'):
        super().__init__(energy,cost,0,name,type) #CO2 == 0
        self.meteo = meteo

class Parc_Eolienne(Central_Solaire):

    def __init__(self,energy,cost,meteo,name,type = 'Eolienne'):
        super().__init__(energy,cost,meteo,name,type) 
        
class Central_Nucleaire(Central):

    def __init__(self,energy,cost,co2,name,type = 'Nucleaire'):
        super().__init__(energy,cost,co2,name,type)

class Central_Gaz(Central):
    
    def __init__(self,energy,cost,co2,name,type = 'Gaz'):
        super().__init__(energy,cost,co2,name,type )

class Stock(Central):
    
    def __init__(self,energy,stock,name):
        super().__init__(energy,0,0,name,0) #CO2 == 0
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