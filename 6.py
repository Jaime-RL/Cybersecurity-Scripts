def tabla_de_multiplicar(n):
    """
    Esta función genera la tabla de multiplicar del número n.

    :param n: El número del cual se quiere generar la tabla de multiplicar.
    :return: Una lista con la tabla de multiplicar del número n.
    """

    tabla = []
    for i in range(1, 11):
        tabla.append(n * i)

    return tabla


n = 7
tabla = tabla_de_multiplicar(n)
print(f"Tabla de multiplicar del {n}:")
i = 1w
for valor in tabla:
    print(f"{n}x{i}={valor}")
    i += 1
