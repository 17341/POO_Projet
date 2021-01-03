import pandas as pd 
import random as r
class Meteo:

    def __init__(self,temperature,wind_speed,status):
        self.temperature = temperature
        self.wind_speed = wind_speed 
        self.status = status
    
    def update(self,new_temperature,new_wind_speed,new_status):
        self.temperature = new_temperature
        self.wind_speed = new_wind_speed 
        self.status = new_status
    def print_infos(self):
        print(self.temperature,self.wind_speed,self.status)
 
meteos = Meteo(0,50,"Neige")

def show_meteo(meteo):
    dict = {'Temperature [°C]' : [],'Wind Speed [km/h]' : [],'Status' : []}
    dict['Temperature [°C]'].append(meteo.temperature)
    dict['Wind Speed [km/h]'].append(meteo.wind_speed)
    dict['Status' ].append(meteo.status)
    df = pd.DataFrame(dict)
    df.isnull()
    print("Meteo ")
    print(df)
    meteo.update(r.randint(20,40),r.randint(10,120),r.choice(["Neige","Pluie","Soleil"]))