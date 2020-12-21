from Distrubuteur import *
from Meteo import Meteo
from Central import *
from Reseau import *
from Consommateur import *

import pandas as pd
import time
import random as r

d = Distributeur()
m_j1= Meteo(20,50,'Ensoleillé')
s1 = Stock(0,0,"Stock")

cons1 = Consommateur(20,5,'kola')
ville1 = Ville(10,2,'kola',1090)
entreprise1 = Entreprise(110,33,'kola','economy')

c1 = Central_Gaz(10,1,5,"Gaz")
c2 = Central_Nucleaire(70,1,5,"Nucleaire")
c3 = Central_Solaire(80,1,5,'Solaire')



r1 = Reseau([cons1,ville1,entreprise1],[c1,c2,c3])
d.update(r1.consommateurs,r1.centrales)


d.verify(s1)

def show_centrales(table):
    dict = {'Energy' : [],'Cost' : [],'CO2' : [],'Name' : []}
    
    for elem in table:
        dict['Energy'].append(elem.energy)
        dict['Cost'].append(elem.cost)
        dict['CO2'].append(elem.co2)
        dict['Name'].append(elem.name)
        if elem.type == "Solaire" :
            elem.update_infos(r.randint(0,10),r.randint(10,100),0)
        else :
            elem.update_infos(r.randint(0,10),r.randint(10,100),r.randint(100,1000))

    df = pd.DataFrame(dict)
    df.isnull()
    print("Centrales ")
    print(df)
    
def show_consommateurs(table):
    dict = {'Consumption' : [],'Price' : [],'Name' : [] }
    
    for elem in table:
        dict['Consumption'].append(elem.consumption)
        dict['Price'].append(elem.price)
        dict['Name'].append(elem.name)

    df = pd.DataFrame(dict)
    df.isnull()
    print("Consommateurs ")
    print(df)

while(1):
    print("##############################################################################################")          
    show_centrales(r1.centrales)
    print("\n")
    show_consommateurs(r1.consommateurs)
    time.sleep(2)

