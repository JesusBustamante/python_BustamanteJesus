import json

with open("largefile.json",encoding="utf-8") as openfile:
    miJSON = json.load(openfile)



def obtener_id(id_busqueda):
    datos = miJSON
    for evento in datos:
        if evento['id'] == id_busqueda:
            return evento
    return None


def crearEvento(NewID, NewType, NewActor, NewRepo):
    crearEventos= {
   
    'id': NewID,
    'type': NewType,
    'actor': NewActor,
    'repo': NewRepo
    }
    
    miJSON.append(crearEventos)
    return miJSON

with open("eventos.json","w") as outfile:
    json.dump(miJSON, outfile) 
    
print("---------------MENÚ---------------")
print("")
print("1. Leer un evento existente")
print("2. Crear un nuevo evento")
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


NewID = input("Ingrese el id del nuevo evento: ")
print("")
NewType = input("Ingrese el nuevo evento: ")
print("")
NewActor = input("Ingrese el id del nuevo actor: ")
print("")
NewRepo = input("Ingrese el id del nuevo repo: ")


miJSON = crearEvento(NewID, NewType, NewActor, NewRepo)

   
with open("eventos.json","w") as outfile:
    json.dump(miJSON,outfile)
    
# for i in range (len(miJSON)):
#     if(miJSON[i]['type']=='CreateEvent'):
#         crearEventos.append(miJSON[i])

#print(crearEventos[5]['actor']['id'])

# for q in range (5):
#     print("#######################")


