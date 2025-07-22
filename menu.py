from limpiar_pantalla import*
from agregar_estudiante import*
from matricular_estudiante import*
from 
MAIN_MENU =  """
======================
MENU PRINCIPAL
======================

1. AGREGAR ESTUDIANTE
2. MATRICULAR ESTUDIANTE
3. MOSTRAR INFORMACION
=======================

ingrese una opcion: 
"""



def main():
    while True:
        limpiar_pantalla()
        print(MAIN_MENU)
        opc = input(" = ")
        match opc:
            case "1":
                limpiar_pantalla()
                agregar_alumno()
                pausar_pantalla()
            case "2":
                limpiar_pantalla()
                matricular_estudiante()
                pausar_pantalla()
            case "3":
                limpiar_pantalla()
                add()
                pausar_pantalla()
                break
            case _:
                print("ERROR...")
                pausar_pantalla()

# Funcion principal
if __name__ == "__main__":
    main()