class Central:
    
    def __init__(self,energy,cost,co2,demands):
        self.energy = energy
        self.cost = cost
        self.co2 = co2
        self.demands = demands

    def get_energy(self):
        return self.energy

    def get_cost(self):
        return self.cost

    def get_co2(self):
        return self.co2

    def update_demands(self,new_demands):
        self.demands = new_demands
        return self.demands

class Central_Solaire(Central):

    def __init__(self,energy,cost,meteo,demands):
        super().__init__(energy,cost,0,demands)
        self.meteo = meteo

class Parc_Eolienne(Central_Solaire):

    def __init__(self,energy,cost,meteo,demands):
        super().__init__(energy,cost,meteo,demands)

class Central_Nucleaire(Central):

    def __init__(self,energy,cost,co2,demands):
        super().__init__(energy,cost,co2,demands)

class Central_Gaz(Central_Nucleaire):
    
    def __init__(self,energy,cost,co2,demands):
        super().__init__(energy,cost,co2,demands)