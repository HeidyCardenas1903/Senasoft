#1.Cree un modulo con todas las operaciones matemáticas, luego impórtela en un archivo.py y realice las operaciones matemáticas llamando a cada función.
import operaciones_matematicas

resultado_suma = operaciones_matematicas.suma(10, 5)
print("Suma:", resultado_suma)

resultado_resta = operaciones_matematicas.resta(10, 5)
print("Resta:", resultado_resta)

resultado_multiplicacion = operaciones_matematicas.multiplicacion(10, 5)
print("Multiplicación:", resultado_multiplicacion)

try:
    resultado_division = operaciones_matematicas.division(10, 5)
    print("División:", resultado_division)
except ValueError as e:
    print(e)
