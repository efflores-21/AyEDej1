# Diseñar un método “Convbinario” que reciba un entero como parámetro. La función, usando una pila, deberá mostrar el número en código binario.

def conv_binario(numero):
    if numero == 0:
        return [0]  # caso especial

    pila = []

    # Convertir a binario usando división entre 2
    while numero > 0:
        resto = numero % 2
        pila.append(resto)
        numero //= 2

    # Invertir la pila para obtener el binario correcto
    binario = []
    while pila:
        binario.append(pila.pop())

    return binario


# Prueba del método
numero = 12
resultado = conv_binario(numero)
print("Salida:", resultado)  # Salida: [1, 1, 0, 0]
