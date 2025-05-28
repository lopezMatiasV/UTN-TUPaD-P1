""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla
el factorial de todos los números enteros entre 1 y el número que indique el usuario """
def factorial(num):
    return 1 if (num == 0 or num == 1) else num * factorial(num - 1)

#Programa principal
num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    fact = factorial(i)
    print(f"El factorial de {i} es: {fact}")

""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie
completa hasta la posición que el usuario especifique. """
def finobacci(pos):
    return pos if pos <= 1 else finobacci(pos - 1) + finobacci(pos - 2)

#Programa principal
pos = int(input("Ingrese un número: "))
for i in range(1, pos + 1):
    print(finobacci(i))

""" 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). 
Prueba esta función en un algoritmo general. """

def potencia(base, exp):
    return 1 if exp == 0 else base *potencia(base, exp -1)

#Programa Principal
base = int(input("Ingrese el número base: "))
exp = int(input("Ingrese el número exponente: "))
print(potencia(base, exp))

""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como
una cadena de texto. 
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. Para convertir un número decimal a 
binario, se puede seguir este procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario."""

def aBinario(num):
    return str(num) if num <= 1 else aBinario(num // 2) + str(num % 2)

#Programa principal
num = int(input("Ingrese un numero: "))
print(aBinario(num))

""" 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True
si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed(). """

def esPalindromo(palabra):
    largo = len(palabra)
    if largo <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return esPalindromo(palabra[1 : -1])
    
#Programa Principal
palabra = input("Ingrese una palabra: ")
print(esPalindromo(palabra))

""" 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus
dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5) """

def sumadigitos(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sumadigitos(num // 10)

#Programa principal
num = int(input("Ingrese un número: "))
print(sumadigitos(num))
""" 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y 
así sucesivamente hasta llegar al último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita
para construir toda la pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1) """

def contarBloques(num):
    return 1 if num == 1 else num + contarBloques(num -1) 

#Programa Principal
num = int(input("Ingrese la cantidas de bloques de la base: "))
print(contarBloques(num))

""" 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito 
(entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3 
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0"""

def contarDigito(num, dig):
    if num == 0:
        return 0
    elif num % 10 == dig:
        return 1 + contarDigito(num // 10, dig)
    else:
        return contarDigito(num // 10, dig)

#Programa Principal
num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el dígito a buscar: "))
print(contarDigito(num, dig))