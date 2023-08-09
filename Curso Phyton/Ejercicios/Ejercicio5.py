# 1.Cree una base de datos que se llame Personas. Luego introduzca
# al menos diez personas en esa base de datos.
# 2. Cree una base de datos personas con los siguientes
# requerimientos: nombre, edad, sexo y DNI. El DNI debe ser una
# clave primaria, por lo cual no se puede repetir.
# 3. En la base de datos que acaba de crear realice un CRUD. (Crear,
# leer, actualizar, eliminar)

import sqlite3

conn = sqlite3.connect('Personas.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Personas (
        DNI TEXT PRIMARY KEY,
        nombre TEXT,
        edad INTEGER,
        sexo TEXT
    )
''')

def insert_persona(dni, nombre, edad, sexo):
    cursor.execute('INSERT INTO Personas VALUES (?, ?, ?, ?)', (dni, nombre, edad, sexo))
    conn.commit()


personas_ejemplo = [
    ("12345678A", "Juan Pérez", 30, "M"),
    ("23456789B", "María García", 25, "F"),
    ("34567890C", "Carlos Rodríguez", 40, "M"),
    ("45678901D", "Laura Martínez", 28, "F"),
    ("56789012E", "Andrés López", 22, "M"),
    ("67890123F", "Ana Sánchez", 33, "F"),
    ("78901234G", "Pedro Ramírez", 29, "M"),
    ("89012345H", "Sara Fernández", 37, "F"),
    ("90123456I", "Javier Torres", 45, "M"),
    ("01234567J", "Lucía Díaz", 26, "F")
]

for persona in personas_ejemplo:
    insert_persona(*persona)

def select_persona(dni):
    cursor.execute('SELECT * FROM Personas WHERE DNI = ?', (dni,))
    return cursor.fetchone()


def update_persona(dni, nombre, edad, sexo):
    cursor.execute('UPDATE Personas SET nombre=?, edad=?, sexo=? WHERE DNI=?', (nombre, edad, sexo, dni))
    conn.commit()


def delete_persona(dni):
    cursor.execute('DELETE FROM Personas WHERE DNI = ?', (dni,))
    conn.commit()


print("Persona con DNI 12345678A (antes de la actualización):", select_persona("12345678A"))
update_persona("12345678A", "Juan Pérez Actualizado", 31, "M")
print("Persona con DNI 12345678A (después de la actualización):", select_persona("12345678A"))

print("Eliminando persona con DNI 23456789B")
delete_persona("23456789B")


conn.close()
