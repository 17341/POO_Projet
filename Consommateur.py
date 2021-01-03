from ligne import *
import pandas as pd
import random as r

consommateurs_messages = []

class Consommateur:
    
    def __init__(self,consumption,price,name,type = "Consommateur",status = False,):
        self.consumption = consumption
        self.price = price
        self.name= name
        self.line = Line(100,"Ligne-"+name)
        self.line.connexions = 1
        self.type = type
        self.status = status

    def update_consumption(self,new_consumption):
        consommateurs_messages.append(f'Demands of {self.name} updated from {self.consumption}MW to {new_consumption}MW')
        self.consumption = new_consumption
        self.price = self.consumption / 10
        self.line.power = self.consumption 

    def check(self):
        if self.consumption== 0 :
            self.status = False
            consommateurs_messages.append(f'{self.name} has no energy')
        else:
            self.status = True

class Ville(Consommateur):
    def __init__(self,consumption,price,name,zip_code,type = "Ville"):
        super().__init__(consumption,price,name,type)
        self.zip = zip_code
       

class Entreprise(Consommateur):
    def __init__(self,consumption,price,name,activity,type = "Entreprise"):
        super().__init__(consumption,price,name,type)
        self.activity = activity
        

class Etranger(Consommateur):
    def __init__(self,consumption,price,name,transaction,type = "Etranger"):
        super().__init__(consumption,price,name,type)
        self.transaction = transaction
        

class Dissipateur(Consommateur):

    def __init__(self,consumption,production,name,type = "Dissipateur"):
        super().__init__(consumption,"",name,type)
        self.production = production
        self.name = name
        

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
    dict = {'Consumption [MW]' : [],'Price' : [],'Name' : [], 'Type' : [], 'Status' : []}
    for elem in table:
        elem.line.check()
        elem.check()
        dict['Consumption [MW]'].append(elem.consumption)
        dict['Price'].append(elem.price)
        dict['Name'].append(elem.name)
        dict['Type'].append(elem.type)
        dict['Status'].append(elem.status)       

    df = pd.DataFrame(dict)
    df.isnull()
    print("Consommateurs ")
    print(df)