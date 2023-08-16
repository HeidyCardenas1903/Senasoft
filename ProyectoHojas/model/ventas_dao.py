from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        tipo_cliente INTEGER,
        cantidad INTEGER,
        precio_por_hoja REAL,
        subtotal REAL,
        neto_por_pagar REAL
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        i = messagebox.showinfo('Crear registro', 'Se creó la tabla en la base de datos')
    except:
        i = messagebox.showwarning('Crear registro', 'La tabla ya existe!')

def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE IF EXISTS ventas'
 
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        i = messagebox.showinfo('Borrar registro', 'La tabla de la base de datos se borró con éxito')
    except:
        i = messagebox.showerror('Borrar registro', 'No hay tabla para borrar')

class Venta:
    def __init__(self, nombre, tipo_cliente, cantidad, precio_por_hoja, subtotal, neto_por_pagar):
        self.id = None
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente
        self.cantidad = cantidad
        self.preciohoja = precio_por_hoja
        self.subtotal = subtotal
        self.neto_por_pagar = neto_por_pagar

    def __str__(self):
        return f'venta[{self.nombre},{self.tipo_cliente},{self.cantidad},{self.preciohoja},{self.subtotal},{self.neto_por_pagar}]'
    
def guardar(venta):
    conexion = ConexionDB()

    sql = f"""INSERT INTO ventas (nombre, tipo_cliente, cantidad, precio_por_hoja, subtotal, neto_por_pagar)
    VALUES('{venta.nombre}', '{venta.tipo_cliente}', '{venta.cantidad}', '{venta.preciohoja}', '{venta.subtotal}', '{venta.neto_por_pagar}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        i = messagebox.showerror('Conexión al registro', 'La tabla no ha sido creada o no existe')    

def listar():
    conexion = ConexionDB()

    lista_clientes = []
    sql = 'SELECT * FROM ventas'

    try:
        conexion.cursor.execute(sql)
        lista_clientes = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        i = messagebox.showwarning('Conexión al registro', 'Error al conectar con la base de datos')