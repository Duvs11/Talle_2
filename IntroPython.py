# Comentario de una linea 
# Todo lo que va después es ignorado por el interprete de python
# Interprete de pyton

# Variables: Espacio de memoria, con nombre, donde guardo valores
# Los nombres de variables deben ser cortos, descriptivos, SIN ESPACIOS
# EN BLANCO ni carácteres especiales, no deben empezar con un número

# Descriptivo significa que representa la categoría del dato que quiero guardar

# En python las variables pueden contener cualquier dato de tipo primitivo
# números (entero, reales), cadenas de carácteres (string), booleanos (true, false)
#carácteres (letras)

variable = 1
variable = 'Juventud divino tesoro te vas para no volver...'
variable = True
variable = 'a'
variable = 3.1415926535

# para asignar un valor a una variable se usa el operador =

# Operadore: Es un mecanismo para obtener un dato a partir de otros datos
# Los datos que intervienen se llaman operandos
# Aritmeticos: (+)(-)(*)(/)(%)
# Comparación: Retornan True o False (<)(>)(<=)(>=)(==)(!=)
# Lógica booleana: OR AND, retornan True o False deacuerdo a una tabla de verdad
# Los operandos siempre son booleanos

a = True
b = False

print(a and b)

# Los operadores booleanos y de comparación son usados para definir condiciones

# Estrucutras de control de código
# En general un programa se ejecuta de manera secuencial
# Sepuede romper esa secuencialidad 
# Empleando un conjunto de sentencias (Expresiones) que permite:
# 1. Seleccionar la ejecución de un bloque de código
# 2. Repetir la ejecucuón de un bloque de código
# 3. Seleccionar entre ejecutar un bloque de código u otro bloque de código
# De esa manera "romper" la secuencialidad

# Principios del paradigma de programación estructurado

# Sentencia if, si se cumple una condición (se evalua cómo True)
# Se ejecuta un bloque de código

print("Linea 1")
print("Linea 2")

# 1.
if 5>3:
    print("Esto se muestra si la condición es verdadera")

# 2.    
if 5>8 or 3<7:
    print("Esto se muestra si la condición es verdadera")
    
# 3.
if 5>8 or 3<7:
    print("Esto se muestra si la condición es verdadera")
else: 
    print("Esto se muestra si la condición es falsa")
    
# mmm
entrada = int(input("cuantos años tiene??"))

if entrada<18:
    print("Es menor de edad")
else:
    print("Es mayor de edad")

# Taller: Crear un programa en python que genere un número aleatrorio entre 1 y 12
# Si el número es 7 imprimir Ganó
# Si el número es iprimr deje el juego