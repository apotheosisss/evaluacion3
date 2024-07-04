def registrar_reserva(reservas):
    nombre = input("Nombre y apellido del cliente: ")
    ciudad_origen = input("Ciudad de origen: ")
    detalle_tour = input("Detalle del tour (Torres del Paine, Carretera Austral o Chiloé): ")
    cantidad_personas = int(input("Cantidad de personas para el tour: "))
    reserva = {
        "nombre": nombre,
        "ciudad_origen": ciudad_origen,
        "detalle_tour": detalle_tour,
        "cantidad_personas": cantidad_personas
    }
    reservas.append(reserva)
    print("Reserva registrada exitosamente.")

def listar_reservas(reservas):
    print("\nListado de reservas:")
    for reserva in reservas:
        print(f"Cliente: {reserva['nombre']}, Ciudad de origen: {reserva['ciudad_origen']}, Detalle del tour: {reserva['detalle_tour']}, Personas: {reserva['cantidad_personas']}")

def imprimir_detalle_por_destino(reservas):
    destino = input("Selecciona un destino (Torres del Paine, Carretera Austral o Chiloé): ")
    nomarchivo = f"{destino}_reservas.txt"
    with open(nomarchivo, "w") as file:
        for reserva in reservas:
            if reserva["detalle_tour"].lower() == destino.lower():
                file.write(f"Cliente: {reserva['nombre']}, Ciudad de origen: {reserva['ciudad_origen']}, Personas: {reserva['cantidad_personas']}\n")
    print(f"Detalle de reservas para {destino} guardado en {nomarchivo}")

def principal():
    reservas = []
    while True:
        print("\n--- Menú ---")
        print("1. Registrar reserva")
        print("2. Listar todas las reservas")
        print("3. Imprimir detalle de reservas por destino")
        print("4. Salir del programa")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_reserva(reservas)
        elif opcion == "2":
            listar_reservas(reservas)
        elif opcion == "3":
            imprimir_detalle_por_destino(reservas)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")

if __name__ == "__main__":
    principal()

