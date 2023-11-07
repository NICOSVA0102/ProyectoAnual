import sqlite3

miConexion = sqlite3.connect("CreacionBD")

miCursor = miConexion.cursor()

class Producto:
    
    def nuevoP(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

        miCursor.execute("INSERT INTO Productos (Nombre, Precio) VALUES (?, ?)", (nombre, precio))

        miConexion.commit()
     
class Cliente:

    def nuevoC(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        
        miCursor.execute("INSERT INTO Clientes (DNI, Nombre) VALUES (?, ?)", (dni, nombre))
    
        miConexion.commit()

class Distrito:

    def nuevoD(self, nombre, origen, distancia):
        self.nombre = nombre
        self.origen = origen
        self.distancia = distancia

        miCursor.execute("INSERT INTO Distrito (Nombre, Origen, Distancia) VALUES (?, ?, ?)", (nombre, origen, distancia))
    
        miConexion.commit()

class Orden:
    def __init__(self, producto, cliente, distrito):
        self.producto = producto
        self.cliente = cliente
        self.distrito = distrito

Productonuevo = Producto()
Clientenuevo = Cliente()
Distritonuevo = Distrito()

Productonuevo.nuevoP("Celular", 500)
Distritonuevo.nuevoD("San Martin", "Argentina", "50km")
miConexion.close()
