""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. """
for i in range(101):
    print(i)

""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene. """
num = int(input("Ingrese un número entero: "))
count = len(str(num))
print(f"El número {num} tiene {count} dígitos.")

""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores. """
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
total = sum(range(num1 + 1, num2)) 
print(f"La suma de los números entre {num1} y {num2} es {total}.")

""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0. """
total = 0
while True:
    num = int(input("Ingrese un número entero (0 para terminar): "))
    if num == 0:
        break
    total += num
print(f"Total acumulado: {total}")

""" 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. """
import random
intentos = 1
num = random.randint(0,9)
while True:
    numUsuario = int(input("Adivina un número entre 0 y 9: "))
    if numUsuario == num:
        print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Intenta de nuevo.\n")
        intentos += 1

""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente. """
for i in range(100, -1, -2):
    print(i)
    i = i - 2

""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario. """
num = int(input("Ingresa un numero: "))
cont = 0
for i in range(0, num +1):
    cont = cont + i
print(cont)

""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio). """
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(0, 100):
    num = int(input("Ingresa un numero: "))
    if num % 2 == 0:
        pares +=1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    else:
        negativos +=1
print("******************")
print(f"Pares: {pares},\nImpares: {impares}, \nPositivos: {positivos}, \nNegativos: {negativos}")

""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor). """
media = 0
total = 0
for i in range(0, 100):
    num = int(input("Ingresa un numero: "))
    total += num
    media = total / (i + 1)
print(f"La media es: {media}")

""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. """
num = int(input("Ingresa un numero: "))
invertido = str(num)[::-1]
print(f"El número invertido es: {invertido}")