class Line:
    def __init__(self,max_power,name,connexions = 0 ,status = False):
        self.max_power = max_power
        self.status = status
        self.name = name
        self.connexions= connexions 
       

    def check(self,current_power):
        if self.status:
            if current_power > self.max_power:
                print(f'{self.name} cant support this power')
            elif current_power == 0 :
                print(f'{self.name} unused ...')
            else :
                print("Ok")
        else:
            print(f'{self.name} is not connected !')


