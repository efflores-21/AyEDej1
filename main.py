# Ejercicio 1: Una escuela de educación primaria requiere un algoritmo que muestre los datos de los estudiantes de un salón de clase ordenados de forma ascendente, según un parámetro indicado; este parámetro puede ser cualquiera de los siguientes campos: carnet, nombres, apellidos, peso, estatura, sexo, promedio.
# Grupo: Elias Flores, Carlos Acuña, Harvey Gonzalez
# Version 1.0

from estudiante import Estudiante  # Importa la clase Estudiante desde el módulo estudiante
from lista_enlazada import ListaEnlazada  # Importa la clase ListaEnlazada desde el módulo lista_enlazada

def main():
    # Crear lista de estudiantes
    lista = ListaEnlazada()  # Se inicializa una lista enlazada para almacenar objetos de tipo Estudiante

    # Agregar algunos estudiantes
    # Se crean instancias de Estudiante y se agregan a la lista enlazada
    lista.agregar(Estudiante("A001", "Carlos", "López", 50, 1.5, "M", 85))
    lista.agregar(Estudiante("A003", "Ana", "Martínez", 48, 1.4, "F", 92))
    lista.agregar(Estudiante("A002", "Luis", "Gómez", 55, 1.6, "M", 78))
    lista.agregar(Estudiante("A004", "María", "Pérez", 45, 1.45, "F", 88))

    # Imprimir la lista original de estudiantes
    print("Lista original:")
    lista.imprimir_lista()  # Método para mostrar los elementos de la lista enlazada

    # Solicitar al usuario el campo por el cual desea ordenar la lista
    print("\nCampos disponibles: carnet, nombres, apellidos, peso, estatura, sexo, promedio")
    campo = input("Ingrese el campo por el cual desea ordenar: ").strip().lower()  # Se obtiene el campo de ordenamiento

    # Ordenar la lista enlazada por el campo especificado
    lista.ordenar_por_campo(campo)  # Método que ordena la lista enlazada según el campo ingresado

    # Imprimir la lista ordenada
    print("\nLista ordenada por", campo, ":")
    lista.imprimir_lista()  # Se muestra la lista enlazada ordenada

# Punto de entrada del programa
if __name__ == "__main__":
    main()  # Llama a la función principal