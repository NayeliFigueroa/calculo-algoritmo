# Definimos la función que esta representa en f(x) = 4x^2 - 2x + 1

def funcion(x):
    return 4 * x**2 - 2 * x + 1

# Luego definimos la función para calcular la derivada utilizando el método de diferencias finitas hacia adelante
def diferencia_finita_adelante(x, h):

    # aque implementamos la fórmula de diferencias finitas hacia adelante
    derivada = (funcion(x + h) - funcion(x)) / h
    return derivada

# este es punto en el que se desea calcular la derivada
x = 1

# Tamaño del paso (h)
h = 0.001

# Calcular la derivada usando diferencias finitas hacia adelante
derivada = diferencia_finita_adelante(x, h)

# Imprimir el resultado
print("f'(1) =", derivada)
