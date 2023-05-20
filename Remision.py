import tkinter
from tkinter import *
from PIL import ImageTk, Image
import colores
from colores import *
import tkinter as tk

def ventanaremision(abrirremision):
    # Creacio
    ventana_remision = tk.Tk()
    ventana_remision.title("Menu")
    ventana_remision.configure(bg=gris)
    titulo = Label(ventana_remision, text="Menu", font=letra_mediana, bg=gris, fg=negro)
    titulo.place(in_=ventana_remision, anchor="center", relx=0.5, rely=0.11)
    ancho = 1355
    alto = 750
    # ajustas a pesta;a
    posx = int(ventana_remision.winfo_screenwidth() / 2 - (ancho / 2))
    posy = int(ventana_remision.winfo_screenheight() / 2 - (alto / 2))

    ventana_remision.geometry("{}x{}+{}+{}".format(ancho, alto, posx, posy))
    ventana_remision.resizable(0, 0)



    imagen2 = ImageTk.PhotoImage(colores.imagen2)
    Label_imagen2 = Label(ventana_remision, image=imagen2, border=0)
    Label_imagen2.image = imagen2
    Label_imagen2.place(x=30, y=150)




#_______________MENU BEBIDAS____________________
    # Label cerveza
    # Label remision
    titulo1 = Label(ventana_remision,
                    text="Remisión",
                    bg=gris,
                    fg=negro,
                    font=letra_pequena)
    titulo1.place(x=310, y=430)

    # Boton remision
    img = tk.PhotoImage(file="imagenes/factura.png")
    img = img.subsample(3, 3)
    buttonorden = tk.Button(ventana_remision, image=img, bg=gris, activebackground=gris)
    buttonorden.pack()
    buttonorden.place(x=280, y=250)

#_______________FIN MENU BEBIDAS_____________

    ventana_remision.mainloop()

def salir():
    pass

    #boton_Salir = Button(ventana_remision, text="Regresar", command=salir)
    #boton_Salir.place(x=300,y=300)