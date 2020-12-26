from ligne import *

class Consommateur:
    
    def __init__(self,consumption,price,name,line):
        self.consumption = consumption
        self.price = price
        self.name= name
        self.line = line

    def update_consumption(self,new_consumption):
        self.consumption = new_consumption
        

class Ville(Consommateur):
    def __init__(self,consumption,price,name,zip_code,line = Line(100,"Line-Ville")):
        super().__init__(consumption,price,name,line)
        self.zip = zip_code



class Entreprise(Consommateur):
    def __init__(self,consumption,price,name,activity,line = Line(100,"Line-Entreprise")):
        super().__init__(consumption,price,name,line)
        self.activity = activity
    

class Etranger(Consommateur):
    def __init__(self,consumption,price,name,transaction,line = Line(100,"Line-Etranger")):
        super().__init__(consumption,price,name,line)
        self.transaction = transaction
    

class Dissipateur(Consommateur):

    def __init__(self,consumption,production,line = Line(100,"Line-Dissipateur")):
        super().__init__(consumption,"","",line)
        self.production = production

    def update_production(self,new_production):
        self.production = new_production
        if self.production > self.consumption :
            print("We are dissipating energy ...")
        else : 
            print("Ok")
