def separar_par_impar(pila):
    pares = []
    impares = []

    # Clasificar los elementos en pares e impares
    while pila:
        num = pila.pop()
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    # Reconstruir la pila: primero los pares (al fondo), luego los impares
    resultado = []

    while pares:
        resultado.append(pares.pop())

    while impares:
        resultado.append(impares.pop())

    return resultado


# Prueba del método
pila = [2, 3, 6, 8, 11, 13, 18, 21]
resultado = separar_par_impar(pila.copy())  # .copy() para no modificar la original
print("Resultado:", resultado)
