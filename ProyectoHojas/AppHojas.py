# 
from tkinter import *

# Creación de la función que se encargará de calcular el precio total y el recibo de una venta
def calcular_total(nombre, tipo_cliente, cantidad, precio_por_hoja):
    descuentos = {1: 0.05, 2: 0.08, 3: 0.12, 4: 0.15}

    if tipo_cliente in descuentos:
        descuento = descuentos[tipo_cliente]
    else:
        descuento = 0.0

    subtotal = cantidad * precio_por_hoja
    neto_por_pagar = subtotal * (1 - descuento)

    return subtotal, neto_por_pagar

def imprimir_recibo(nombre, subtotal, neto_por_pagar):
    print("Nombre del cliente:", nombre)
    print("Subtotal por pagar:", subtotal)
    print("Neto por pagar:", neto_por_pagar)

# App
root =Tk()
root.title("App || Hojas de hielo")
root.iconbitmap("C:\\Users\\hvcar\\OneDrive\\Documentos\\PRACTICAS\\SENASOFT\\ProyectoHojas\\bolsa-de-hielo.ico\\")

nombre = StringVar()
tipo_de_cliente = StringVar()
cantidad = StringVar()
precio_por_hoja = StringVar()
calcular_total = StringVar()
imprimir_recibo = StringVar()

nombre_label = Label(text="Nombre del cliente: ")
nombre_label.grid(row=0, column=0)
nombre_entry = Entry(textvariable=nombre)
nombre_entry.grid(row=0, column=1)

cantidad_label = Label(text="Cantidad de hojas: ")
cantidad_label.grid(row=2, column=0)
cantidad_entry = Entry(textvariable=cantidad)
cantidad_entry.grid(row=2, column=1)

precio_por_hoja_label = Label(text="Precio por hoja: ")
precio_por_hoja_label.grid(row=3, column=0)
precio_por_hoja_entry = Entry(textvariable=precio_por_hoja)
precio_por_hoja_entry.grid(row=3, column=1)

# Botones
boton1 = Button(text="Calcular total", command=calcular_total)
boton1.grid(row=4, column=0)

boton2 = Button(text="Imprimir recibo", command=imprimir_recibo)
boton2.grid(row=4, column=1)

# Estilo
root.config(bg="#B6FCFA")
nombre_label.config(bg="#B6FCFA")
cantidad_label.config(bg="#B6FCFA")
precio_por_hoja_label.config(bg="#B6FCFA")

root.mainloop()