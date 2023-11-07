import sqlite3

miConexion = sqlite3.connect("CreacionBD")

miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
    DNI INT PRIMARY KEY UNIQUE,
    Nombre VARCHAR(10)
    )
''')

miCursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos (
    ID INTEGER PRIMARY KEY,
    Nombre VARCHAR(10),
    Precio FLOAT
    )
''')

miCursor.execute('''
    CREATE TABLE IF NOT EXISTS Distrito (
    ID INTEGER PRIMARY KEY,
    Nombre VARCHAR(10),
    Origen VARCHAR(10),
    Distancia FLOAT
    )
''')

miCursor.execute('''
    CREATE TABLE IF NOT EXISTS Orden (
    ID INTEGER PRIMARY KEY,
    Cliente INT,
    Producto VARCHAR(10),
    Distrito VARCHAR(10)
    )
''')

miConexion.close()


