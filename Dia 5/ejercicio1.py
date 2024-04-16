def parejas(a, n, k):

    pares = set()
    count = 0
 
    # check for all possible pairs
    for i in range(n):
        for b in range(i + 1, n):
            if (a[i] + a[b]) % k == 0:
                par = (a[i], a[b])

                if par not in pares:
                    pares.add(par)
                    count += 1
    return count

#Leer número de casos
T = int(input(""))
assert T < 100, "T debe ser menor que 100"

for case in range (1, T + 1):
    # Leer cantidad de enteros y número divisor
    n, k = map(int, input("").split())
    assert 1 < n < 100001, "n debe estar en el rango (1, 100001)"
    
    assert 0 < k < 501, "k debe estar en el rango (0, 501)"

    # Leer la lista de enteros
    a = list(map(int, input("").split()))
    assert all(abs(ai) < 10000001 for ai in a), "|a| debe ser menor que 10000001 para cualquier i"

    # Llamar a la función y mostrar el resultado
    resultado = parejas(a, n, k)
    print(f"case {case}: {resultado}")