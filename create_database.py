import sqlite3

"""Creación de Base da Datos con ID - Nombre - Apellidos - Documento - Edad - Email - Posición - Compañia"""
def create_database():
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    cursor.execute("CREATE TABLE if not exists users (ID INTEGER PRIMARY KEY AUTOINCREMENT,Name VARCHAR(50) NOT NULL,LastName VARCHAR(50) NOT NULL,Document INTEGER UNIQUE NOT NULL,Age INTEGER NOT NULL,Email VARCHAR(50),Position VARCHAR(50),Company VARCHAR(50))")

    conexion.commit()
    cursor.close()