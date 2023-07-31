#1.Cree un modulo con todas las operaciones matemáticas, luego impórtela en un archivo.py y realice las operaciones matemáticas llamando a cada función.
def suma(a,b):
    return a + b

def resta(a,b):
    return a -b

def division(a,b):
    if b==0:
        raise ValueError('No es posible dividir entre cero :c')

def multiplicacion(a,b):
    return a * b

