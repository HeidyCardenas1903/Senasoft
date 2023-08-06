from tkinter import  *

root=Tk()

root.title("Heidy")

root.resizable(1,1)
root.iconbitmap("C:\\Users\\hvcar\\OneDrive\\Documentos\\PRACTICAS\\SENASOFT\\Curso Phyton\\Ejercicios practicos\\dia 12\\nina.ico")

miFrame = Frame(root)
miFrame.pack(fill="y", expand=1)
miFrame.config(width=400, height=300)
miFrame.config(cursor="heart")
miFrame.config(bg="red")
miFrame.config(bd="20")
miFrame.config(relief="ridge")



root.config(cursor="boat")
root.config(bg="blue")
root.config(bd="10")
root.config(relief="sunken")



root.mainloop()
