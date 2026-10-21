def extrae_pares(lista):
    """
    Esta función recibe una lista de números y devuelve una nueva lista que contiene solo los números pares.

    :param lista: Lista de números
    :return: Lista de números pares
    """
    return [num for num in lista if num % 2 == 0]


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = extrae_pares(lista_numeros)
print(f"Números pares extraídos: {numeros_pares}")
