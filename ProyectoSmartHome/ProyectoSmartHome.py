#Registrar un Usuario y una nueva habitación

print("A continuación le vamos a pedir que dijite su Usuario")


print("Usuaríos: (1) Luis ")
print("Serian todos los usuarios")
print("Si desea registrar un nuevo Usuario digite(2)")

selección=int(input("Digite su elección: "))

#Registrar un nuevo usuario
if selección==2:
    print()
    usuario2=input("Digite su correo email: ")
    contraseña=int(input("Digite una contraseña numerica: "))
    print()
    print("Usuaríos: (1) Luis ")
    print("          (2)",usuario2)
    print("Si desea registrar un nuevo Usuario digite(3)")
    selección=int(input("Digite su usuario: "))

    if selección==1:
        print("Bienvenido de nuevo: Luis Miguel")
    elif selección==2:
        print()
        print("Bienvenido",usuario2)
        vContraseña=int(input("Digite su contraseña:"))

        #Despues de crear un nuevo usuario, ahora toca registrar una nueva habitación 
        if vContraseña==contraseña:
            print()
            print("Bienvenido de Nuevo",usuario2)
            habitacion1=int(input("Para registar una nueva habitación digite (1):"))

            if habitacion1==1:
                habitacion1=input("Digite el nombre de la habitación: ")
                print("Has registrado",habitacion1)
            

        else:
            print("Su contraseña es invalida")
            
    elif selección==3:
        print()
    usuario3=input("Digite su correo email: ")
    contraseña2=int(input("Digite una contraseña numerica: "))
    print()
    print("Usuaríos: (1) Luis ")
    print("          (2)",usuario2)
    print("          (3)",usuario3)
    print("Cantidad maxima de usuarios alcanzada")
    selección=int(input("Digite su usuario: "))


        

#Esto es parte del nuevo usuario
elif selección==1:
    print("Bienvenido de nuevo: Luis Miguel")

else:
    print("Su elección no es valida")

    


