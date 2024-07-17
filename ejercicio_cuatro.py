"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""
# Diccionario con registros de un alumno
alumno = {
    1: {"nombre": "Juan", "edad": 20},
    2: {"nombre": "Maria", "edad": 22}
}

# Función para imprimir los registros del alumno
def imprimir_registros():
    for key, value in alumno.items():
        print(f"Registro {key}: Nombre: {value['nombre']}, Edad: {value['edad']}")

# Función para editar el campo 'nombre' de un registro del alumno
def editar_nombre_registro(id_registro, nuevo_nombre):
    if id_registro in alumno:
        alumno[id_registro]["nombre"] = nuevo_nombre
        print(f"Nombre del registro {id_registro} actualizado correctamente.")
    else:
        print("El registro no existe en el diccionario.")

# Ejemplo de uso de las funciones
imprimir_registros()
editar_nombre_registro(1, "Pedro")
imprimir_registros()
