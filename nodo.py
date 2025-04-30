class Nodo:
    def __init__(self, estudiante):
        # Inicializa un nodo con un objeto Estudiante y un puntero al siguiente nodo
        self.estudiante = estudiante  # Contiene el objeto Estudiante asociado al nodo
        self.siguiente = None  # Puntero al siguiente nodo en la lista enlazada (inicia como None)