from tkinter import *

root=Tk()
root.title('HOJAS DE HIELO || Heidy')
root.iconbitmap("C:\\Users\\hvcar\\OneDrive\\Documentos\\PRACTICAS\\SENASOFT\\ProyectoHojas\\bolsa-de-hielo.ico\\")

frame = Frame(root,width="700",height="450")


label1 = Label(frame,text="Nombre del cliente: ")
label1.grid(row=0, column=0)
entrada1 = Entry(frame)
entrada1.grid(row=0, column=1)

# 

label1 = Label(frame,text="Cantidad de hojas: ")
label1.grid(row=2, column=0)
entrada1 = Entry(frame)
entrada1.grid(row=2, column=1)

root.mainloop()