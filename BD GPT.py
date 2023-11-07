class Cliente:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.conexion = sqlite3.connect("clientes.db")
        self.cursor = self.conexion.cursor()
        self._crear_tabla()

    def _crear_tabla(self):
        query = """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            apellido TEXT,
            correo TEXT
        )
        """
        self.cursor.execute(query)
        self.conexion.commit()

    def crear_cliente(self):
        query = "INSERT INTO clientes (nombre, apellido, correo) VALUES (?, ?, ?)"
        valores = (self.nombre, self.apellido, self.correo)
        self.cursor.execute(query, valores)
        self.conexion.commit()
        print("Cliente creado con éxito.")

    def leer_clientes(self):
        query = "SELECT * FROM clientes"
        self.cursor.execute(query)
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Apellido: {cliente[2]}, Correo: {cliente[3]}")

    def actualizar_cliente(self, cliente_id, nuevo_nombre, nuevo_apellido, nuevo_correo):
        query = "UPDATE clientes SET nombre=?, apellido=?, correo=? WHERE id=?"
        valores = (nuevo_nombre, nuevo_apellido, nuevo_correo, cliente_id)
        self.cursor.execute(query, valores)
        self.conexion.commit()
        print("Cliente actualizado con éxito.")

    def eliminar_cliente(self, cliente_id):
        query = "DELETE FROM clientes WHERE id=?"
        valores = (cliente_id,)
        self.cursor.execute(query, valores)
        self.conexion.commit()
        print("Cliente eliminado con éxito.")

    def cerrar_conexion(self):
        self.conexion.close()

# Ejemplo de uso
if __name__ == "__main__":
    cliente1 = Cliente("John", "Doe", "johndoe@example.com")
    cliente1.crear_cliente()

    cliente2 = Cliente("Jane", "Smith", "janesmith@example.com")
    cliente2.crear_cliente()

    print("Clientes registrados:")
    cliente1.leer_clientes()

    cliente1.actualizar_cliente(1, "John", "Johnson", "john@example.com")

    print("Clientes actualizados:")
    cliente1.leer_clientes()

    cliente1.eliminar_cliente(2)

    print("Clientes después de eliminar:")
    cliente1.leer_clientes()

    cliente1.cerrar_conexion()