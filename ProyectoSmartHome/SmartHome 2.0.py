usuarios = {}
claves = {}
habitaciones = {}
dispositivos = {}
contadorUsu = 0
usuActual = 0
ingresoUsu = 0
HabUsuario = 0
cerraduras = {}
estados = ["abierto", "cerrado"]

def menuSmartHome():
    print("==============================")
    print("Bienvenido a SmartHome\n")
    print("Menu de Opciones.\n1.Ingresar con usuario existente.\n2.Registrar nuevo usuario.\n3.Salir.\n")

def menuUsuario(usu):
    print("==============================")
    print(f"Bienvenido a SmartHome {usuarios[usu]}\n") 
    print("Menu de Opciones.\n1.Menu de Habitaciones.\n2.Cambiar contraseña del usuario.\n3.Cerraduras.\n4.Salir de este Usuario.\n") 

def registrarUsuarios():
    global contadorUsu
    print()
    usuarios[contadorUsu] = input("Ingrese el nombre del nuevo usuario: ")
    claves[contadorUsu] = input("Ingrese una nueva contraseña para este usuario: ")
    print("\nHas registrado un nuevo Usuario")
    habitaciones[contadorUsu] = {}
    cerraduras[contadorUsu] = {}
    contadorUsu += 1

def imprimirUsuarios():
    print()
    for x in range(len(usuarios)):
        print(f"{x+1}. {usuarios[x]}")

def ingresarUsuario():
    global usuActual
    while True:
        print("==============================\nUsuarios disponibles:")
        imprimirUsuarios()
        eleccion2 = int(input("\nDigite el usuario a ingresar: "))
        usuActual = eleccion2-1
        verifiContraUsua()
        return usuActual

def verifiContraUsua():
    correo = ""
    contraseña = ""
    while usuarios[usuActual] != correo or claves[usuActual] != contraseña:
        correo=input("\nDigite su Usuario: ")
        contraseña=input("Digite su contraseña: ")
        if correo == usuarios[usuActual] and contraseña == claves[usuActual]:
            return
        else:
            print("\nContraseña o Usuario incorrecto, Pruebe otra vez")

def menuHabitaciones():
    global HabUsuario
    print("===============================")
    print(f"Menu de habitaciones, De: {usuarios[usuActual]}\n")
    if len(habitaciones[usuActual]) >= 1:
        imprimirHab()
    else:
        print("No has registrado Habitaciones")
    print(f"\n1. Ingresar a habitación. \n2. Registrar nuevas habitaciones.\n3. Salir.\n")

def menuHabitacionActual():
    print("============================")
    print(f"Menu de habitación: {habitaciones[usuActual][eleccion5-1]['nombre']}\n")
    if habitaciones[usuActual][eleccion5-1]['conteoDisp'] >= 1:
        imprimirDisp()
    else:
        print("No has registrado dispositivos.")
    print("\n1. Registrar Nuevo dispositivo.\n2. Ingresar a un dispositivo.\n3. Salir.")

def registarDispocitivo():
    print("============================")
    dispositivo = input("Ingrese el nombre del dispositivo a agregar: ")
    estadoDisp = int(input("1.Encendido.  2.Apagado. Seleccione (1/2): "))
    if estadoDisp == 1:
        estadoDisp = "Encendido"
    elif estadoDisp == 2:
        estadoDisp = "Apagado"
    habitacionActual = habitaciones[usuActual][eleccion5-1]['nombre']
    dispo1 = habitaciones[usuActual][eleccion5-1]['conteoDisp']
    dispositivos[(usuActual, habitacionActual, dispo1)] = {"NombreDisp": dispositivo, "EstadoDisp": estadoDisp}
    print(f"Dispositivo '{dispositivo}' agregado a la habitación '{habitacionActual}'.")
    habitaciones[usuActual][eleccion5-1]['conteoDisp'] += 1

def imprimirHab():
    for i, habitacion in habitaciones[usuActual].items():
        print(f"{i+1}. {habitacion['nombre']}")

def imprimirDisp():
    habitacionActual = habitaciones[usuActual][eleccion5-1]['nombre']
    dispositivosHabitacion = [(key, disp) for key, disp in dispositivos.items() if key[0] == usuActual and key[1] == habitacionActual]
    if dispositivosHabitacion:
        for i, (_, dispositivo) in enumerate(dispositivosHabitacion):
            print(f"{i+1}. {dispositivo['NombreDisp']}: {dispositivo['EstadoDisp']}")
    else:
        print("No hay dispositivos registrados en esta habitación.")

def menuDispocitivos():
    print("============================")
    print("Menu del dispositivo:", dispositivos[(usuActual, habitaciones[usuActual][eleccion5-1]['nombre'], eleccion7-1)]["NombreDisp"])
    print("Estado:", dispositivos[(usuActual, habitaciones[usuActual][eleccion5-1]['nombre'], eleccion7-1)]["EstadoDisp"])
    print("\n1.Cambiar estado del dispositivo.\n2.Salir.")

def registrarHab():
    NewHab = input("Digite el nombre de la nueva habitación: ")
    if NewHab not in habitaciones[usuActual]:
        habitaciones[usuActual][len(habitaciones[usuActual])] = {'nombre': NewHab, 'conteoDisp': 0}
    else:
        print("La habitación ya existe.")

def cambiarEstadoDisp():
    dispositi = (usuActual, habitaciones[usuActual][eleccion5-1]["nombre"], eleccion7-1)
    if dispositivos[dispositi]["EstadoDisp"] == "Encendido":
        dispositivos[dispositi]["EstadoDisp"] = "Apagado" 
        print("Cambiaste el estado a Apagado")
    elif dispositivos[dispositi]["EstadoDisp"] == "Apagado":
        dispositivos[dispositi]["EstadoDisp"] = "Encendido"
        print("Cambiaste el estado a Encendido")
    return dispositivos[dispositi]["EstadoDisp"]

def cambioContra():
    a = ""
    b = ""
    c = claves[usuActual]
    while b != claves[usuActual]:
        claves[usuActual] = c
        print("============================")
        b = input("Digite su contraseña actual: ")
        print()
        if b == claves[usuActual]:
            claves[usuActual] = input("\nDigite la nueva contraseña: ")
            a = input("Vuelva a digitar la nueva contraseña: ")
            if claves[usuActual] == a:
                print("\nLa contraseña se cambió con éxito\n")
                return claves[usuActual]
            else:
                print("\nLas contraseñas no coinciden, Pruebe de nuevo\n")
        else:
            print("Contraseña incorrecta, Pruebe otra vez\n")

def menuCerraduras():
    print("============================")
    print("Menú de Cerraduras\n")
    print("Cerraduras registradas:")
    print()
    if cerraduras[usuActual]:
        for cerradura, i in cerraduras[usuActual].items():
            print(f"- {cerradura}: {i['estado']}")
    else:
        print("No hay cerraduras registradas.")
    print("\nMenu de opciones.\n1. Registrar cerradura.\n2. Cambiar estado de cerradura.\n3. Eliminar cerradura.\n4. Salir.")
    eleccion = int(input("\nSeleccione una opción: "))
    return eleccion

def registarCerradura():
    print("============================")
    nombre = input("Ingrese el nombre de la nueva cerradura: ")
    if nombre not in cerraduras[usuActual]:
        clave = input("Digite una clave para esta cerradura: ")
        cerraduras[usuActual][nombre] = {"estado": "Indefinido", "clave": clave}
    else:
        print("La cerradura ya existe.")

def cambiarEstadoCerradura():
    print("============================")
    nombre = input("Ingrese el nombre de la cerradura: ")
    if usuActual in cerraduras and nombre in cerraduras[usuActual]:
        claveCerradura = cerraduras[usuActual][nombre]["clave"]
        clave = input("Ingrese la clave de la cerradura: ")
        if clave == claveCerradura:
            if cerraduras[usuActual][nombre]["estado"] == "Indefinido":
                nuevoEstado = input(f"\nIngrese el nuevo estado ({'/'.join(estados)}): ").lower()
                if nuevoEstado in estados:
                    nuevoEstado = nuevoEstado.capitalize()
                    cerraduras[usuActual][nombre]["estado"] = nuevoEstado
                    print(f"\nEstado de la cerradura '{nombre}' cambiado a '{nuevoEstado}'.")
                else:
                    print("Estado no válido. Por favor, ingrese 'Abierto' o 'Cerrado'.")
            elif cerraduras[usuActual][nombre]["estado"] == "Abierto":
                cerraduras[usuActual][nombre]["estado"] = estados[1]
                print(f"El estado de la cerradura {nombre} cambio a",estados[1])
            elif cerraduras[usuActual][nombre]["estado"] == "cerrado":
                cerraduras[usuActual][nombre]["estado"] = estados[0]
                print(f"El estado de la cerradura {nombre} cambio a",estados[0])
        else:
            print("Contraseña Incorrecta.")
    else:
        print(f"No se encontró la cerradura '{nombre}' o el usuario no tiene cerraduras registradas.")

def eliminarCerradura():
    print("============================")
    nombre = input("Ingrese el nombre de la cerradura a eliminar: ")
    if nombre in cerraduras[usuActual]:
        del cerraduras[usuActual][nombre]
        print(f"\nLa crradura {nombre} ha sido eliminada.")
    else:
        print(f"No se encontró la cerradura '{nombre}'.")

while True:
    menuSmartHome()
    eleccion1 = int(input("Digite su elección: "))
    if eleccion1 == 1:
        if contadorUsu >= 1:
            usuActual = ingresarUsuario()
            ingresoUsu = 1
            if ingresoUsu == 1:
                ingresoUsu -= 1
                while True:
                    menuUsuario(usuActual)
                    eleccion3 = int(input("Digite su elección: "))
                    if eleccion3 == 1:
                        while True:
                            menuHabitaciones()
                            eleccion4 = int(input("Digite su elección: "))
                            if eleccion4 == 1:
                                imprimirHab()
                                eleccion5 = int(input("Digite la habitacion a entrar: "))
                                if eleccion5 >= len(habitaciones[usuActual])+1:
                                    print("Eleccion Invalida")
                                else:
                                    while True:
                                        menuHabitacionActual()
                                        eleccion6 = int(input("Digite su elección: "))
                                        if eleccion6 == 1:
                                            registarDispocitivo()
                                        elif eleccion6 == 2:
                                            print("============================")
                                            imprimirDisp()
                                            eleccion7 = int(input("\nDigite el dispositivo a ingresar: "))
                                            if eleccion7-1 >= habitaciones[usuActual][eleccion5-1]['conteoDisp']:
                                                print("Dispositivo Inexistente")
                                            else:
                                                while True:
                                                    menuDispocitivos()
                                                    eleccion8 = int(input("Digite su elección: "))
                                                    if eleccion8 == 1:
                                                        cambiarEstadoDisp()
                                                    elif eleccion8 == 2:
                                                        print("Has salido del menu del dispositivo", dispositivos[(usuActual, habitaciones[usuActual][eleccion5-1]['nombre'], eleccion7-1)]["NombreDisp"])
                                                        break
                                                    else:
                                                        print("Elección Invalida.")
                                        elif eleccion6 == 3:
                                            print("Has salido de", habitaciones[usuActual][eleccion5-1]['nombre'])
                                            break
                                        else:
                                            print("Eleccion invalida.Prueve otra vez")
                            elif eleccion4 == 2:
                                registrarHab()
                            elif eleccion4 ==3:
                                print("Salió del menú de habitaciones")
                                break
                            else:
                                print("Elección Invalida")
                    elif eleccion3 == 2:
                        claves[usuActual] = cambioContra()
                    elif eleccion3 == 3:
                        while True:
                            opcion_cerraduras = menuCerraduras()
                            if opcion_cerraduras == 1:
                                registarCerradura()
                            elif opcion_cerraduras == 2:
                                cambiarEstadoCerradura()
                            elif opcion_cerraduras == 3:
                                eliminarCerradura()
                            elif opcion_cerraduras == 4:
                                print("\nSalió del menú de cerraduras")
                                break
                            else:
                                print("\nElección inválida.")
                    elif eleccion3 == 4:
                        print(f"Salió del usuario {usuarios[usuActual]}")
                        break
                    else:
                        print("Opción inválida")
            else:
                print("No ingresó a ningún usuario.\n")
        else:
            print("\nNo hay usuarios registrados\n")
    elif eleccion1 == 2:
        registrarUsuarios()
    elif eleccion1 == 3:
        print("=====================================")
        print("Gracias por ingresar a SmartHome.")
        break
    else:
        print("\nElección Invalida, Pruebe otra vez")
