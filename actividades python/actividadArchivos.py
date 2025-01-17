import json

# Datos proporcionados
datos = [
    ("72642413-6", "Comercial Calcetas Runner", 150000000),
    ("76437473-2","Reparación Mac",300000000),
    ("76254356-9","ProgramaSoftware",27500000),
    ("76077262-3","Calzados Roma",15000000),
    ("76310800-8","Empresa Arcos",80000000),
    ("76283690-4","Casino Coffe",120000000),
    ("76952985-5","Cafe Express ltda",50000000),
    ("76081440-2","Vino Export SA",20000000),
    ("76216579-1","Cepa Merl LTDA",30000000),
    ("76597875-0","Comercial Ropa America",60000000),
    ("76852106-3","Empresas JP",90000000),
    ("76887745-8","Empresas ICata SA",100000000),
    ("76210124-2","Buses Peñalolen",150000000),
    ("76802052-4","Sandias Paine LTDA",70000000),
    ("76575973-1","Modas Junior P",400000000),
    ("76869384-2","Bar del 81",25000000),
    ("76877803-6","Empresas LLS",8000000),
    ("76706124-0","Empresas luz y vida SA",3000000),
]

# Clasificación de empresas
clasificacion_empresas = []
for rut, nombre, ventas in datos:
    if ventas <= 100000000:
        clasificacion = "Pequeño Contribuyente"
    elif 100000001 <= ventas <= 200000000:
        clasificacion = "Mediano Contribuyente"
    else:
        clasificacion = "Gran Contribuyente"
    clasificacion_empresas.append({
        "RUT": rut,
        "Nombre": nombre,
        "Ventas": ventas,
        "Clasificacion": clasificacion
    })

# Crear archivo JSON
with open("segmentacionEmpresas.json", "w") as archivo_json:
    json.dump(clasificacion_empresas, archivo_json, indent=4)

print("Archivo 'segmentacionEmpresas.json' creado exitosamente.")
