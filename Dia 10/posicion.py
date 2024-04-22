
entrada = input("Ingrse los valores a enlistar: ")

arreglo = list(sorted(set(map(int, entrada.split(",")))))


objetivo = int(input("Ingrese el objetivo: "))




if objetivo in arreglo:  
    jesus = len(arreglo)     
    for i in range (0,jesus):     
        if objetivo == arreglo[i]:
            print(i)
            break


if objetivo not in arreglo:
    arreglo.append(objetivo)
    arreglo.sort()
    tamaño2 = len(arreglo)
    for i in range (0,tamaño2):        
            if objetivo == arreglo[i]:
                print(i)
                break

#Desarrollado por Jesus Bustamante PPT 1258502