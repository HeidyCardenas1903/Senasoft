import sqlite3

conexion = sqlite3.connect('MiBase.db')#nuestra primer conexion
cursor = conexion.cursor()
#cursor.execute('CREATE TABLE USUARIOS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(50))')

cursor.execute("INSERT INTO USUARIOS VALUES('Brian',25,'Masculino')")
conexion.close()