from ligne import *
import pandas as pd
import random as r

consommateurs_messages = []

class Consommateur:
    
    def __init__(self,consumption,price,name,line,type = "Consommateur"):
        self.consumption = consumption
        self.price = price
        self.name= name
        self.line = line
        self.line.connexions = 1
        self.type = type

    def update_consumption(self,new_consumption):
        consommateurs_messages.append(f'Demands of {self.name} updated from {self.consumption}MW to {new_consumption}MW')
        self.consumption = new_consumption
        self.line.check()
        self.line.power = self.consumption - 10

class Ville(Consommateur):
    def __init__(self,consumption,price,name,zip_code,type = "Ville",line = Line(100,"Line-Ville")):
        super().__init__(consumption,price,name,line,type)
        self.zip = zip_code



class Entreprise(Consommateur):
    def __init__(self,consumption,price,name,activity,type = "Entreprise",line = Line(100,"Line-Entreprise")):
        super().__init__(consumption,price,name,line,type)
        self.activity = activity
    

class Etranger(Consommateur):
    def __init__(self,consumption,price,name,transaction,type = "Etranger",line = Line(100,"Line-Etranger")):
        super().__init__(consumption,price,name,line,type)
        self.transaction = transaction
    

class Dissipateur(Consommateur):

    def __init__(self,consumption,production,type = "Dissipateur",line = Line(1000,"Line-Dissipateur")):
        super().__init__(consumption,"","",line,type)
        self.production = production

    def update_production(self,new_consumption,new_production):
        self.consumption = new_consumption
        self.production = new_production
        if self.production > self.consumption :
            consommateurs_messages.append(f"Dissipating {self.production -self.consumption}[MW] of energy ! ")
            return True
        else : 
            consommateurs_messages.append("Ok")
            return False

def show_consommateurs(table):
    dict = {'Consumption [MW]' : [],'Price' : [],'Name' : [], 'Type' : []}
    for elem in table:
        elem.update_consumption(r.randint(0,100))
        dict['Consumption [MW]'].append(elem.consumption)
        dict['Price'].append(elem.price)
        dict['Name'].append(elem.name)
        dict['Type'].append(elem.type)

    df = pd.DataFrame(dict)
    df.isnull()
    print("Consommateurs ")
    print(df)