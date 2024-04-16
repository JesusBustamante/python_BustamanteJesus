nodos = []
cantidad = int(input("¿Cuántos valores vas a ingresar? "))
assert 0 <= cantidad <= 300, "Error, escriba números en rango de 0 _ 300"

for i in range(0, cantidad):
    nodos.append(input("Ingrese los valores de la lista "))

duplicados = list(set(nodos))

duplicados.sort()
print(duplicados)