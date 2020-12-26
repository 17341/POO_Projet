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
    dict = {'Energy' : [],'Cost' : [],'CO2' : [],'Name' : []}
    
    for elem in table:
        dict['Energy'].append(elem.energy)
        dict['Cost'].append(elem.cost)
        dict['CO2'].append(elem.co2)
        dict['Name'].append(elem.name)
        if elem.type == "Solaire" :
            elem.update_infos(r.randint(0,100))
        else :
            elem.update_infos(r.randint(0,100))

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


lines_centrales = []
lines_consommateurs = []

#On crée les centrales avec leurs lignes initiales
c1 = Central_Gaz(10,"Gaz")
c2 = Central_Nucleaire(70,"Nucleaire")
c3 = Central_Solaire(80,'Solaire',10)
c4 = Parc_Eolienne(80,'Eolienne',8)


liste_centrales = [c1,c2,c3,c4]

for central in liste_centrales:   
    lines_centrales.append(central.line)

distributeur = Distributeur()

nc1 = Noeud_Concentration(500,"Noeud-Centrale",lines_centrales,distributeur.input_line)

cons1 = Consommateur(20,5,'kola',line = Line(100,"Line-Cons1"))
ville1 = Ville(10,2,'kola',1090)
entreprise1 = Entreprise(110,33,'kola','economy')

liste_consommateurs = [cons1,ville1,entreprise1]

for conso in liste_consommateurs:   
    lines_consommateurs.append(conso.line)

nd1 = Noeud_Distribution(500,"Noeud-Consommateur",lines_consommateurs,distributeur.output_line)

reseau = Reseau(liste_consommateurs,liste_centrales)

def run():
    print("##############################################################################################")          
    show_centrales(reseau.centrales)
    print("\n")
    show_consommateurs(reseau.consommateurs)
    time.sleep(2)

while(1):
    run()