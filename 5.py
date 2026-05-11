def es_palindromo(entrada):
    # Convertir la entrada a cadena, minúsculas y eliminar espacios
    entrada = str(entrada).lower().replace(" ", "")

    # Comparar la entrada con su reverso usando un bucle
    reverso = ""
    for caracter in entrada:
        reverso = caracter + reverso
    return entrada == reverso


entrada = "Anita lava la tina"
resultado = es_palindromo(entrada)
print(f"¿Es '{entrada}' un palíndromo? {resultado}")
