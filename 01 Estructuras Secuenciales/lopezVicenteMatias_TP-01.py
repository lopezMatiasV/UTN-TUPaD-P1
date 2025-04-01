""" TP Estructuras Secuenciales """
""" Alumno: López Vicente Matias """

""" Actividad n°1 """
frase = "Hola Mundo!!"
print(frase)

""" Actividad n°2 """
nombre = input('Ingrese su nombre: ')
print("Hola " + nombre + "!!")

""" Actividad n°3 """
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print("Soy " + nombre, apellido + " tengo " + edad + " años y vivo en " + lugar)

""" Actividad n°4 """
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * radio ** 2
perimetro = 3.14 * radio
print("El área del círculo es de:", area)
print("El perimetro del círculo es de:", perimetro)

""" Actividad n°5 """
segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos / 60
print("Equivales a", horas, "horas")

""" Actividad n°6 """
num = int(input("Ingrese un número: "))

""" lista = range(num, num * 10+1, num)
print(lista) """

""" for i in range(1, 10+1):
    print(num * i) """

print("Tabla de multiplicar del número:", num, "\n", num * 1, "\n", num * 2, "\n", num * 3, "\n", num * 4, "\n", num * 5, "\n", num * 6, "\n", num * 7, "\n", num * 8, "\n", num * 9, "\n", num * 10)

""" Actividad n°7 """
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero, distinto al anterior y que no sea 0: "))

if num2 == num1:
    print("el segundo numero tiene que ser distinto!!")
elif num2 == 0:
    print("el segundo numero no puede ser 0!!")
else:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    print("Suma:", suma, "\nResta:", resta, "\nMultiplicacion:", multiplicacion, "\nDivision:", division)

""" Actividad n°8 """
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
masaCorporal = peso / altura
print(masaCorporal)

""" Actividad n°9 """
temperatura = float(input("Igrese los grados a calcular"))
aFahrenheit = 9/5 * temperatura + 32
print(aFahrenheit)

""" Actividad n°10 """
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese un ultimo número: "))
promedio = (num1 + num2 + num3) / 3
print(promedio)