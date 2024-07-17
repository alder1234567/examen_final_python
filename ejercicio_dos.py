"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_numeros_primos(lista):
    return list(filter(es_primo, lista))

# Ejemplo de uso
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_primos = filtrar_numeros_primos(numeros)
print(numeros_primos)