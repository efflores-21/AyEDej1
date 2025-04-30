from nodo import Nodo  # Importa la clase Nodo para construir la lista enlazada

class ListaEnlazada:
    def __init__(self):
        # Inicializa la lista enlazada con la cabeza como None
        self.cabeza = None

    def agregar(self, estudiante):
        # Agrega un nuevo nodo con un objeto Estudiante a la lista enlazada
        nuevo_nodo = Nodo(estudiante)
        if not self.cabeza:  # Si la lista está vacía, el nuevo nodo es la cabeza
            self.cabeza = nuevo_nodo
        else:
            # Recorre la lista hasta el último nodo y agrega el nuevo nodo al final
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        # Recorre la lista enlazada e imprime cada estudiante
        actual = self.cabeza
        while actual:
            print(actual.estudiante)  # Se asume que el objeto Estudiante tiene un método __str__ o similar
            actual = actual.siguiente

    def ordenar_por_campo(self, campo):
        # Convierte la lista enlazada en una lista normal para facilitar el ordenamiento
        estudiantes = []
        actual = self.cabeza
        while actual:
            estudiantes.append(actual.estudiante)  # Agrega cada estudiante a la lista
            actual = actual.siguiente

        # Verifica que el campo especificado existe en los objetos Estudiante
        if not hasattr(estudiantes[0], campo):
            print(f"Campo '{campo}' no encontrado en Estudiante.")  # Mensaje de error si el campo no existe
            return

        # Ordena la lista de estudiantes por el campo especificado
        estudiantes.sort(key=lambda est: getattr(est, campo))

        # Reconstruye la lista enlazada con los estudiantes ordenados
        self.cabeza = None  # Reinicia la lista enlazada
        for est in estudiantes:
            self.agregar(est)  # Agrega cada estudiante ordenado a la lista enlazada
