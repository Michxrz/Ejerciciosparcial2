nombre = ""
edad = 0
nacionalidad = ""

nombre = input ("ingresa tu nombre: ")
edad = int(input ("ingresa tu edad: "))
nacionalidad = input("ingresa tu nacionalidad: ")

if edad >= 18: #el if va seguido de la condicion y dos puntos
    print("Eres mayor de edad")
else:# else va seguido de dos puntos para decir que se hace si no se cumple la condicion del if
    print("No eres mayor de edad")

if nacionalidad == "N":
    print("Eres de nacionalidad mexicana")
else:
    print("No eres de nacionalidad mexicana")