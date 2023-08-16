import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from model.ventas_dao import crear_tabla, borrar_tabla
from model.ventas_dao import Venta

def info():
    i= messagebox.showinfo('Informacion','Esta aplicacion fue creada por Heidy')

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    menu_inicio=tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio)

    menu_inicio.add_command(label='Crear tabla en DB', command= crear_tabla)
    menu_inicio.add_command(label='Eliminar tabla en DB', command= borrar_tabla)
    menu_inicio.add_command(label='Salir', command= root.destroy)

    barra_menu.add_cascade(label = 'Información', command= info)


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=800, height=520)
        self.root = root
        self.pack()

        self.campos_ventas()
        self.desabilitar_campos()
        self.calcular_total()
        self.tabla_registros()

    def campos_ventas(self):
        # Labels de cada campo
        self.label_nombre = tk.Label(self, text='Nombre del cliente: ')
        self.label_nombre.config(font= ('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0,column=1, padx= 10, pady= 5)

        self.label_tipo_cliente = tk.Label(self, text='Tipo de cliente (1 2 3 4): ')
        self.label_tipo_cliente.config(font= ('Arial', 12, 'bold'))
        self.label_tipo_cliente.grid(row=1,column=1, padx= 10, pady= 5)

        self.label_cantidad = tk.Label(self, text='Cantidad: ')
        self.label_cantidad.config(font= ('Arial', 12, 'bold'))
        self.label_cantidad.grid(row=2,column=1, padx= 10, pady= 5)

        self.label_precio_por_hoja = tk.Label(self, text='Precio por hoja: ')
        self.label_precio_por_hoja.config(font= ('Arial', 12, 'bold'))
        self.label_precio_por_hoja.grid(row=3,column=1, padx= 10, pady= 5)

        self.label_subtotal = tk.Label(self, text='Subtotal: ')
        self.label_subtotal.config(font= ('Arial', 12, 'bold'), fg= '#4A55A2')
        self.label_subtotal.grid(row=4,column=1, padx= 10, pady= 5)

        self.label_neto_por_pagar = tk.Label(self, text='Neto por pagar: ')
        self.label_neto_por_pagar.config(font= ('Arial', 12, 'bold'), fg= '#4A55A2')
        self.label_neto_por_pagar.grid(row=5,column=1, padx= 10, pady= 5)

        #Entrys
        self.nombre=tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable= self.nombre)
        self.entry_nombre.config(width= 50,font= ('Arial', 12),bd=2)
        self.entry_nombre.grid(row=0, column= 1,padx= 20, pady= 5, columnspan=3)

        self.tipo_cliente = tk.StringVar()
        self.entry_tipo_cliente = tk.Entry(self, textvariable= self.tipo_cliente )
        self.entry_tipo_cliente.config(width= 50,font= ('Arial', 12),bd=2)
        self.entry_tipo_cliente.grid(row=1, column= 1,padx= 20, pady= 5, columnspan=3)

        self.cantidad = tk.StringVar()
        self.entry_cantidad = tk.Entry(self,textvariable= self.cantidad)
        self.entry_cantidad.config(width= 50,font= ('Arial', 12),bd=2)
        self.entry_cantidad.grid(row=2, column= 1,padx= 20, pady= 5, columnspan=3)

        self.preciohoja = tk.StringVar()
        self.entry_precio_por_hoja = tk.Entry(self, textvariable= self.preciohoja)
        self.entry_precio_por_hoja.config(width= 50,font= ('Arial', 12),bd=2)
        self.entry_precio_por_hoja.grid(row=3, column= 1,padx= 20, pady= 5, columnspan=3)

        self.subtotal = tk.StringVar()
        self.entry_subtotal = tk.Entry(self, textvariable= self.subtotal)
        self.entry_subtotal.config(width= 50,font= ('Arial', 12),bd=5)
        self.entry_subtotal.grid(row=4, column= 1,padx= 20, pady= 5, columnspan=3)

        self.neto_por_pagar = tk.StringVar()
        self.entry_neto_por_pagar = tk.Entry(self, textvariable= self.neto_por_pagar)
        self.entry_neto_por_pagar.config(width= 50,font= ('Arial', 12),bd=5)
        self.entry_neto_por_pagar.grid(row=5, column= 1,padx= 20, pady= 5, columnspan=3)
        
        # Botones 
        self.boton_nueva_venta = tk.Button(self, text='Nuevo', command= self.habilitar_campos )
        self.boton_nueva_venta.config(width= 20, font= ('Arial', 12, 'bold'), fg= '#FFF', bg= '#0082FF', 
                                      cursor= 'hand2', activebackground='#D2E9FF')
        self.boton_nueva_venta.grid(row=6,column=1,padx= 5, pady= 5)

        self.boton_calcular = tk.Button(self, text='Calcular', command= self.calcular_total)
        self.boton_calcular.config(width= 20, font= ('Arial', 12, 'bold'), fg= '#FFF', bg= '#32A8F3', 
                                      cursor= 'hand2', activebackground='#D2E9FF')
        self.boton_calcular.grid(row=6,column=2,padx= 5, pady= 5)

        self.boton_guardar = tk.Button(self, text='Guardar', command= self.guardar_datos)
        self.boton_guardar.config(width= 20, font= ('Arial', 12, 'bold'), fg= '#FFF', bg= '#20A0F1', 
                                      cursor= 'hand2', activebackground='#D2E9FF')
        self.boton_guardar.grid(row=6,column=3,padx= 5, pady= 5)

        self.boton_cancelar = tk.Button(self, text='Cancelar', command= self.desabilitar_campos)
        self.boton_cancelar.config(width= 20, font= ('Arial', 12, 'bold'), fg= '#FFF', bg= '#3370AC', 
                                      cursor= 'hand2', activebackground='#D2E9FF')
        self.boton_cancelar.grid(row=7,column=2,padx= 5, pady= 5)

    def habilitar_campos(self):
        self.nombre.set('')
        self.tipo_cliente.set('')
        self.cantidad.set('')
        self.preciohoja.set('')
        self.subtotal.set('')
        self.neto_por_pagar.set('')

        self.entry_nombre.config(state='normal')
        self.entry_tipo_cliente.config(state='normal')
        self.entry_cantidad.config(state='normal')
        self.entry_precio_por_hoja.config(state='normal')
        self.entry_subtotal.config(state='disabled')
        self.entry_neto_por_pagar.config(state='disabled')

        self.boton_calcular.config(state= 'normal')
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='normal')

    def desabilitar_campos(self):
        self.nombre.set('')
        self.tipo_cliente.set('')
        self.cantidad.set('')
        self.preciohoja.set('')
        self.subtotal.set('')
        self.neto_por_pagar.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_tipo_cliente.config(state='disabled')
        self.entry_cantidad.config(state='disabled')
        self.entry_precio_por_hoja.config(state='disabled')
        self.entry_subtotal.config(state='disabled')
        self.entry_neto_por_pagar.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
        self.boton_calcular.config(state= 'disabled')

    def calcular_total(self):
        try:
            cantidad = int(self.cantidad.get())
            precio_hoja = float(self.preciohoja.get())
            subtotal = cantidad * precio_hoja
            self.subtotal.set(f"${subtotal:.2f}")

            tipo_cliente = int(self.tipo_cliente.get())
            if tipo_cliente in [1, 2, 3, 4]:
                descuento = {1: 0.05, 2: 0.08, 3: 0.12, 4: 0.15}[tipo_cliente]
                total = subtotal * (1 - descuento)
                self.neto_por_pagar.set(f"${total:.2f}")
            else:
                self.neto_por_pagar.set(f"${subtotal:.2f}")
        except ValueError:
            messagebox.showinfo("Sugerencia", "Por favor ingresar valores válidos para cantidad y precio por hoja (Ej: Números enteros)")

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def guardar_datos(self):
        nueva_venta = Venta(
            self.nombre.get(),
            self.tipo_cliente.get(),
            self.cantidad.get(),
            self.preciohoja.get(),
            self.subtotal.get(),
            self.neto_por_pagar.get(),
        )

        guardar=(nueva_venta)

        # self.desabilitar_campos()

    def tabla_registros(self):
        self.tabla = ttk.Treeview(self, columns=('Nombre cliente', 'Tipo de cliente', 'Cantidad de hojas', 'Precio por hoja', 'Subtotal', 'Neto Pagado'))
        self.tabla.grid(row= 10, column=0 ,columnspan=6)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre cliente')
        self.tabla.heading('#2', text='Tipo de cliente')
        self.tabla.heading('#3', text='Cantidad de hojas')
        self.tabla.heading('#4', text='Precio por hoja')
        self.tabla.heading('#5', text='Subtotal')
        self.tabla.heading('#6', text='Neto Pagado')

        # Editar
        self.boton_editar = tk.Button(self, text='Editar')
        self.boton_editar.config(width= 20, font= ('Arial', 12, 'bold'), fg= '#FFF', bg= '#0082FF', 
                                      cursor= 'hand2', activebackground='#D2E9FF')
        self.boton_editar.grid(row=12,column=2,padx= 5, pady= 5)

        #Eliminar
        self.boton_eliminar = tk.Button(self, text='Eliminar')
        self.boton_eliminar.config(width= 20, font= ('Arial', 12, 'bold'), fg= '#FFF', bg= '#3370AC', 
                                      cursor= 'hand2', activebackground='#D2E9FF')
        self.boton_eliminar.grid(row=13,column=2,padx= 5, pady= 5)
        



        


