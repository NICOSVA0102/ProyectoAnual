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

def ventana():
    ventana1 = Tk()
    
    ventana1.title("Nueva Orden")

    miFrame3 = Frame(ventana1, width = 1200, height = 600)
    miFrame3.pack()

    global cuadroCliente, cuadroProducto, cuadroDistrito

    cuadroCliente = Entry(miFrame3)
    cuadroCliente.grid(row = 1, column = 1, padx = 10, pady = 10)

    cuadroProducto = Entry(miFrame3)
    cuadroProducto.grid(row = 2, column = 1, padx = 10, pady = 10)

    cuadroDistrito = Entry(miFrame3)
    cuadroDistrito.grid(row = 3, column = 1, padx = 10, pady = 10)

    tituloLabel = Label(miFrame3, text = "Generar Orden ")
    tituloLabel.grid(row = 0, column = 0, columnspan=2, sticky = "nsew", padx = 10, pady = 10)

    clienteLabel = Label(miFrame3, text = "Cliente: ")
    clienteLabel.grid(row = 1, column = 0, sticky = "nsew", padx = 10, pady = 10)

    productoLabel = Label(miFrame3, text = "Producto: ")
    productoLabel.grid(row = 2, column = 0, sticky = "nsew", padx = 10, pady = 10)

    distritoLabel = Label(miFrame3, text = "Distrito: ")
    distritoLabel.grid(row = 3, column = 0, sticky = "nsew", padx = 10, pady = 10)

    botonGenerarOrden = Button(ventana1, text = "Generar", command=Ventana2)
    botonGenerarOrden.pack()

    ventana1.mainloop()
    
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

def clientes():
    miConexion = sqlite3.connect("CreacionBD")

    miCursor = miConexion.cursor()
    
    
def productos():

    miConexion = sqlite3.connect("CreacionBD")

    miCursor = miConexion.cursor()
def distritos():

    miConexion = sqlite3.connect("CreacionBD")

    miCursor = miConexion.cursor()

raiz=Tk()

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

archivoNuevaOrden=Menu(barraMenu)

archivoClientes=Menu(barraMenu)

archivoProductos=Menu(barraMenu)

archivoDistritos=Menu(barraMenu)

barraMenu.add_command(label="Nueva Orden", command=ventana)

barraMenu.add_command(label="Clientes", command=)

barraMenu.add_command(label="Productos", command=)

barraMenu.add_command(label="Distritos", command=)

raiz.mainloop()




