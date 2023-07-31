#1. Cree un fichero y ábralo en modo escritura, luego asigne un texto a una variable e insértelo en el fichero. Por último, visualice el documento.txt si fue escrito correctamente.

with open("documento.txt", "w") as archivo:
    texto_a_insertar = "Este es el texto que se va a insertar en el archivo."
    archivo.write(texto_a_insertar)

with open("documento.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
