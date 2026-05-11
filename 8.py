def es_contraseña_valida(contraseña):
    """
    Verifica si una contraseña es válida según las siguientes reglas:
    1. Debe tener al menos 8 caracteres.
    2. Debe contener al menos una letra mayúscula.
    3. Debe contener al menos una letra minúscula.
    4. Debe contener al menos un dígito.
    5. No debe contener espacios en blanco.

    Args:
        contraseña (str): La contraseña a verificar.

    Returns:
        bool: True si la contraseña es válida, False en caso contrario.
    """
    # Verificar si la contraseña tiene al menos 8 caracteres
    tiene_longitud_valida = len(contraseña) >= 8

    # Verificar si la contraseña contiene al menos una letra mayúscula
    tiene_mayuscula = any(caracter.isupper() for caracter in contraseña)

    # Verificar si la contraseña contiene al menos una letra minúscula
    tiene_minuscula = any(caracter.islower() for caracter in contraseña)

    # Verificar si la contraseña contiene al menos un dígito
    tiene_digito = any(caracter.isdigit() for caracter in contraseña)

    # Verificar si la contraseña no contiene espacios en blanco
    no_tiene_espacios = " " not in contraseña

    # Retornar True si todas las condiciones son cumplidas
    return tiene_longitud_valida and tiene_mayuscula and tiene_minuscula and tiene_digito and no_tiene_espacios
