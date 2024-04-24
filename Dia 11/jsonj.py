import json

# Ruta al archivo JSON
archivo_json = "largefile.json"

# Abre y lee el archivo JSON
with open(archivo_json, encoding="utf-8") as archivo:
    datos_json = json.load(archivo)

if datos_json:
    print("-----------EVENTOS-------------")
    for i, evento in enumerate(datos_json,1):
        print(f"{i}. {evento["type"]} - {evento["id"]}")

def obtener_id(id_busqueda):
    datos = datos_json
    for evento in datos:
        if evento['id'] == id_busqueda:
            return evento
    return None

print("---------------MENÚ---------------")
print("")
print("1. Leer un evento existente")
print("2. Crear un uevo evento")
print("3. Actualizar un evento existente")
print("4. Eliminar un evento existente")
print("5. Salir")
print("")



    

id_busqueda = input("Ingrese la ID del elemento que desea leer: ")

evento = obtener_id(id_busqueda)

if evento:
    print("Elemento encontrado:", evento)
else:
    print("No se encontró ningún elemento con esa ID.")




