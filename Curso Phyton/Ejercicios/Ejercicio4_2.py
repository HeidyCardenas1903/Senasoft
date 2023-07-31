#2. Serialice un diccionario utilizando el método dump. El archivo una vez serializado debe mostrarnos un mensaje que nos diga que no se puede abrir.
import pickle
datos = {
    "nombre": "Juan",
    "edad": 30,
    "profesion": "Ingeniero"
}
with open("datos.pkl", "wb") as archivo:
    pickle.dump(datos, archivo)

try:
    with open("datos.pkl", "rb") as archivo_leido:
        contenido = pickle.load(archivo_leido)
        print("El archivo se ha abierto correctamente.")
except FileNotFoundError:
    print("No se pudo abrir el archivo.")