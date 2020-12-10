from Central import *
from Reseau import *
from Consommateur import *

import time
import random

c1 = Consommateur('20W',5)
c2 = Consommateur('10W',2)
c3 = Consommateur('110W',33)
r1 = Reseau([c1,c2,c3],"centrale")

while(1):
    r1.update_reseau()
    demand = random.randint(10, 50)
    
    print("\n")
    c1.update_consumption(f'{demand}W')
    time.sleep(1)
   