""" 1) Dado el diccionario precios_frutas, Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800 """

precios_frutas["Banana"] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. """

frutas = precios_frutas.keys()
print(frutas)

""" 4) Escribí un programa que permita almacenar y consultar números telefónicos. Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
Luego, pedí un nombre y mostrale el número asociado, si existe."""

contactos = {
    "Matias" : 1122334455,
    "Emma" : 1144556677,
    "Bauti" : 1188779944,
    "Mauricio" : 1163524174,
    "Antonia" : 1178965412
}
print(contactos["Emma"])

""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra. """

frase = input("Ingrese una frase: ").lower()
palabras = frase.split(" ")
palabrasUnicas = set(palabras)
cantidadPalabras = {}
for palabra in palabras:
    cantidadPalabras[palabra] = cantidadPalabras.get(palabra, 0) + 1

print(f"Palabras unicas: ")
for palabra in palabrasUnicas:
    print(f"{palabra}")
print(f"Cantidad de apariciones de las palabras: ")
for palabra, cantidad in cantidadPalabras.items():
    print(f"{palabra}: {cantidad}")

""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. """

alumno1 = input("Ingrese el nombre del 1er alumno: ")
print("Ingrese sus notas...")
notasAlum1 = tuple(float(input(f"Ingrese nota {i+1}: "))for i in range (3))

alumno2 = input("Ingrese el nombre del 2do alumno: ")
print("Ingrese sus notas...")
notasAlum2 = tuple(float(input(f"Ingrese nota {i+1}: "))for i in range (3))

alumno3 = input("Ingrese el nombre del 3er alumno: ")
print("Ingrese sus notas...")
notasAlum3 = tuple(float(input(f"Ingrese nota {i+1}: "))for i in range (3))

alumnos = {
    alumno1 : notasAlum1,
    alumno2 : notasAlum2,
    alumno3 : notasAlum3
}

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

""" 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). """

parcial1 = {10, 11, 12, 13, 14 }
parcial2 = {13, 14, 16, 17, 10}

ambosParciales = parcial1 & parcial2
unParcial = parcial1 ^ parcial2
todosAprobados = parcial1 | parcial2

print("Aprobaron ambos parciales: ")
for alumno in ambosParciales:
    print(f"Alumno: ", alumno)
print("Aprobaron solo uno de los dos:")
for alumno in unParcial:
    print(f"Alumno: ", alumno)
print("Aprobaron al menos un parcial:")
for alumno in todosAprobados:
    print(f"Alumno: ", alumno)


""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe. """

productos = {
    "arroz" : 12,
    "azucar": 10,
    "yerba" : 5,
}
def admin():
    seleccion = int(input("Ingrese 0 para consultar un producto, 1 si desea agregar uno nuevo y 2 si desea modificar su stock: "))
    if seleccion == 0:
        producto = input("Que producto desea consultar: ").lower()
        return productos[producto]
    elif seleccion == 1 :
        nombre = input("Nombre del nuevo producto: ").lower()
        precio = int(input("Precio del nuevo producto: "))
        productos[nombre] = precio
        return productos
    elif seleccion == 2:
        nombre = input("Que producto modificas?: ").lower()
        precio = int(input("Nuevo precio: "))
        productos[nombre] = precio
        return productos
    else:
        print("Selecciona una opcion valida..")
        admin()

print(admin())

""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora. """

agenda = {
    ("13062025", "1400") : "parcial matematicas",
    ("14062025", "2000") : "parcial programación",
}

def consultarEvento(dia, hora):
    consulta = (dia, hora)
    for evento in agenda:
        if evento == consulta:
            return agenda[evento]
        else:
            return "No se encuentra el evento"
dia = input("Ingrese fecha del evento a consultar: (ddmmaa)")
hora = input("Ingrese hora del evento a consultar: (hhmm)")

print(consultarEvento(dia, hora))


""" 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores. """

paises = {
    "argentina" : "buenos aires",
    "brasil" : "brasilia",
    "chile" : "santiago"
}
capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais
print(capitales)