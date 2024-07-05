def validar_lista_numeros():
    while True:
        try:
            entrada = input("Ingresa una lista de números enteros separados por espacios: ")
            numeros = [int(num) for num in entrada.split()]
            return numeros
        except ValueError:
            print("Error: Ingresa solo números enteros válidos. Inténtalo nuevamente.")

def clasificar_numeros(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

# Solicitar la lista de números al usuario
numeros_ingresados = validar_lista_numeros()

# Clasificar los números
numeros_pares, numeros_impares = clasificar_numeros(numeros_ingresados)

# Mostrar los resultados
print("Números pares:", numeros_pares)
print("Números impares:", numeros_impares)
