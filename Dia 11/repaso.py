#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def abrirArchivo():
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)

continuar = ("no")
while continuar.lower() == "no":

    print("################")
    print("## PLATAFORMA DE GESTION ##")
    print("################")
    print("")

    print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes:\n2.Modificar estudiante:\n3.Crear estudiantes:\n4.Eliminar estudiantes:\n5.Salir\n")
    x=int(input("¿Qué opción deseas ejecutar?\n"))

    miInfo=[]
    if(x==1):
        miInfo=abrirArchivo()

        pregunta = "si"
        while pregunta.lower() == "si":

            for i in miInfo:
                for estudiante in i["estudiantes"]:

                    print("################")
                    print("ID:",estudiante["id"])
                    print("Nombre:",estudiante["nombre"])
                    print("Apellido:",estudiante["apellido"])
                    print("Edad",estudiante["edad"])
                    print("Fecha de Nacimiento (DD-MM-AAAA):",estudiante["fechaNacimiento"])
                    print("Cédula:",estudiante["cedula"])
                    print("E-mail:",estudiante["email"])
                    print("GitHub:",estudiante["github"])
                    print("################")
                    print("")
            
            pregunta = input("¿Deseas ver la lista de estudiantes nuevamente? ")

    elif(x==2):

        miInfo=abrirArchivo()
        contador = 0

        for i in miInfo:
            contador = contador +1
            for estudiante in i["estudiantes"]:
                contador = contador + 1
                print("################")
                print(" ESTUDIANTE #", contador)
                print("ID:",estudiante["id"])
                print("Nombre:",estudiante["nombre"])
                print("Apellido:",estudiante["apellido"])
                print("Edad",estudiante["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",estudiante["fechaNacimiento"])
                print("Cédula:",estudiante["cedula"])
                print("E-mail:",estudiante["email"])
                print("GitHub:",estudiante["github"])
                print("################")
                print("")
            contador = 0
        

        opcion = "si"
        while opcion.lower() == "si":

            index = int(input("¿En qué índice se encuentra el estudiante? "))

            if index == 0:
                estudiante = int(input("Cual numero de identificacion vas a cambiar? "))
                datoCambiar=int(input("Que te gustaría cambiar del estudiante:\n1.ID:\n2.Nombre:\n3.Apellido:\n4.Edad:\n5.Fecha de nacimiento:\n6.Cédula:\n7.Email:\n8.GitHub:\n "))
                
                if (datoCambiar==1):
                    nuevoId = int(input("Ingresa el nuevo ID :"))
                    miInfo[0]["estudiantes"][estudiante-1]["id"] = nuevoId
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")
                
                if (datoCambiar==2):
                    nuevoNombre = input("Ingresa el nuevo nombre:")
                    miInfo[0]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==3):
                    nuevoApellido = input("Ingresa el nuevo apellido :")
                    miInfo[0]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==4):
                    nuevaEdad = int(input("Ingresa la nueva edad :"))
                    miInfo[0]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==5):
                    nuevaFN = input("Ingresa la nueva fecha de nacimiento:")
                    miInfo[0]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevaFN
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==6):
                    nuevoCC = input("Ingresa el nuevo número de cédula:")
                    miInfo[0]["estudiantes"][estudiante-1]["cedula"] = nuevoCC
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==7):
                    nuevoEmail = input("Ingresa el nuevo E-mail:")
                    miInfo[0]["estudiantes"][estudiante-1]["email"] = nuevoEmail
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==8):
                    nuevoGit = input("Ingresa el nuevo GitHub:")
                    miInfo[0]["estudiantes"][estudiante-1]["github"] = nuevoGit
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")
                    
                miInfo=abrirArchivo()
                contador = 0
                for i in miInfo:
                    for estudiante in i["estudiantes"]:
                        contador = contador +1
                        print("################")
                        print(" ESTUDIANTE #",contador)
                        print("ID:",estudiante["id"])
                        print("Nombre:",estudiante["nombre"])
                        print("Apellido:",estudiante["apellido"])
                        print("Edad",estudiante["edad"])
                        print("Fecha de Nacimiento (DD-MM-AAAA):",estudiante["fechaNacimiento"])
                        print("Cédula:",estudiante["cedula"])
                        print("E-mail:",estudiante["email"])
                        print("GitHub:",estudiante["github"])
                        print("################")
                        print("")
                contador = 0

            if index == 1:

                estudiante = int(input("Cual numero de identificacion vas a cambiar? "))
                datoCambiar=int(input("Que te gustaría cambiar del estudiante:\n1.ID:\n2.Nombre:\n3.Apellido:\n4.Edad:\n5.Fecha de nacimiento:\n6.Cédula:\n7.Email:\n8.GitHub:\n "))
                
                if (datoCambiar==1):
                    nuevoId = int(input("Ingresa el nuevo ID :"))
                    miInfo[1]["estudiantes"][estudiante-1]["id"] = nuevoId
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")
                
                if (datoCambiar==2):
                    nuevoNombre = input("Ingresa el nuevo nombre:")
                    miInfo[1]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==3):
                    nuevoApellido = input("Ingresa el nuevo apellido :")
                    miInfo[1]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==4):
                    nuevaEdad = int(input("Ingresa la nueva edad :"))
                    miInfo[1]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==5):
                    nuevaFN = input("Ingresa la nueva fecha de nacimiento:")
                    miInfo[1]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevaFN
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==6):
                    nuevoCC = input("Ingresa el nuevo número de cédula:")
                    miInfo[1]["estudiantes"][estudiante-1]["cedula"] = nuevoCC
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==7):
                    nuevoEmail = input("Ingresa el nuevo E-mail:")
                    miInfo[1]["estudiantes"][estudiante-1]["email"] = nuevoEmail
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                if (datoCambiar==8):
                    nuevoGit = input("Ingresa el nuevo GitHub:")
                    miInfo[1]["estudiantes"][estudiante-1]["github"] = nuevoGit
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")

                miInfo=abrirArchivo()
                contador = 0
                for i in miInfo:
                    for estudiante in i["estudiantes"]:
                        contador = contador +1
                        print("################")
                        print(" ESTUDIANTE #",contador)
                        print("ID:",estudiante["id"])
                        print("Nombre:",estudiante["nombre"])
                        print("Apellido:",estudiante["apellido"])
                        print("Edad",estudiante["edad"])
                        print("Fecha de Nacimiento (DD-MM-AAAA):",estudiante["fechaNacimiento"])
                        print("Cédula:",estudiante["cedula"])
                        print("E-mail:",estudiante["email"])
                        print("GitHub:",estudiante["github"])
                        print("################")
                        print("")
                contador = 0

            opcion = input("¿Deseas actualizar otro dato? ")

    elif (x==3):

        miInfo = abrirArchivo()


        pregunta = "si"
        while pregunta.lower() == "si":

            index = int(input("¿En qué grupo desea ingresar al estudiante? (0:T2/1:P1) "))

            if 0 <= index < len(miInfo):

                Crear = {}
                Crear["id"] = int(input("Ingrese el ID del nuevo estudiante: "))
                

                Crear["nombre"] = str(input("Ingrese el nombre del nuevo estudiante: "))
                

                Crear["apellido"] = str(input("Ingrese el apellido del nuevo estudiante: "))
                

                Crear["edad"] = int(input("Ingrese la edad del nuevo estudiante: "))
                

                Crear["fechaNacimiento"] = str(input("Ingrese la fecha de nacimiento del nuevo estudiante (DD-MM-AAAA): "))
                

                Crear["cedula"] = int(input("Ingrese el número de cédula del nuevo estudiante: "))
                

                Crear["email"] = str(input("Ingrese el correo electrónico del nuevo estudiante: "))
                

                Crear["github"] = str(input("Ingrese el github del nuevo estudiante: "))
                
                miInfo[index]["estudiantes"].append(Crear)
                guardarArchivo(miInfo)
                print("Creación exitosa")
            
            else:
                print("El índice ingresado no es válido")

            pregunta = input("¿Deseas registrar otro estudiante? ")

    elif (x==4):

        miInfo = abrirArchivo()

        pregunta = "si"
        while pregunta.lower() == "si":

            index = int(input("¿En qué grupo se encuentra el estudiante que desea borrar? (0:T2/1:P1) "))

            if 0 <= index < len(miInfo):
                
                borrar = int(input("Ingrese el ID del estudiante que quiere borrar: "))

                for estudiante in miInfo[index]["estudiantes"]:
                    if estudiante["id"] == borrar:
                        miInfo[index]["estudiantes"].remove(estudiante)
                        guardarArchivo(miInfo)
                        print("La eliminación del estudiante se realizó exitosamente")
                        break

                    else:
                        print("El ID ingresado no existe")

            pregunta = input("¿Desea eliminar otro estudiante? ")

    elif (x==5):

        continuar = input("¿Estás seguro que deseas terminar el programa? ")


#Desarrollado por Jesús Bustamante - PPT: 1258502
