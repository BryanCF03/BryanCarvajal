while True:

    print("Bienvenido a SmartHome")
    print()
    print("Menu de Opciones:")
    print("1.Registrar nuevo usuario\n2.Salir")

    selección=int(input("Digite su elección: "))
    #Registrar Un Nuevo Usuario
    if selección == 1:
        u1=input("Registre su correo email: ")
        clave=input("Registre una contraseña: ")
        print()
        print("Has registrado un nuevo usuario!")
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
                    print("=======================================================================") #Ingreso a app con Usuario 1(u1)
                    print("Bienvenido",u1)
                    print()
                    print("Menu de opciones:")
                    print("1.Menu de Habitaciones.\n2.Salir del Programa.")

                    elección=int(input("Digite su elección: "))
                    print()
                    if elección == 1:
                        print("Menu de Habitaciones:")
                        print()
                        print("1.Registrar una Nueva Habitación.") #Registrar una Nueva Habitación para Usuario 1(u1)

                        elección=int(input("Digite su elección: "))
                        print()
                        if elección == 1:
                            H1=input("Digite el nombre de la Nueva habitación:")
                            print()
                            print("Has registrado una nueva habitación")
                            print()
                            print("Menu de opciones:")
                            print("1.Menu de habitaciones.\n2.Salir del Programa.")

                            elección=int(input("Dijite su elección: "))

                            if elección == 1:
                                print("Menu de Habitaciones:")
                                print()
                                print(f"1.{H1}\n2.Registrar una Nueva Habitación.")
                                #Agregar mas Habitaciones

                            elif eleción == 2:
                                print()
                                print("Gracias por Ingresar")
                                break
                           
                    elif elección == 2:
                        print()
                        print("Gracias por Ingresar")
                        break
                    else:
                        print("Algo salio mal, intente otra vez")

                
                else:
                    print("Algo salio mal, intente otra vez")

        elif selección == 2:
            u2=input("Registre su correo email: ")
            clave2=input("Registre una contraseña: ")
            print()
            print("Has registrado un nuevo usuario!")
            print()
            print("Menu de Opciones:")
            print("1.Ingresar con usuario existente\n2.Registrar nuevo usuario\n3.Salir")
            break

        elif selección == 3:
            print()
            print("Gracias por ingresar")
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
        break

