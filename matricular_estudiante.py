from agregar_estudiante import*
from modelsdata import*
from limpiar_pantalla import*
def matricular_estudiante():
    agregar_alumno()
    limpiar_pantalla()
    id = input('ingrese el id a mostrar: ')
    alumnos = campus.get(id,{})
    print("rutas disponibles: ")
    print('seleccione una ruta a matricular: ')
    opc=list(rutas.keys())
    for i, opcion in enumerate(opc, start=1):
        print(f'{i}. {opcion}')
    while True:
        try:
            opcion = int(input('ingrese un numero de la ruta: '))-1
            rutas.get(opc,-1)
            if 0 <= opcion < len(opc):
                break
            else:
                print("⚠️ Número fuera de rango. Intente nuevamente.")
        except ValueError:
            print("⚠️ Ingrese un número válido.")

        ruta = {
            'nombre_ruta': opc[opcion],
            'skills' : {}
        }
        alumnos.update({'ruta':ruta})
        print(campus)   

    print("✅ Matriculado correctamente.")