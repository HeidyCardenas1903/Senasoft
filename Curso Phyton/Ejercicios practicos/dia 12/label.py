from tkinter import *


root=Tk()
root.title("Bienvenida")
root.config(width=400, height=300)

label = Label(root,text="Hola Mundo")
label.place(x=100,y=50)
label.config(bg="Pink", fg="Blue", font=("Curier", 20))

label = Label(root,text="Bievenida Profe Angelica")
label.place(x=100,y=100)
label.config(bg="Blue", fg="Pink")








root.mainloop()