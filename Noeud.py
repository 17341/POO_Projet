from typing import List
from ligne import *

class Noeud:
    def __init__(self,max_power,name,lines: List[Line]):
        self.max_power = max_power
        self.name = name
        self.lines = lines 
        self.verify()

    def verify(self):
        remove_list = []
        for line in self.lines :
            if line.connexions < 2:
                if type(line) != Line:
                    print(f'{line.name} is not a line!')
                else:
                    line.connexions += 1
                    line.status = True
            else: 
                print(f'{line.name} already used')
                remove_list.append(line)

        for elem in remove_list:        
            self.lines.remove(elem) 

    def add_line(self,line):
        if type(line) == Line:
            self.lines.append(line)
            self.verify()
        else: 
            print(f'{line} is not a line')

    def remove_line(self,line):
        if type(line) == Line:
            self.lines.remove(line)
            self.verify()
        else: 
            print(f'{line} is not a line')

    def lines_names(self):
        for line in self.lines:
            print(line.name)

class Noeud_Concentration(Noeud):
    def __init__(self,max_power,name,lines,output_line):
        super().__init__(max_power,name, lines) #CO2 == 0
        self.output_line = output_line
        self.verify_output()

    def verify_output(self):
        if type(self.output_line) == Line and self.output_line.connexions < 2:
            print("OK output ")
        else : 
            print("Error output")

class Noeud_Distribution(Noeud):

    def __init__(self,max_power,name ,lines,input_line):
        self.input_line = input_line
        super().__init__(max_power,name,lines)
        self.verify_input()

    def verify_input(self):
        if type(self.input_line) == Line and (self.input_line).connexions < 2:
            print("OK input")
        else : 
            print("Error output")


l1 = Line(50,"Line1")
l2 = Line(100,"Line2")
l3 = Line(70,"Line3")
l4 = Line(70,"Line4")
l5 = Line(70,"Line5")
l6 = Line(70,"Line6")
l7 = Line(70,"Line7")
l8 = Line(70,"Line8")
l9 = Line(70,"Line9")

n1 = Noeud_Distribution(1000,'Nd1',[l1,l2],l3)


n2 = Noeud_Distribution(1000,'Nd2',[l4,l5],l1)


n3 = Noeud_Concentration(1000,'Nc3',[l4,l5,l2],l6)


n3 = Noeud_Concentration(1000,'Nc3',[l9,l5,l4],l8)

n3.lines_names()