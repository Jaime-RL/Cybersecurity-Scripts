def contador_elementos(lista):
    """
    Cuenta cuántas veces aparece cada elemento de una lista usando un diccionario.

    :param lista: La lista cuyos elementos se quieren contar.
    :return: Diccionario {elemento: número de apariciones}.
    """

    hashmap = {}
    for elemento in lista:
        if elemento in hashmap:
            hashmap[elemento] += 1
        else:
            hashmap[elemento] = 1

    return hashmap


lista_numeros = [1, 2, 2, 3, 4, 4, 4, 5]
contador = contador_elementos(lista_numeros)
print(f"Contador de elementos: {contador}")
