#1.Cree una clase Persona con sus atributos correspondientes. Luego cree una clase Empleado que herede esos atributos de la clase Padre.
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

class Empleado(Persona):
    def __init__(self, nombre, edad, genero, salario, cargo):
        super().__init__(nombre, edad, genero)
        self.salario = salario
        self.cargo = cargo


#2.Realice una clase persona, luego haga una clase empleado que herede los atributos de la clase Persona. Por último, cree un método de la clase empleado e instancie la clase.
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}"


class Empleado(Persona):
    def __init__(self, nombre, edad, genero, salario, cargo):
        super().__init__(nombre, edad, genero)
        self.salario = salario
        self.cargo = cargo

    def __str__(self):
        return f"{super().__str__()}, Salario: {self.salario}, Cargo: {self.cargo}"

    def aumentar_salario(self, aumento):
        self.salario += aumento

persona1 = Persona("Juan", 30, "Masculino")
print(persona1)

empleado1 = Empleado("Ana", 25, "Femenino", 50000, "Gerente")
print(empleado1)

empleado1.aumentar_salario(10000)
print(f"Nuevo salario de {empleado1.nombre}: {empleado1.salario}")

