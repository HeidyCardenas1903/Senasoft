#1. Cree una clase Persona con sus atributos correspondientes:
#nombre, edad, sexo, nacionalidad. Luego cree una instancia de la clase Persona.

#Solucion😊
class Persona:
    def __init__(self, nombre, edad, sexo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad

# Instancia de la clase Persona
persona1 = Persona(nombre="Juan", edad=30, sexo="Masculino", nacionalidad="Colombiano")

# Acceder a los atributos de la instancia
print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)
print("Sexo:", persona1.sexo)
print("Nacionalidad:", persona1.nacionalidad)

#2.Cree una clase Auto con sus atributos correspondientes: marca, modelo, año, color. Defina también un método, donde luego al instanciar la clase nos diga si el auto esta encendido o apagado.

#Solucion😊
class Auto:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.encendido = False

    def cambiar_estado(self):
        if self.encendido:
            self.encendido = False
        else:
            self.encendido = True

    def estado(self):
        return "encendido" if self.encendido else "apagado"

# Instancia de la clase Auto
mi_auto = Auto(marca="Toyota", modelo="Corolla", año=2022, color="Azul")

# Verificar el estado inicial del auto (apagado)
print("Estado inicial:", mi_auto.estado())

# Encender el auto y verificar su estado nuevamente
mi_auto.cambiar_estado()
print("Estado después de encenderlo:", mi_auto.estado())

# Apagar el auto y verificar su estado nuevamente
mi_auto.cambiar_estado()
print("Estado después de apagarlo:", mi_auto.estado())
