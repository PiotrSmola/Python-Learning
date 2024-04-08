import random
from array import *

tablica = array('i', [])
for x in range(10):
    tablica.append(random.randint(-5, 5))
with open('result.txt', 'w') as file:
    for i in range(len(tablica)):
        file.write(str(tablica[i]))
        file.write(" ")

file.close()
