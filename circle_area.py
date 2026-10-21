import math


def area_circulo(radio):
    pi = math.pi
    area = pi * radio**2
    return area


radio = 5
area = area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area}")
