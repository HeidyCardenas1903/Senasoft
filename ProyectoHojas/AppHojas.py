import tkinter as tk
from sqlite3 import connect

# Creacion de la base de datos / Hojas - Heidy
#Conexion :)
conexion = connect("ventas.db")
cursor = conexion.cursor()

#Tabla de ventas
cursor.execute('''
CREATE TABLE sales (
  name text,
  type_id int,
  quantity int,
  price_per_sheet float,
  total float
)
''')