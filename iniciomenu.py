from tkinter import *
from colores import *
from remision import abrir_ventana2

def abrir_menubc(ventana):
    #Creacio
    ventana_menubc = Tk()
    ventana_menubc.title("Menu")
    ventana_menubc.configure(bg=gris)
    titulo = Label(ventana_menubc, text="Bienvenido",font=letra_mediana, bg=gris,fg=negro)
    titulo.place(in_=ventana_menubc,anchor="center", relx=0.5, rely=0.17)
    ancho = 1355
    alto = 750
    # ajustas a pesta;a
    posx = int(ventana_menubc.winfo_screenwidth() / 2 - (ancho / 2))
    posy = int(ventana_menubc.winfo_screenheight() / 2 - (alto / 2))

    ventana_menubc.geometry("{}x{}+{}+{}".format(ancho, alto, posx, posy))
    ventana_menubc.resizable(0, 0)

    def abrir_remision(ventana):
        abrir_ventana2(ventana)


    boton_ingresar = Button(ventana_menubc,
                            text="Ingresar",image=imagen1,
                            bg=negro,
                            fg=blanco,
                            command=lambda:abrir_remision(ventana_menubc),
                            font=letra_pequena,
                            activebackground=cafe_bonito,
                            activeforeground=blanco)
    boton_ingresar.place(x=638, y=630)

def salir():
    pass

    #boton_Salir = Button(ventana_menubc, text="Regresar", command=salir)
    #boton_Salir.place(x=300,y=300)