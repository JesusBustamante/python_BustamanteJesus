Fruticas = [("Mora",0.33,23),("Melón",5.5,5),("Melocotón",0.73,9)]

mayusculas = [fruta.upper() for fruta, precio, cantidad in Fruticas] 
print(mayusculas)

precioMenor = [fruta for fruta, precio, cantidad in Fruticas if precio < 0.50] 
print(precioMenor)

cantidadMayor=max(Fruticas, key=lambda x: x[2]); print(cantidadMayor) 

Fruticas.sort(key=lambda fruta: fruta[1] * fruta[2], reverse=True) 
for fruta in Fruticas:
    nombre, precio, cantidad = fruta
    print(f"Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}, Valor en stock: {precio * cantidad}")