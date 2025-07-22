from modelsdata import*
from limpiar_pantalla import*

def agregar_alumno():
    limpiar_pantalla
    
    alumno = alumnos.copy()
    id = input("Ingrese el id del alumno: ")
    alumno['nombre'] = input("Ingrese el nombre del alumno: ")
    alumno['edad'] = input("Ingrese la edad del alumno: ")
    alumno['email']  = input("Ingrese el email del alumno: ")
    alumno['telefono'] = input("Ingrese el telefono del alumno: ")
    campus.update({id: alumno})
    
def mostrar_alumnos():
    limpiar_pantalla
    print('\n Lista de Alumnos:')
    for id, alumno in campus.items():
        print(f"Id: {id} \nnombre: {alumno['nombre']}\nedad: {alumno['edad']}\nemail: {alumno['email']} \ntelefono: {alumno['telefono']}")