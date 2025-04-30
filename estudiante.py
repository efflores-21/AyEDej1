class Estudiante:
    def __init__(self, carnet, nombres, apellidos, peso, estatura, sexo, promedio):
        # Inicializa un objeto Estudiante con los atributos proporcionados
        self.carnet = carnet  # Identificador único del estudiante
        self.nombres = nombres  # Nombres del estudiante
        self.apellidos = apellidos  # Apellidos del estudiante
        self.peso = peso  # Peso del estudiante en kilogramos
        self.estatura = estatura  # Estatura del estudiante en metros
        self.sexo = sexo  # Sexo del estudiante (M/F)
        self.promedio = promedio  # Promedio académico del estudiante

    def __str__(self):
        # Representación en forma de cadena del objeto Estudiante
        return (f"Carnet: {self.carnet}, Nombre: {self.nombres} {self.apellidos}, "
                f"Peso: {self.peso}kg, Estatura: {self.estatura}m, Sexo: {self.sexo}, Promedio: {self.promedio}")