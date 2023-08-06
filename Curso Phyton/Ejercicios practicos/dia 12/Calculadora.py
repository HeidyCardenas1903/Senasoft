from tkinter import *

i = 0

def click(valor):
    global i
    entrada.insert(i, valor)
    i+=1

def borrar():
    entrada.delete(0, END)
    i=0

#Operciones - funcion eval
def operaciones():
    operacion = entrada.get()
    resultado = eval(operacion)
    entrada.delete(0, END)
    entrada.insert(0,resultado)
    i=0





root=Tk()
root.title("Mi calculadora")
root.iconbitmap("C:\\Users\\hvcar\\OneDrive\\Documentos\\PRACTICAS\\SENASOFT\\Curso Phyton\\Ejercicios practicos\\dia 12\\favicon.ico")

#Entrada
entrada = Entry(root,font=("Curier 20"))
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#Botones
Boton1 = Button(root, text="1", width=5,height=2, command=lambda:click(1))
Boton2 = Button(root, text="2", width=5,height=2, command=lambda:click(2))
Boton3 = Button(root, text="3", width=5,height=2, command=lambda:click(3))
Boton4 = Button(root, text="4", width=5,height=2, command=lambda:click(4))
Boton5 = Button(root, text="5", width=5,height=2, command=lambda:click(5))
Boton6 = Button(root, text="6", width=5,height=2, command=lambda:click(6))
Boton7 = Button(root, text="7", width=5,height=2, command=lambda:click(7))
Boton8 = Button(root, text="8", width=5,height=2, command=lambda:click(8))
Boton9 = Button(root, text="9", width=5,height=2, command=lambda:click(9))
Boton0 = Button(root, text="0", width=13,height=2, command=lambda:click(0))


Boton_borrar = Button(root, text="DEL", width=5,height=2, command=lambda:borrar())
Boton_parentesis1 = Button(root, text="(", width=5,height=2, command=lambda:click('('))
Boton_parentesis2 = Button(root, text=")", width=5,height=2, command=lambda:click(')'))
Boton_punto = Button(root, text=".", width=5,height=2, command=lambda:click('.'))


Boton_div = Button(root, text="/", width=5,height=2, command=lambda:click('/'))
Boton_multi = Button(root, text="*", width=5,height=2, command=lambda:click('*'))
Boton_sum = Button(root, text="+", width=5,height=2, command=lambda:click('+'))
Boton_rest = Button(root, text="-", width=5,height=2, command=lambda:click('-'))
Boton_igual = Button(root, text="=", width=5,height=2, command=lambda:click(operaciones))

#Colocar botones
Boton_borrar.grid(row=1,column=0,padx=5,pady=5)
Boton_parentesis1.grid(row=1,column=1,padx=5,pady=5)
Boton_parentesis2.grid(row=1,column=2,padx=5,pady=5)
Boton_div.grid(row=1,column=3,padx=5,pady=5)

Boton7.grid(row=2,column=0,padx=5,pady=5)
Boton8.grid(row=2,column=1,padx=5,pady=5)
Boton9.grid(row=2,column=2,padx=5,pady=5)
Boton_multi.grid(row=2,column=3,padx=5,pady=5)

Boton4.grid(row=3,column=0,padx=5,pady=5)
Boton5.grid(row=3,column=1,padx=5,pady=5)
Boton6.grid(row=3,column=2,padx=5,pady=5)
Boton_sum.grid(row=3,column=3,padx=5,pady=5)

Boton1.grid(row=4,column=0,padx=5,pady=5)
Boton2.grid(row=4,column=1,padx=5,pady=5)
Boton3.grid(row=4,column=2,padx=5,pady=5)
Boton_rest.grid(row=4,column=3,padx=5,pady=5)

Boton0.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
Boton_punto.grid(row=5,column=2,padx=5,pady=5)
Boton_igual.grid(row=5,column=3,padx=5,pady=5)







root.mainloop()
