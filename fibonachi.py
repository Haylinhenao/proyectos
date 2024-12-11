# Ejercicio: generador de secuencia de fibonacci

def fibonacci(hasta):
    """ Funcion que genera la secuencia de fibonacci hasta el numero 'hasta'. """
    secuencia = [0, 1] # los primeros dos numeros de fibonacci
    while secuencia[-1] + secuencia[-2] <= hasta:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

# pedir al usuario el numero limite para la secuencia de fibonacci
limite = int(input("Ingresa un numero para generar la secuencia de fibonacci hasta ese limite: "))

# obtener la secuencia de fibonacci hasta el limite dado por el usuario
secuencia_fibonacci = fibonacci(limite)

# imprime la secuencia obtenida
print("secuencia de fibonacci hasta", limite, ":")
print(secuencia_fibonacci)