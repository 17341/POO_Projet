class Meteo:

    def __init__(self,temperature,wind_speed,status):
        self.temperature = temperature
        self.wind_speed = wind_speed 
        self.status = status
    
    def update_infos(self,infos,new_infos):
        if infos == 'temperature':
            self.temperature = new_infos
            return self.temperature
        if infos == 'wind_speed':
            self.wind_speed = new_infos
            return self.wind_speed
        if infos == 'status':
            self.status = new_infos
            return self.status
    def print_infos(self):
        print(self.temperature,self.wind_speed,self.status)

meteo = Meteo(10,50,"Soleil")
meteo.print_infos()
meteo.update_infos('temperature',24)
meteo.update_infos('wind_speed',100)
meteo.update_infos('status',"Pluie")
meteo.print_infos()