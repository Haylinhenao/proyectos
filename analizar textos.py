# Ejercicio: analisis de texto

def analizar_texto(texto):
    """ funcion que realiza un analisis basico de un texto."""
    #contar lineas
    lineas = texto.splitlines()
    num_lineas = len(lineas)

    #contar palabras
    palabras = texto.split()
    num_palabras = len(palabras)

    #contar caracteres (incluyendo espacios)
    num_caracteres = len(texto)

    #Encontrar la palabra mas larga y la palabra mas corta
    palabras_sin_puntuacion = [palabra.strip('.,!?()[]{}"\'') for palabra in palabras]
    palabras_sin_vacios = [palabra for palabra in palabras_sin_puntuacion if palabra] #Eliminar palabras vacias
    palabra_mas_larga = max(palabras_sin_vacios, key=len)
    palabra_mas_corta = min(palabras_sin_vacios, key=len)

    #mostrar resultados
    print(f"analisis del texto ingresado:")
    print(f"numero de lineas: {num_lineas}")
    print(f"Número de palabras: {num_palabras}")
    print(f"numero de caracteres (incluyendo espacios): {num_caracteres}")
    print(f"palabra mas larga: '{palabra_mas_larga}' (longitud: {len(palabra_mas_larga)})")
    print(f"palabra mas corta: '{palabra_mas_corta}' (longitud: {len(palabra_mas_corta)})")

#pedir al usuario que ingrese un texto
texto_usuario = input("ingresa un texto para analizar: ")

#llamar a la funcion para analizar el texto ingresado
analizar_texto(texto_usuario)