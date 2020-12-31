lines_messages = []
import pandas as pd

class Line:
    def __init__(self,max_power,name,status = False,connexions = 0 ,power = 0):
        self.max_power = max_power
        self.status = status
        self.name = name
        self.connexions= connexions 
        self.power = power

    def check(self):
        if self.connexions == 2 :
            self.status = True
            if self.power > self.max_power:
                lines_messages.append(f'{self.name} cant support this power')
            elif self.power == 0 :
                lines_messages.append(f'{self.name} unused ...')
            else :
                lines_messages.append("Ok")

        elif self.connexions == 1 : 
            self.status = False
            lines_messages.append(f'{self.name} is connected to 1 point only !')

        else : 
            self.status = False
            lines_messages.append(f'{self.name} is not connected !')



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