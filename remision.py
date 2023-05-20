from tkinter import *
from colores import *

def ventanaremision(ventana3):
    ventana1 = Tk(negro)
    titulo = Label(ventana1, text="Bienvenido",
                   font=letra_mediana, bg=negro,fg=blanco)
    titulo.place(in_=ventana1,anchor="center", relx=0.5, rely=0.17)
    ancho = 1355
    alto = 750

    # ajustas a pesta;a
    posx = int(ventana1.winfo_screenwidth() / 2 - (ancho / 2))
    posy = int(ventana1.winfo_screenheight() / 2 - (alto / 2))

    ventana1.geometry("{}x{}+{}+{}".format(ancho, alto, posx, posy))
    ventana1.resizable(0, 0)


    boton_ingresar = Button(ventana1,
                            text="Ingresar",
                            bg=negro,
                            fg=blanco,
                            font=letra_pequena,
                            activebackground=cafe_bonito,
                            activeforeground=blanco)
    boton_ingresar.place(x=638, y=630)

def salir():
    pass

    #boton_Salir = Button(ventana1, text="Regresar", command=salir)
    #boton_Salir.place(x=300,y=300)