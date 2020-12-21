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