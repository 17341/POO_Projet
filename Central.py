class Central:
    
    def __init__(self,energy,cost,co2,demands):
        self.energy = energy
        self.cost = cost
        self.co2 = co2
        self.demands = demands
        
    def update_demands(self,new_demands):
        self.demands = new_demands
        return self.demands



class Central_Solaire(Central):

    def __init__(self,energy,cost,meteo,demands):
        super().__init__(energy,cost,0,demands) #CO2 == 0
        self.meteo = meteo

class Parc_Eolienne(Central_Solaire):

    def __init__(self,energy,cost,meteo,demands):
        super().__init__(energy,cost,meteo,demands) 
        
class Central_Nucleaire(Central):

    def __init__(self,energy,cost,co2,demands):
        super().__init__(energy,cost,co2,demands)

class Central_Gaz(Central):
    
    def __init__(self,energy,cost,co2,demands):
        super().__init__(energy,cost,co2,demands)

class Stock(Central):
    
    def __init__(self,energy,demands,stock):
        super().__init__(energy,0,0,demands) #CO2 == 0
        self.stock = stock 

    def update(self,new_energy,new_demand):
        self.demands = new_demand
        self.energy = new_energy
        if  self.energy > self.demands :
            print("We are stocking energy ...")
            self.stock += self.energy - self.demands
        else : 
            print("Ok")

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

