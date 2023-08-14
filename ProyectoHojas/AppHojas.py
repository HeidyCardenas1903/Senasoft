from tkinter import *
from sqlite3 import connect
import tkinter as tk

# # Creacion de la base de datos / Hojas - Heidy
# #Conexion :)
# conexion = connect("ventas.db")
# cursor = conexion.cursor()

# #Tabla de ventas
# cursor.execute('''
# CREATE TABLE ventas (
#   nombre text,
#   tipo int,
#   cantidad int,
#   precio_por_hoja float,
#   total float
# )
# ''')

#Creacion de la funcion que se encargara de calcular el precio total y el recibo de una venta
def calcular_total(nombre, tipo_cliente, cantidad, precio_por_hoja):
    descuentos = {1: 0.05, 2: 0.08, 3: 0.12, 4: 0.15}
    
    if tipo_cliente in descuentos:
        descuento = descuentos[tipo_cliente]
    else:
        descuento = 0.0
    
    subtotal = cantidad * precio_por_hoja
    neto_por_pagar = subtotal * (1 - descuento)
    
    imprimir_recibo(nombre, subtotal, neto_por_pagar)

def imprimir_recibo(nombre, subtotal, neto_por_pagar):
    print("Nombre del cliente:", nombre)
    print("Subtotal por pagar:", subtotal)
    print("Neto por pagar:", neto_por_pagar)

#App
window = tk.Tk()
window.resizable(1,1)
window.title("App || Hojas de hielo")
window.iconbitmap("C:\\Users\\hvcar\\OneDrive\\Documentos\\PRACTICAS\\SENASOFT\\ProyectoHojas\\bolsa-de-hielo.ico\\")

nombre_label = tk.Label(text="Nombre del cliente:")
nombre_label.grid(row=0, column=0)




window.mainloop()

