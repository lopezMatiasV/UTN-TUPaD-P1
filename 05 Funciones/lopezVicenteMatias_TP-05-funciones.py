""" 1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal. """

def imprimir_hola_mundo():
    return "Hola Mundo!"
#Programa Principal
""" print(imprimir_hola_mundo()) """

""" 2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario. """

def saludar_usuario(nombre):
    return f"Hola {nombre}"
#Programa Principal
""" nombre = input("Ingresa tu nombre: ")
print(saludar_usuario(nombre)) """

""" 3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
los datos al usuario y llamar a esta función con los valores ingresados. """

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
#Programa Principal
""" nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("ingrese su residencia: ")
print(informacion_personal(nombre, apellido, edad, residencia)) """

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_
circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados. """

import math
def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    return area
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro
#Programa principal
""" radio = float(input("Ingrese el radio del círculo: "))
print(f"El área de este círculo es: {calcular_area_circulo(radio)}")
print(f"El área de este círculo es: {calcular_perimetro_circulo(radio)}") """

""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función. """

def segundos_a_horas(segundos):
    horas = (segundos / 60) / 60
    return int(horas)
#Programa principal
""" segundos = int(input("Ingrese la cantidad de segundos: "))
print(segundos_a_horas(segundos)) """

""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función. """

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero * i)
#Programa principal
""" num = int(input("Ingrese un número: "))
tabla_multiplicar(num) """

""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
de forma clara. """

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    resultados = [suma, resta, multiplicacion, division]
    return resultados
#Programa principal
""" num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"Suma: {operaciones_basicas(num1, num2)[0]}")
print(f"Resta: {operaciones_basicas(num1, num2)[1]}")
print(f"Multiplicación: {operaciones_basicas(num1, num2)[2]}")
print(f"División: {operaciones_basicas(num1, num2)[3]}") """

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
para mostrar el resultado con dos decimales. """

def calular_imc(peso, altura):
    imc = peso/(altura**2)
    return round(imc, 2)
#Programa principal
""" peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
print(f"Su IMC es de: {calular_imc(peso, altura)}") """

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función. """

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
#Programa principal
""" celsius = float(input("Ingrese los grados a calcular: "))
print(f"{celsius}° celsius a fahrenheit es: {celsius_a_fahrenheit(celsius)}°.") """

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función. """
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return round(promedio, 2)
#Programa principal
a = float(input("Ingrese la 1ra nota: "))
b = float(input("Ingrese la 2da nota: "))
c = float(input("Ingrese la 3ra nota: "))
print(f"El promedio según las notas ingresadas es de: {calcular_promedio(a, b, c)}.")