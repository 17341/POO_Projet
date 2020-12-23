# importing pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
# importing numpy as np
import numpy as np

# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}

# creating a dataframe from list
df = pd.DataFrame(dict)

# using isnull() function  
df.isnull()

df.plot()

def show_table(table):
    dict = {'Energy' : [],'Cost' : [],'CO2' : [] }

    for elem in table:
        dict['Energy'].append(elem.energy)
        dict['Cost'].append(elem.cost)
        dict['CO2'].append(elem.co2)

    df = pd.DataFrame(dict)
    df.isnull()
    print(df)


"""
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