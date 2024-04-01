# while
# while <condición_verdadera>:
# expresiones booleanas(OR, AND) y operaciones de comparación (<, <=, >, >=, !=, ==)
while 1==1:
    print("ciclo")
# para interumpir la ejecución d código se usa (CTRL + C)

# Ciclos controlados por un contador (i, k)

i=0
k=0

while i<10:
    print("ciclo")
    #Importante modificar el valor del contador
    i+=1
    
#ciclos controlados por el valor de una variable

import random

a=0
while a!=5:
    a=random.randint(1,10)
    print(a)
print("se acabó")