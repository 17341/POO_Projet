from typing import List
from ligne import *

noeuds_messages = []

class Noeud:
    def __init__(self,max_power,name,lines: List[Line], power= 0):
        self.max_power = max_power
        self.name = name
        self.lines = lines 
        self.power = power
        self.verify()

    def verify(self):
        remove_list = []
        for line in self.lines :
            if line.connexions < 2:
                if type(line) != Line:
                    noeuds_messages.append(f'{line.name} is not a line!')
                else:
                    line.connexions += 1
            else: 
                noeuds_messages.append(f'{line.name} already used')
                remove_list.append(line)

        for elem in remove_list:        
            self.lines.remove(elem) 

    def add_line(self,line):
        if type(line) == Line:
            self.lines.append(line)
            self.verify()
        else: 
            noeuds_messages.append(f'{line} is not a line')

    def remove_line(self,line):
        if type(line) == Line:
            self.lines.remove(line)
            self.verify()
        else: 
            noeuds_messages.append(f'{line} is not a line')

    def lines_names(self):
        for line in self.lines:
            noeuds_messages.append(line.name)

    def update(self):
        list_power_line = []
        for line in self.lines :
            list_power_line.append(line.power)
        self.power = sum(list_power_line)

    def check(self):
        if self.power > self.max_power:
            noeuds_messages.append(f"WARNING : TOO MUCH ENERGY IN {self.name}")
        else:
            noeuds_messages.append(f"The current power in {self.name} is {self.power} ")

class Noeud_Concentration(Noeud):
    def __init__(self,max_power,name,lines,output_line,type = "Concentration"):
        self.output_line = output_line
        self.type = type
        super().__init__(max_power,name, lines) #CO2 == 0
        self.verify_output()

    def verify_output(self):
        if type(self.output_line) == Line and self.output_line.connexions < 2:
            noeuds_messages.append("OK output ")
        else : 
            noeuds_messages.append("Error output")


class Noeud_Distribution(Noeud):

    def __init__(self,max_power,name ,lines,input_line,type = "Distribution"):
        super().__init__(max_power,name,lines)
        self.input_line = input_line
        self.type = type
        self.verify_input()

    def verify_input(self):
        if type(self.input_line) == Line and (self.input_line).connexions < 2:
            noeuds_messages.append("OK input")
        else : 
            noeuds_messages.append("Error output")


def show_noeuds(table):
    print("Noeuds")
    for elem in table:
        elem.update()
        elem.check()
        if elem.type == "Concentration":
            lines_name = []
            for line in elem.lines:
                lines_name.append(line.name)
            print(f"Name : {elem.name} \t Type : {elem.type} \t Power : {elem.power} \t Input line(s) : {lines_name} \t Output line(s)  : {elem.output_line.name}")
        elif elem.type == "Distribution":
            lines_name = []
            for line in elem.lines:
                lines_name.append(line.name)
            print(f"Name : {elem.name} \t Type : {elem.type} \t Power : {elem.power} \t Input line(s) : {elem.input_line.name} \t Output line(s)  : {lines_name}")
        else :
            pass
"""
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
"""
