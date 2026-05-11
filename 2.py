def encuentra_minimo(lista):
    """
    Encuentra el valor mínimo en una lista de números.

    :param lista: Lista de números
    :return: Valor mínimo en la lista
    """
    if not lista:
        return None  # Retorna None si la lista está vacía
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo


lista_numeros = [5, 3, 8, 1, 4]
minimo = encuentra_minimo(lista_numeros)
print(f"El número mínimo en la lista es: {minimo}")

minimo_directo = min(lista_numeros)
print(f"El número mínimo usando min() es: {minimo_directo}")
