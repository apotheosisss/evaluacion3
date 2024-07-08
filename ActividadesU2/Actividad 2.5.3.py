#Ejercicio 2
sw=1
saldo = 500000
while True:
    print("-----MENÚ DE RETIRO------")
    print("1.- Ver mi saldo")
    print("2.- Retirar dinero")
    print("3.- Salir")
    op= input("Seleccione una opción (1-3: ")
    for op in range (1,3):
            if op==1:
                print(f"Su saldo es: {saldo}")
                r = int(input("Para volver atrás, presione 1. \n Para salir, presione 2. \n"))
                if r == 2:
                    print("Cierre de sesión exitoso, adiós.")
                    break
            elif op==2:
                print("Transferencia realizada")
                r= int(input("Para volver atrás, presione 1. Para salir, presione 2. \n"))
                if r == 2:
                    print("Cierre de sesión exitoso, adiós.")
                    break
            elif op==3:
                print("Cierre de sesión exitoso, adiós.")
                break
            else:
                print("Ingrese un valor válido. ")
           
   