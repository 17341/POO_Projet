from Distrubuteur import *
from Meteo import *
from Market import *
from Central import *
from Reseau import *
from Consommateur import *
from ligne import *
from Noeud import *

import pandas as pd
import time
import random as r


def show_centrales(table):
  
    dict = {'Energy [MW]' : [],'Cost [€]' : [],'CO2 [g/kWh]' : [],'Name' : [],'Status' : []}
    for elem in table:
        if elem.type != "Stock" :
            elem.update_infos(r.randint(10,100))
            dict['Energy [MW]'].append(elem.energy)
            dict['Cost [€]'].append(elem.cost)
            dict['CO2 [g/kWh]'].append(elem.co2)
            dict['Name'].append(elem.name)
            dict['Status'].append(elem.status)
        else:
            dict['Energy [MW]'].append(elem.stock)
            dict['Cost [€]'].append(elem.cost)
            dict['CO2 [g/kWh]'].append(elem.co2)
            dict['Name'].append(elem.name)
            dict['Status'].append(elem.status)

    df = pd.DataFrame(dict)
    df.isnull()
    print("Centrales ")
    print(df)

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

def show_lines(table):
    dict = {'Power [MW]' : [],'Name' : [],'Status' : [],'Connexions' : []  }
    
    for elem in table:
        dict['Power [MW]'].append(elem.power)
        dict['Name'].append(elem.name)
        dict['Status'].append(elem.status)
        dict['Connexions'].append(elem.connexions)

    df = pd.DataFrame(dict)
    df.isnull()
    print("Lines ")
    print(df)


lines_centrales = []
lines_consommateurs = []

#On crée les centrales avec leurs lignes initiales
c1 = Central_Gaz(0,"Gaz")
c2 = Central_Nucleaire(0,"Nucleaire")
c3 = Central_Solaire(0,'Solaire',10)
c4 = Parc_Eolienne(0,'Eolienne',8)
stock = Stock(0,0,'Stock')

liste_centrales = [c1,c2,c3,c4,stock]

for central in liste_centrales:   
    lines_centrales.append(central.line)
    central.on()

distributeur = Distributeur()

nc1 = Noeud_Concentration(500,"Noeud-Centrale",lines_centrales,distributeur.input_line)

cons1 = Consommateur(0,5,'kola',line = Line(100,"Line-Cons1"))
ville1 = Ville(0,2,'kola',1090)
entreprise1 = Entreprise(0,33,'kola','economy')

liste_consommateurs = [cons1,ville1,entreprise1]

for conso in liste_consommateurs:   
    lines_consommateurs.append(conso.line)

nd1 = Noeud_Distribution(500,"Noeud-Consommateur",lines_consommateurs,distributeur.output_line)

reseau = Reseau(liste_consommateurs,liste_centrales)

def run():
    messages = [centrales_messages,consommateurs_messages,markets_messages,distributeur_messages,lines_messages,noeuds_messages,reseau_messages]
    print("##############################################################################################")    
    print("\n")  
    distributeur.update(reseau.consommateurs,reseau.centrales)
    distributeur.verify(stock = stock)
    print(distributeur.get_total('energy'))
    print(distributeur.get_total('demands'))
    print("\n")  
    show_centrales(reseau.centrales)
    print("\n")
    show_consommateurs(reseau.consommateurs)
    print("\n")
    show_lines(lines_centrales+ lines_consommateurs)
    print("\n")
    print("################ MESSAGES ################")
    for list_msg in messages:
        if len(list_msg) > 0 :
            print("\n")
            for msg in list_msg:
                print(msg)
            list_msg.clear()
        else :
            pass
    time.sleep(2)
    print("\n")  
    
while(1):
    run()
    