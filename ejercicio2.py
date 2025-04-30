# Implementa un método llamado “ordena” que reciba una pila de enteros como parámetro y devuelva la pila ordenada de mayor (fondo de la pila) a menor (top de la pila).

def ordena(pila):
    # Extraer todos los elementos
    elementos = []
    while pila:
        elementos.append(pila.pop())
    
    # Ordenar de mayor a menor
    elementos.sort(reverse=True)

    # Volver a apilar (mayor al fondo, menor al tope)
    resultado = []
    for elem in elementos:
        resultado.append(elem)
    
    return resultado


# Prueba del método
pila = [1, 3, 2, 4]
resultado = ordena(pila.copy())  # .copy() para no modificar la original
print("Resultado:", resultado)
