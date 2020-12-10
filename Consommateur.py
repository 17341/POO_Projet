class Consommateur:
    
    def __init__(self,consumption,price,name):
        self.consumption = consumption
        self.price = price
        self.name= name

    def update_consumption(self,new_consumption):
        self.consumption = new_consumption
        

class Ville(Consommateur):
    def __init__(self,consumption,price,name,zip_code):
        super().__init__(consumption,price,name)
        self.zip = zip_code


class Entreprise(Consommateur):
    def __init__(self,consumption,price,name,activity):
        super().__init__(consumption,price,name)
        self.activity = activity
    

class Etranger(Consommateur):
    def __init__(self,consumption,price,name,transaction):
        super().__init__(consumption,price,name)
        self.transcation = transaction
    

class Dissipateur(Consommateur):

    def __init__(self,consumption,production):
        super().__init__(consumption,"","")
        self.production = production

    def update_production(self,new_production):
        self.production = new_production
        if self.production > self.consumption :
            print("We are dissipating energy ...")
        else : 
            print("Ok")
