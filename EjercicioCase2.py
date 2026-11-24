name = []
lastName =[]
age = []
email = []
password = []
confirmPass = []
opcion = 0

while True:
    print("Bienvenido al sistema de registro de usuarios")
    print("---------MENÚ PRINCIPAL---------")
    print("1. Registrar usuario")
    print("2. Ver información del usuario")
    print("3. Borrar información del usuario")
    print ("4. Modificar información del usuario")
    print("5. Salir")
    print("---------------------------------")
    opcion = int(input("Selecciona una opción: "))

    match opcion:#Aquí inicia el match, que es una validación de caso
        
        case 1:
            name.append(input("Ingresa tu nombre: "))
            lastName.append(input("Ingresa tu apellido: "))
            age.append(int(input("Ingresa tu edad: ")))
            email.append(input("Ingresa tu correo electrónico: "))
            password.append(input("Ingresa tu contraseña: "))
            confirmPass.append(input("Confirma tu contraseña: "))
        case 2:
            print("Nombre:", name, "Edad:", age, "Correo electrónico:", email, "Contraseña:", password)
            for i in range(len(name)):
                print("Id:-", i," Con el nombre: ", name[i], " con el apellido: ", lastName[i], " Con la edad de: ", age[i])
        case 3:
            name = ""
            lastName = ""
            age = 0
            birthday = ""
            email = ""
            password = ""
        case 4:
            name.append(input("Ingresa tu nombre: "))
            lastName.append(input("Ingresa tu apellido: "))
            age.append(int(input("Ingresa tu edad: ")))
            email.append(input("Ingresa tu correo electrónico: "))
            password.append(input("Ingresa tu contraseña: "))
        case 5:
            print("¡Adios!")
            break
        case _:
            print("Opción no válida")