from tkinter import *
from colores import *
import tkinter as tk
import colores
from tkinter import ttk
from remision import ventanaremision
from tkinter import FLAT

def abrir_menubc(ventana):
    #Creacio
    ventana_menubc = tk.Tk()
    ventana_menubc.title("Menu")
    ventana_menubc.configure(bg=gris)
    titulo = Label(ventana_menubc, text="Menu",font=letra_mediana, bg=gris,fg=negro)
    titulo.place(in_=ventana_menubc,anchor="center", relx=0.5, rely=0.11)
    ancho = 1355
    alto = 750
    # ajustas a pesta;a
    posx = int(ventana_menubc.winfo_screenwidth() / 2 - (ancho / 2))
    posy = int(ventana_menubc.winfo_screenheight() / 2 - (alto / 2))

    ventana_menubc.geometry("{}x{}+{}+{}".format(ancho, alto, posx, posy))
    ventana_menubc.resizable(0, 0)

    #Label Orden
    titulo1 = Label(ventana_menubc,
                    text="Remisión",
                    bg=gris,
                    fg=negro,
                    font=letra_pequena)
    titulo1.place(x=310, y=430)


    #Boton Orden
    img = tk.PhotoImage(file="imagenes/factura.png")
    img = img.subsample(3, 3)
    buttonorden = tk.Button(ventana_menubc, image=img,bg=gris,activebackground=gris, command=lambda:funcion_abrirremision(ventana_menubc) )
    buttonorden.pack()
    buttonorden.place(x=280, y=250)


    #Label Inventario
    textoinventario = Label(ventana_menubc,
                    text="Inventario",
                    bg=gris,
                    fg=negro,
                    font=letra_pequena)
    textoinventario.place(x=932, y=430)

    #Boton Inventario
    img1 = tk.PhotoImage(file="imagenes/1referencia.png")
    img1 = img1.subsample(3, 3)
    buttoninventario = tk.Button(ventana_menubc, image=img1,bg=gris,activebackground=gris, command=lambda: print("Button clicked"))
    buttoninventario.pack()
    buttoninventario.place(x=900, y=250)

    imagen1 = ImageTk.PhotoImage(colores.imagen1)
    Label_imagen1 = Label(ventana_menubc, image=imagen1, border=0)
    Label_imagen1.image = imagen1
    Label_imagen1.place(x=590, y=150)

    ventana_menubc.mainloop()


def funcion_abrirremision(ventana):
    ventana1=abrir_menubc(ventana)
    ventana1.destroy()
    ventanaremision(ventana )
def salir():
    pass

    #boton_Salir = Button(ventana_menubc, text="Regresar", command=salir)
    #boton_Salir.place(x=300,y=300)