while(1):
    print("##############################################################################################")          
    show_centrales(r1.centrales)
    print("\n")
    show_consommateurs(r1.consommateurs)
    time.sleep(2)

d = Distributeur()
m_j1= Meteo(20,50,'Ensoleillé')
s1 = Stock(0,0,"Stock")

cons1 = Consommateur(20,5,'kola')
ville1 = Ville(10,2,'kola',1090)
entreprise1 = Entreprise(110,33,'kola','economy')



r1 = Reseau([cons1,ville1,entreprise1],[c1,c2,c3])
d.update(r1.consommateurs,r1.centrales)


d.verify(s1)
l1 = Line(50,"Line1")
l2 = Line(100,"Line2")
l3 = Line(70,"Line3")
l4 = Line(70,"Line4")
 
n1 = Noeud(1000,"n1",1,[l1,l2])
n2 = Noeud(1000,"n1",1,[l3,l2])
n3 = Noeud(1000,"n1",1,[l4,l2])

n3.add_line(l1)
n1.lines_names()
n2.lines_names()
n3.lines_names()
"""