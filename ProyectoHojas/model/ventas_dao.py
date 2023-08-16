from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE ventas (
        id INTEGER,
        nombre TEXT,
        tipo_cliente INTEGER,
        cantidad INTEGER,
        precio_por_hoja REAL,
        subtotal REAL,
        neto_por_pagar REAL,
        PRIMARY KEY(id AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        i = messagebox.showinfo('Crear registro','Se creo la tabla en la base de datos')
    except:
        i = messagebox.showwarning('Crear registro','La tabla ya existe!')

def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE ventas'
 
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        i = messagebox.showinfo('Borrar registro','La tabla de la base de datos se borro con éxito')
    except:
        i = messagebox.showerror('Borrar registro','No hay tabla para borrar')
