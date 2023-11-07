from tkinter import *
from tkinter import messagebox
import sqlite3

def registrarNuevoCliente():

    DNI = cuadroDNI.get()

    Nombre = cuadroNombre.get()

    miConexion = sqlite3.connect("CreacionBD")

    miCursor = miConexion.cursor()

    try:
        miCursor.execute("INSERT INTO Clientes (DNI, Nombre) VALUES (?, ?)", (DNI, Nombre))

        miConexion.commit()

        miConexion.close()
        
        messagebox.showinfo("Registro Exitoso", "El cliente se ha registrado exitosamente.")

    except:

        messagebox.showerror("Error", "No se ha podido registrar al cliente, verifique los datos e intente nuevamente.")
        
def Ventana2 ():

    cliente = cuadroCliente.get()

    producto = cuadroProducto.get()

    distrito = cuadroDistrito.get()

    miConexion = sqlite3.connect("CreacionBD")

    miCursor = miConexion.cursor()

    try: 

        miCursor.execute("SELECT DNI FROM Clientes WHERE DNI = ?",(cliente,))
        resultadoC = miCursor.fetchone()
        
        if resultadoC:

            miCursor.execute("SELECT Nombre FROM Productos WHERE Nombre = ?",(producto,))
            resultadoP = miCursor.fetchone()
        
            if resultadoP:
                miCursor.execute("INSERT INTO Orden (Cliente, Producto, Distrito) VALUES (?, ?, ? )", (cliente, producto, distrito))

                miConexion.commit()

                miConexion.close

                messagebox.showinfo("Orden Exitosa", "La orden se ha generado exitosamente.")
                
            else:
                messagebox.showerror("Producto no encontrado", "El producto no existe.")

        else:
            messagebox.showerror("Cliente no encontrado", "El cliente con el DNI proporcionado no existe.")

            raise Exception("Cliente no encontrado")

        
    except Exception as e:
            
        ventana2=Tk()

        ventana2.title("Ventana")

        miFrame2 = Frame(ventana2, width = 1200, height = 600)
        miFrame2.pack()
            
        global cuadroDNI, cuadroNombre
            
        cuadroDNI = Entry(miFrame2)
        cuadroDNI.grid(row = 1, column = 1, padx = 10, pady = 10)

        cuadroNombre = Entry(miFrame2)
        cuadroNombre.grid(row = 2, column = 1, padx = 10, pady = 10)

        tituloLabel = Label(miFrame2, text = "Registrar Cliente")
        tituloLabel.grid(row = 0, column = 0, columnspan=2, sticky = "nsew", padx = 10, pady = 10)

        DNILabel = Label(miFrame2, text = "DNI: ")
        DNILabel.grid(row = 1, column = 0, sticky = "nsew", padx = 10, pady = 10)

        NombreLabel = Label(miFrame2, text = "Nombre: ")
        NombreLabel.grid(row = 2, column = 0, sticky = "nsew", padx = 10, pady = 10)

        botonRegistrarCliente = Button(ventana2, text = "Registrar", command=registrarNuevoCliente)
        botonRegistrarCliente.pack()
            
        ventana2.mainloop()


raiz=Tk()

raiz.title("Ventana")

miFrame = Frame(raiz, width = 1200, height = 600)
miFrame.pack()

global cuadroCliente, cuadroProducto, cuadroDistrito

cuadroCliente = Entry(miFrame)
cuadroCliente.grid(row = 1, column = 1, padx = 10, pady = 10)

cuadroProducto = Entry(miFrame)
cuadroProducto.grid(row = 2, column = 1, padx = 10, pady = 10)

cuadroDistrito = Entry(miFrame)
cuadroDistrito.grid(row = 3, column = 1, padx = 10, pady = 10)

tituloLabel = Label(miFrame, text = "Generar Orden ")
tituloLabel.grid(row = 0, column = 0, columnspan=2, sticky = "nsew", padx = 10, pady = 10)

clienteLabel = Label(miFrame, text = "Cliente: ")
clienteLabel.grid(row = 1, column = 0, sticky = "nsew", padx = 10, pady = 10)

productoLabel = Label(miFrame, text = "Producto: ")
productoLabel.grid(row = 2, column = 0, sticky = "nsew", padx = 10, pady = 10)

distritoLabel = Label(miFrame, text = "Distrito: ")
distritoLabel.grid(row = 3, column = 0, sticky = "nsew", padx = 10, pady = 10)

botonGenerarOrden = Button(raiz, text = "Generar", command=Ventana2)
botonGenerarOrden.pack()

raiz.mainloop()



