def duplicados(nums, destino):

    # Crear un diccionario para guardar los números y sus índices
    indices = {}

    # Recorrer la lista de números
    for i, num in enumerate(nums):

        # Calcular el complemento del número actual para alcanzar el objetivo
        complemento = destino - num

        # Si el complemento está en el diccionario, hemos encontrado una solución
        if complemento in indices:
            return [indices[complemento], i]
        
        # Si no, añadir el número y su índice al diccionario
        indices[num] = i

    # Si no se encuentra ninguna solución, devolver una lista vacía
    return ["No se encontró solución"]

# Ejemplo de uso
nums = [2, 7, 11, 15]
destino = 22
print(duplicados(nums, destino))