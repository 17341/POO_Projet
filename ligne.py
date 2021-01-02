lines_messages = []
import pandas as pd

class Line:
    def __init__(self,max_power,name,status = False ,connexions = 0, power = 0):
        self.max_power = max_power
        self.status = status
        self.name = name
        self.power = power
        self.connexions = connexions

    def check(self):
        if self.power == 0 :
            self.status = False
            lines_messages.append(f'{self.name} unused ...')
        elif self.power > self.max_power:
            lines_messages.append(f'{self.name} cant support this power')
            self.status = False
        else:
            lines_messages.append(f'The {self.name} is running {self.power}')
            self.status = True

def show_lines(table):
    dict = {'Power [MW]' : [],'Name' : [],'Status' : [],'Max Power [MW]' : []  }
    
    for elem in table:
        dict['Power [MW]'].append(elem.power)
        dict['Name'].append(elem.name)
        dict['Status'].append(elem.status)
        dict['Max Power [MW]'].append(elem.max_power)

    df = pd.DataFrame(dict)
    df.isnull()
    print("Lines ")
    print(df)