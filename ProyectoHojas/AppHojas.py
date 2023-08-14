from tkinter import *
from sqlite3 import connect
import tkinter as tk

# # Creacion de la base de datos / Hojas - Heidy
# #Conexion :)
conexion = connect("ventas.db")
cursor = conexion.cursor()

#Tabla de ventas
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
root = tk.Tk()
root.title("App || Hojas de hielo")
root.iconbitmap("C:\\Users\\hvcar\\OneDrive\\Documentos\\PRACTICAS\\SENASOFT\\ProyectoHojas\\bolsa-de-hielo.ico\\")

nombre_label = tk.Label(text="Nombre del cliente: ")
nombre_label.grid(row=0, column=0)
nombre_entry = tk.Entry()
nombre_entry.grid(row=0, column=1)

tipo_cliente_label = tk.Label(text="Tipo de cliente 1 2 3 4: ")
tipo_cliente_label.grid(row=1, column=0)
tipo_cliente_entry = tk.Entry()
tipo_cliente_menu = tk.OptionMenu(root,tipo_cliente_entry ,1, 2, 3, 4)
tipo_cliente_menu.grid(row=1, column=1)

cantidad_label = tk.Label(text="Cantidad de hojas: ")
cantidad_label.grid(row=2, column=0)
cantidad_entry = tk.Entry()
cantidad_entry.grid(row=2, column=1)

precio_por_hoja_label = tk.Label(text="Precio por hoja: ")
precio_por_hoja_label.grid(row=3, column=0)



#Estilo
root.config(bg="#B6FCFA")
nombre_label.config(bg="#B6FCFA")
tipo_cliente_label.config(bg="#B6FCFA")
cantidad_label.config(bg="#B6FCFA")
precio_por_hoja_label.config(bg="#B6FCFA")

root.mainloop()
conexion.close()
