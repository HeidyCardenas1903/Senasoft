import tkinter as tk
from client.interfaz import *


def main():
    root = tk.Tk()
    root.title('Hojas de hielo || Heidy')
    root.iconbitmap('C:\\Users\\hvcar\\OneDrive\\Documentos\\PRACTICAS\\SENASOFT\\ProyectoHojas\\iconoapp.ico')
    root.resizable()

    barra_menu(root)
    

    app = Frame(root =root)

    root.mainloop()

if __name__ == '__main__':
    main()