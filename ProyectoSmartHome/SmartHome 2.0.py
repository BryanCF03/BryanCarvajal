usuarios = {}
claves = {}
habitaciones_usuarios = {}
conteo_usuarios = 0
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
    print("Menu de Opciones:\n\n1.Menu de Habitaciones.\n2.Cambiar contraseña del usuario.\n3.Cerraduras.\n4.Salir de este Usuario.\n") 

def registrarUsuarios():
    global conteo_usuarios
    print()
    usuarios[conteo_usuarios] = input("Ingrese el nombre del nuevo usuario: ")
    claves[conteo_usuarios] = input("Ingrese una nueva contraseña para este usuario: ")
    habitaciones_usuarios[conteo_usuarios] = {}
    cerraduras[conteo_usuarios] = {}
    conteo_usuarios += 1

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
    if len(habitaciones_usuarios[usuActual]) >= 1:
        imprimirHab()
    else:
        print("No has registrado Habitaciones")
    print(f"\n1. Ingresar a habitación. \n2. Registrar nuevas habitaciones.\n3. Salir.\n")

def imprimirHab():
    for i in range(len(habitaciones_usuarios[usuActual])):
        print(f"{i+1}. {habitaciones_usuarios[usuActual][i]}.")

def registrarHab():
    NewHab = input("Digite el nombre de la nueva habitación: ")
    if NewHab not in habitaciones_usuarios[usuActual]:
        habitaciones_usuarios[usuActual][len(habitaciones_usuarios[usuActual])] = NewHab
    else:
        print("La habitación ya existe.")

def cambioContra():
    a = ""
    b = ""
    c = claves[usuActual]
    while b != claves[usuActual]:
        claves[usuActual] = c
        b = input("Digite su contraseña actual: ")
        print()
        if b == claves[usuActual]:
            claves[usuActual] = input("Digite la nueva contraseña: ")
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
    if cerraduras[usuActual]:
        for cerradura, info in cerraduras[usuActual].items():
            print(f"- {cerradura}: {info['estado']}")
    else:
        print("No hay cerraduras registradas.")
    print("\nOpciones:\n1. Registrar cerradura.\n2. Cambiar estado de cerradura.\n3. Eliminar cerradura.\n4. Salir.")
    eleccion = int(input("\nSeleccione una opción: "))
    return eleccion

def registarCerradura():
    nombre = input("Ingrese el nombre de la nueva cerradura: ")
    if nombre not in cerraduras[usuActual]:
        clave = input("Digite una clave para esta cerradura: ")
        cerraduras[usuActual][nombre] = {"estado": "Indefinido", "clave": clave}
    else:
        print("La cerradura ya existe.")

def cambiarEstadoCerradura():
    nombre = input("Ingrese el nombre de la cerradura: ")
    if usuActual in cerraduras and nombre in cerraduras[usuActual]:
        clave_cerradura = cerraduras[usuActual][nombre]["clave"]
        codigo = input("Ingrese la clave de la cerradura: ")
        if codigo == clave_cerradura:
            if cerraduras[usuActual][nombre]["estado"] == "Indefinido":
                nuevo_estado = input(f"Ingrese el nuevo estado ({'/'.join(estados)}): ").lower()
                if nuevo_estado in estados:
                    nuevo_estado = nuevo_estado.capitalize()
                    cerraduras[usuActual][nombre]["estado"] = nuevo_estado
                    print(f"Estado de la cerradura '{nombre}' cambiado a '{nuevo_estado}'.")
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
    nombre = input("Ingrese el nombre de la cerradura a eliminar: ")
    if nombre in cerraduras[usuActual]:
        del cerraduras[usuActual][nombre]
        print(f"Cerradura '{nombre}' ha sido eliminada.")
    else:
        print(f"No se encontró la cerradura '{nombre}'.")

while True:
    menuSmartHome()
    eleccion1 = int(input("Digite su elección: "))
    if eleccion1 == 1:
        if conteo_usuarios >= 1:
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
                                if eleccion5 >= len(habitaciones_usuarios[usuActual])+1:
                                    print("Eleccion Invalida")
                                else:
                                    print("============================")
                                    print("Menu de habitación:",habitaciones_usuarios[usuActual][eleccion5-1])                     
                            
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
        print("Elección Invalida, Pruebe otra vez")
