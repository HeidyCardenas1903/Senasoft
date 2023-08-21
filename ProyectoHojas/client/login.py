import tkinter as tk
from tkinter import messagebox
from client.interfaz import Frame

class VentanaInicioSesion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Inicio de Sesión')
        self.iconbitmap('C:\\Users\\hvcar\\OneDrive\\Documentos\\PRACTICAS\\SENASOFT\\ProyectoHojas\\login.ico')
        self.geometry("350x150")
        
        self.label_usuario = tk.Label(self, text='Usuario:')
        self.label_usuario.pack()
        
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack()
        
        self.label_contraseña = tk.Label(self, text='Contraseña:')
        self.label_contraseña.pack()
        
        self.entry_contraseña = tk.Entry(self, show='*')
        self.entry_contraseña.pack()
        
        self.boton_iniciar = tk.Button(self, text='Iniciar Sesión', command=self.verificar_inicio_sesion)
        self.boton_iniciar.pack()

    def verificar_inicio_sesion(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()

        if usuario == 'Heidyadmin' and contraseña == '123456Sena':
            self.destroy()
            aplicacion_principal = Frame()
        else:
            messagebox.showerror('Inicio de Sesión Fallido', 'Usuario o contraseña incorrectos')

if __name__ == '__main__':
    ventana_inicio_sesion = VentanaInicioSesion()
    ventana_inicio_sesion.mainloop()
