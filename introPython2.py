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
    
# ciclos controlados por el valor de una variable

import random

a=0
while a!=5:
    a=random.randint(1,10)
    print(a)
print("se acabó")

# Ciclos controlados por un evento

a=0

while 1==1:
    a=int(input("Ingrese un número"))
    
    if a==10:
        break
    
# FOR: se usa para recorrer un "iterable"
# List, tupla, diccionario...

# Lista: conjunto de variables orgaizadas en
# espacios consecutivos de memoria. Alas que se
# les asigna un único nombre. Se diferencian por 
# la posición que ocupan respecto al primer 
# elemento de la lista

miLista1=[1,True,"Textos",3.89]
miLista2=[]

# Todo en python es un objeto
# Tiene atributos y comportamientos

print(miLista1)

miLista.sort()

print(miLista1)

# Función len() cuenta los elementos de un iterable

print(len(miLista1))

# Tupla: lista inmutable

miTupla=(2,45,6,8,9,10)

# for: ciclo para recorrer iterables. El cuerpo del for
# se repite tantas veces como elementos tenga el iterable.
# En cada 

miLista=[5,45,89,6,7]

# estructura de for en Python
# for variable_donde_guardo_el_elemento in iterable:

for x in miLista:
    print(x)
    break

for x in miLista:
    if x>50:
        print("Grande")
        
# si solo utilizo el iterable para definir la cantidad de repeticiones
# entonces no es necesaria la variable 

for _ in miLista:
    print
    
# Si no tengo un iterable puedo uasr la función range() para generar una
# secuencia de números

for x in range(-10,10):
    print (x)
    
# imprimiría desde -10, hasta 9
# range() incluye el primer número pero no el segundo

# Taller crear un programa que pida un número al usuario y:
# 1. Números impares entre -número y número
# 2. Números primos entre número 0 y número*100
# El programa debe garantizar que el usuario ingrese un numero>0

