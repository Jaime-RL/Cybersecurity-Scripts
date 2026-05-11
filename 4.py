def contador_elementos(lista):
    """
    Esta función cuenta la cantidad de elementos en una lista.

    :param lista: La lista de la cual se quiere contar los elementos.
    :return: La cantidad de elementos en la lista.
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
