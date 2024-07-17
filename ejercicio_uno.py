"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""
def encontrar_minimo_maximo(lista):
    minimo = min(lista)
    maximo = max(lista)
    return {'menor': minimo, 'mayor': maximo}

# uso de dato
datos = encontrar_minimo_maximo([5, 10, 3, 8, 15])
print(datos)