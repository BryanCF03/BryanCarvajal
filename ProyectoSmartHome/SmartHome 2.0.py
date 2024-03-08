cerrarApp = 0
salirBlucle = 0
def compararNombres():
    while True:
        if h1 == h2 or h1 == h3 or h1 == h4 or h1 == h5 or h2 == h3 or h2 == h4 or h2 == h5 or h3 == h4 or h3 == h5 or h4 == h5:
            print("El nombre ya existe, Pruebe con otro")
            print()
            break
        else:
            global salirBlucle
            print("Cambiaste el nombre de la habitacion")
            print()
            salirBlucle += 1
            break
            
#Estas Variables solo sirven para guardar datos
h1 = "Habitación 1"
Disp1h1 = "Dispositivo 1"
Disp2h1 = "Dispositivo 2"
Disp3h1 = "Dispositivo 3"
Disp4h1 = "Dispositivo 4"
h2 = "Habitación 2"
Disp1h2 = "Dispositivo 1"
Disp2h2 = "Dispositivo 2"
Disp3h2 = "Dispositivo 3"
Disp4h2 = "Dispositivo 4"
h3 = "Habitación 3"
Disp1h3 = "Dispositivo 1"
Disp2h3 = "Dispositivo 2"
Disp3h3 = "Dispositivo 3"
Disp4h3 = "Dispositivo 4"
h4 = "Habitación 4"
Disp1h4 = "Dispositivo 1"
Disp2h4 = "Dispositivo 2"
Disp3h4 = "Dispositivo 3"
Disp4h4 = "Dispositivo 4"
h5 = "Habitación 5"
Disp1h5 = "Dispositivo 1"
Disp2h5 = "Dispositivo 2"
Disp3h5 = "Dispositivo 3"
Disp4h5 = "Dispositivo 4"

while True:
    if cerrarApp == 1:
        cerrarApp -=1
        break
    else:
        print("=========================================")
        print("Bienvenido a SmartHome")
        print()
        print("Menu de Opciones:")
        print("1.Registrar nuevo usuario\n2.Salir")

        selección=int(input("Digite su elección: "))
        #Registrar Un Nuevo Usuario
        if selección == 1:
            print()
            u1=input("Registre el nombre de Usuario: ")
            clave=input("Registre una contraseña: ")
            print()
            print("Has registrado un nuevo usuario!")
            print()
            while True:
                print("=========================================")
                print("Bienvenido a SmartHome")
                print()
                print("Menu de Opciones:")
                print("1.Ingresar con usuario existente\n2.Registrar nuevo usuario\n3.Salir")
        
                selección=int(input("Digite su elección: "))
        
                if selección == 1:           #Verificación de contraseña Usuario 1(u1)
                    correo = 0
                    contraseña = 0
                    while u1 != correo or clave != contraseña:
                        print()
                        print(f"Usuarios disponibles:\n-{u1}")
                        print()
                        correo=input("Digite su Usuario: ")
                        contraseña=input("Digite su contraseña: ")
                        if correo == u1 and contraseña == clave:
                            while True:
                                print("=========================================") #Ingreso a app con Usuario 1(u1)
                                print("Bienvenido",u1)
                                print()
                                print("Menu de opciones:")
                                print("1.Menu de Habitaciones.\n2.Salir de este Usuario.")
        
                                elección=int(input("Digite su elección: "))
                                print()
                                if elección == 1: #Menu de Habitaciones
                                    while True:
                                        print("=========================================")
                                        print("Menu de habitaciones")
                                        print()
                                        print(f"1.{h1}\n2.{h2}\n3.{h3}\n4.{h4}\n5.{h5}\n\n6.Salir del Menu de habitaciones")
                                        print()
                                        eleccion = int(input("Digite su elección:"))
                                        print()

                                        if eleccion == 1:
                                                while True:
                                                    print("Estás en",h1)
                                                    print()
                                                    print(f"1.Menu de dispositivos\n2.Cambiar Nombre de {h1}\n3.Salir de {h1}")
                                                    print()
                                                    eleccionHab = int(input("Digite su elección: "))
                                                
                                                    if eleccionHab == 1:
                                                        while True:
                                                            print("Menu de Dispositivos")
                                                            print()
                                                            print(f"1.{Disp1h1}\n2.{Disp2h1}\n3.{Disp3h1}\n4.{Disp4h1}\n5.Salir del menú de dispositivos")
                                                            print()
                                                            break #Este break es solo para que no tire error, para continuar el código se elimina.
                                                    
                                                    elif eleccionHab == 2:
                                                        while True:
                                                            h1=input("Digite el nuevo nombre para esta Habitación: ")
                                                            print()
                                                            compararNombres()
                                                            if salirBlucle == 1:
                                                                salirBlucle -= 1
                                                                break
                                                        
                                                    elif eleccionHab == 3:
                                                        print()
                                                        print("Saliste de",h1)
                                                        print()
                                                        break
                                                        
                                                    else:
                                                        print()
                                                        print("Elección Invalida, Pruebe otra vez")
                                                        print()

                                        if eleccion == 2:
                                            while True:
                                                    print("Estás en",h2)
                                                    print()
                                                    print(f"1.Menu de dispositivos\n2.Cambiar Nombre de {h2}\n3.Salir de {h2}")
                                                    print()
                                                    eleccionHab = int(input("Digite su elección: "))
                                                
                                                    if eleccionHab == 1:
                                                        while True:
                                                            print("Menu de Dispositivos")
                                                            print()
                                                            print(f"1.{Disp1h2}\n2.{Disp2h2}\n3.{Disp3h2}\n4.{Disp4h2}\n5.Salir del menú de dispositivos")
                                                            print()
                                                            break #Este break es solo para que no tire error, para continuar el código se elimina.
                                                    
                                                    elif eleccionHab == 2:
                                                        while True:
                                                            h2=input("Digite el nuevo nombre para esta Habitación: ")
                                                            print()
                                                            compararNombres()
                                                            if salirBlucle == 1:
                                                                salirBlucle -= 1
                                                                break
                                                        
                                                    elif eleccionHab == 3:
                                                        print()
                                                        print("Saliste de",h2)
                                                        print()
                                                        break
                                                        
                                                    else:
                                                        print()
                                                        print("Elección Invalida, Pruebe otra vez")
                                                        print()
                                               
                                        if eleccion == 3:
                                                while True:
                                                    print("Estás en",h3)
                                                    print()
                                                    print(f"1.Menu de dispositivos\n2.Cambiar Nombre de {h3}\n3.Salir de {h3}")
                                                    print()
                                                    eleccionHab = int(input("Digite su elección: "))
                                                
                                                    if eleccionHab == 1:
                                                        while True:
                                                            print("Menu de Dispositivos")
                                                            print()
                                                            print(f"1.{Disp1h3}\n2.{Disp2h3}\n3.{Disp3h3}\n4.{Disp4h3}\n5.Salir del menú de dispositivos")
                                                            print()
                                                            break #Este break es solo para que no tire error, para continuar el código se elimina.
                                                    
                                                    elif eleccionHab == 2:
                                                        while True:
                                                            h3=input("Digite el nuevo nombre para esta Habitación: ")
                                                            print()
                                                            compararNombres()
                                                            if salirBlucle == 1:
                                                                salirBlucle -= 1
                                                                break
                                                        
                                                    elif eleccionHab == 3:
                                                        print()
                                                        print("Saliste de",h3)
                                                        print()
                                                        break
                                                        
                                                    else:
                                                        print()
                                                        print("Elección Invalida, Pruebe otra vez")
                                                        print()
                                                        
                                        if eleccion == 4:
                                            while True:
                                                    print("Estás en",h4)
                                                    print()
                                                    print(f"1.Menu de dispositivos\n2.Cambiar Nombre de {h4}\n3.Salir de {h4}")
                                                    print()
                                                    eleccionHab = int(input("Digite su elección: "))
                                                
                                                    if eleccionHab == 1:
                                                        while True:
                                                            print("Menu de Dispositivos")
                                                            print()
                                                            print(f"1.{Disp1h4}\n2.{Disp2h4}\n3.{Disp3h4}\n4.{Disp4h4}\n5.Salir del menú de dispositivos")
                                                            print()
                                                            break #Este break es solo para que no tire error, para continuar el código se elimina.
                                                    
                                                    elif eleccionHab == 2:
                                                        while True:
                                                            h4=input("Digite el nuevo nombre para esta Habitación: ")
                                                            print()
                                                            compararNombres()
                                                            if salirBlucle == 1:
                                                                salirBlucle -= 1
                                                                break
                                                        
                                                    elif eleccionHab == 3:
                                                        print()
                                                        print("Saliste de",h4)
                                                        print()
                                                        break
                                                        
                                                    else:
                                                        print()
                                                        print("Elección Invalida, Pruebe otra vez")
                                                        print()
                                                        
                                        if eleccion == 5:
                                            while True:
                                                    print("Estás en",h5)
                                                    print()
                                                    print(f"1.Menu de dispositivos\n2.Cambiar Nombre de {h5}\n3.Salir de {h5}")
                                                    print()
                                                    eleccionHab = int(input("Digite su elección: "))
                                                
                                                    if eleccionHab == 1:
                                                        while True:
                                                            print("Menu de Dispositivos")
                                                            print()
                                                            print(f"1.{Disp1h5}\n2.{Disp2h5}\n3.{Disp3h5}\n4.{Disp4h5}\n5.Salir del menú de dispositivos")
                                                            print()
                                                            break #Este break es solo para que no tire error, para continuar el código se elimina.
                                                    
                                                    elif eleccionHab == 2:
                                                        while True:
                                                            h5=input("Digite el nuevo nombre para esta Habitación: ")
                                                            print()
                                                            compararNombres()
                                                            if salirBlucle == 1:
                                                                salirBlucle -= 1
                                                                break
                                                        
                                                    elif eleccionHab == 3:
                                                        print()
                                                        print("Saliste de",h5)
                                                        print()
                                                        break
                                                        
                                                    else:
                                                        print()
                                                        print("Elección Invalida, Pruebe otra vez")
                                                        print()
                                                        
                                        elif eleccion == 6:
                                            print()
                                            print("Has salido de el Menu de Habitaciones")
                                            print()
                                            break

            
                                       
                                elif elección == 2:
                                    print()
                                    print("Saliste del usuario",u1)
                                    print()
                                    break
                                else:
                                    print("Algo salio mal, intente otra vez")
        
                        
                        else: #Aqui ya es fuera del Usuario 1 {1}
                            print("Algo salio mal, intente otra vez")
        
                elif selección == 2:
                    u2=input("Registre su correo email: ")
                    clave2=input("Registre una contraseña: ")
                    print()
                    print("Has registrado un nuevo usuario!")
                    print()
                    print("Menu de Opciones:")
                    print("1.Ingresar con usuario existente\n2.Registrar nuevo usuario\n3.Salir")
                    cerrarApp += 1
                    break
        
                elif selección == 3:
                    print()
                    print("Gracias por ingresar")
                    cerrarApp += 1
                    break
        
                else:
                    print()
                    print("Elección invalida, pruebe otra vez")
                    print()
        
        elif selección == 2:
            print()
            print("Gracias por ingresar")
            break
            
        else:
            print()
            print("Elección invalida, pruebe otra vez")
            print()
