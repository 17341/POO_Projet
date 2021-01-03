from Distrubuteur import *
from Meteo import *
from Market import *
from Central import *
from Reseau import *
from Consommateur import *
from ligne import *
from Noeud import *

import time

lines_centrales = []
lines_consommateurs = []

#On crée les centrales avec leurs lignes initiales
c1 = Central_Gaz(0,"Gaz")
c2 = Central_Nucleaire(0,"Nucleaire")
c3 = Central_Solaire(0,'Solaire')
c4 = Parc_Eolienne(0,'Eolienne')

stock = Stock(0,0,'Stock')

liste_centrales = [c1,c2,c3,c4,stock]

for central in liste_centrales:   
    lines_centrales.append(central.line)

distributeur = Distributeur("distributeur")

nc1 = Noeud_Concentration(500,"Noeud-Centrale",lines_centrales,distributeur.input_line)

cons1 = Consommateur(0,0,'ECAM')
ville1 = Ville(0,0,'Bruxelles',1090)
entreprise1 = Entreprise(0,0,'Microsoft','economy')
entreprise2 = Entreprise(0,0,'Microsoft2','economy')

liste_consommateurs = [cons1,ville1,entreprise1,entreprise2]

for conso in liste_consommateurs:   
    lines_consommateurs.append(conso.line)

nd1 = Noeud_Distribution(500,"Noeud-Consommateur",lines_consommateurs,distributeur.output_line)

reseau = Reseau(liste_consommateurs,liste_centrales,[nc1,nd1])

def run():
    messages = [distributeur_messages,markets_messages,centrales_messages,consommateurs_messages,lines_messages,noeuds_messages,reseau_messages]
    print("###########################################")    
    show_meteo(meteos)
    print("\n")  
    show_centrales(reseau.centrales)
    print("\n")
    show_consommateurs(reseau.consommateurs)
    print("\n")
    show_lines(lines_centrales+ lines_consommateurs)
    print("\n")
    show_noeuds(reseau.noeuds)
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
    distributeur.update(reseau.get_consommateurs(),reseau.get_centrales())
    distributeur.verify(stock = stock)
    
    
while(1):
    run()
    