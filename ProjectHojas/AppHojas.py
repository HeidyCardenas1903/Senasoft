import tkinter as tk
from Client.interfaz import *

def main():
    root = tk.Tk()
    root.title('Hojas de hielo || Heidy')
    root.iconbitmap('C:\\Users\\hvcar\\OneDrive\\Documentos\\PRACTICAS\\SENASOFT\\ProyectoHojas\\bolsa-de-hielo.ico')
    root.resizable(1,1)

    barra_menu(root)

    app = Frame(root =root)

    app.mainloop()

if __name__ == '__main__':
    main()
