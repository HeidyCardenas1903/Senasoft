# Cree una función de generar números pares de manera tradicional
def generar_pares_tradicional(n):
    pares = []
    for i in range(2, n+1, 2):
        pares.append(i)
    return pares

n = 20
pares_tradicionales = generar_pares_tradicional(n)
print(pares_tradicionales)

# Cree una función genera pares utilizando generadores.
def generar_pares_generador(n):
    for i in range(2, n+1, 2):
        yield i

n = 20
generador_pares = generar_pares_generador(n)
pares_generados = list(generador_pares)
print(pares_generados)

# Doble un numero utilizando map y función Lambda
numeros = [1, 2, 3, 4, 5]

numeros_doblados = list(map(lambda x: x * 4, numeros))
print(numeros_doblados)