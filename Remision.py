import tkinter
from tkinter import *
from PIL import ImageTk, Image
import colores
from colores import *
import tkinter as tk

def ventanaremision(abrirremision):
    # Creacio
    ventana_remision = tk.Tk()
    ventana_remision.title("Remisión")
    ventana_remision.configure(bg=gris)
    titulo = Label(ventana_remision, text="Remisión", font=letra_grande, bg=gris, fg=negro)
    titulo.place(in_=ventana_remision, anchor="center", relx=0.5, rely=0.11)
    ancho = 1355
    alto = 750
    # ajustas a pesta;a
    posx = int(ventana_remision.winfo_screenwidth() / 2 - (ancho / 2))
    posy = int(ventana_remision.winfo_screenheight() / 2 - (alto / 2))

    ventana_remision.geometry("{}x{}+{}+{}".format(ancho, alto, posx, posy))
    ventana_remision.resizable(0, 0)

    ############titulo




    #############

    imagen2 = ImageTk.PhotoImage(colores.imagen2)
    Label_imagen2 = Label(ventana_remision, image=imagen2, border=5,background=negro )
    Label_imagen2.image = imagen2
    Label_imagen2.place(x=30, y=150)

    menutitulo = Label(ventana_remision,
                    text="Carta:",
                    bg=crema,
                    fg=negro,
                    font=letra_mediana)
    menutitulo.place(x=55, y=180)




#_______________MENU BEBIDAS____________________
    ############# Label cerveza##################



    titulo1 = Label(ventana_remision,
                    text="Cerveza",
                    bg=crema,
                    fg=negro,
                    font=letra_pequena)
    titulo1.place(x=78, y=340)

########  #  # Boton cerveza#########################
    img = tk.PhotoImage(file="imagenes/cerveza.png")
    img = img.subsample(8, 8)
    buttonorden = tk.Button(ventana_remision, image=img, bg=crema2,border=4, activebackground=crema2)
    buttonorden.pack()
    buttonorden.place(x=90, y=270)

###################################fin cerveza

  ############  # Label coctel##############

    titulo1 = Label(ventana_remision,
                    text="Coctel",
                    bg=crema,
                    fg=negro,
                    font=letra_pequena)
    titulo1.place(x=210, y=340)

    # Boton coctel########################

    imgCoc = tk.PhotoImage(file="imagenes/coctel.png")
    imgCoc = imgCoc.subsample(8, 8)
    buttonCoc = tk.Button(ventana_remision, image=imgCoc, bg=crema2,border=4, activebackground=crema2)
    buttonCoc.pack()
    buttonCoc.place(x=210, y=270)

#############fin coctel###########

    # Label mojito####################

    titulo1 = Label(ventana_remision,
                    text="Mojito",
                    bg=crema,
                    fg=negro,
                    font=letra_pequena)
    titulo1.place(x=90, y=460)

    # Boton mojito########################

    imgMoj = tk.PhotoImage(file="imagenes/mojito.png")
    imgMoj = imgMoj.subsample(8, 8)
    buttonMoj = tk.Button(ventana_remision, image=imgMoj, bg=crema2,border=4, activebackground=crema2)
    buttonMoj.pack()
    buttonMoj.place(x=90, y=390)

    #################fin mojito############
###

    ##########Shot  ##################
    titulo1 = Label(ventana_remision,
                    text="Shot",
                    bg=crema,
                    fg=negro,
                    font=letra_pequena)
    titulo1.place(x=220, y=460)

    #Boton aguardiente########################

    imgShot = tk.PhotoImage(file="imagenes/trago-de-tequila.png")
    imgShot = imgShot.subsample(8, 8)
    buttonShot = tk.Button(ventana_remision, image=imgShot, bg=crema2, border=4, activebackground=crema2)
    buttonShot.pack()
    buttonShot.place(x=210, y=390)
######fin aguardiente ############


####vino
    titulo1 = Label(ventana_remision,
                    text="Vino",
                    bg=crema,
                    fg=negro,
                    font=letra_pequena)
    titulo1.place(x=155, y=590)

    # Boton vino########################

    imgVino = tk.PhotoImage(file="imagenes/vino.png")
    imgVino = imgVino.subsample(8, 8)
    buttonVino = tk.Button(ventana_remision, image=imgVino, bg=crema2, border=4, activebackground=crema2)
    buttonVino.pack()
    buttonVino.place(x=148, y=515)
####################FIN VINO








    #_______________FIN MENU BEBIDAS_____________

    ventana_remision.mainloop()

def salir():
    pass

    #boton_Salir = Button(ventana_remision, text="Regresar", command=salir)
    #boton_Salir.place(x=300,y=300)