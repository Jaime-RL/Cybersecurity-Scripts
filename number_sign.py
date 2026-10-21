try:
    num = int(input("Introduce un número: "))
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
except ValueError:
    print("Por favor, introduce un número válido.")
