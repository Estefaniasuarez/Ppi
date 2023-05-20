import tkinter.ttk
from tkinter.ttk import LabelFrame
from tkinter import FLAT
from tkinter import Button
from colores import *
from tkinter.ttk import Label
from tkinter.ttk import Entry
from MenuUsuBasic import abrir_ventana1


def mostrar_formulario(ventana_principal):


    tkinter.ttk.Style().configure("TLabelframe", background=gris)
    formulario = LabelFrame(ventana_principal, height=300, width=380, relief=FLAT)
    formulario.place(x=500, y=400)

    tkinter.ttk.Style().configure("TLabel", backgroud=blanco, foreground=negro)
    titulo = Label(formulario, text="Login", font=letra_pequena,background=gris,foreground=negro)
    titulo.place(x=150, y=10)

#nombre
    tkinter.ttk.Style().configure("TLabel", backgroud=blanco, foreground=negro)
    usuario = Label(formulario, text="Nombre: *", font=letra_pequena,background=gris,foreground=negro)
    usuario.place(x=30, y=70)

    entry_usuario = Entry(formulario, width=47, )
    entry_usuario.place(x=70, y=110)
    tkinter.ttk.Style().configure("TButton", background=negro, foreground=negro)

#contraseña
    tkinter.ttk.Style().configure("TLabel", backgroud=blanco, foreground=negro)
    contraseña = Label(formulario, text="Contraseña: *", font=letra_pequena,background=gris,foreground=negro)
    contraseña.place(x=30, y=140)

    contraseña = Entry(formulario, width=47,show="*" )
    contraseña.place(x=70, y=180)
    tkinter.ttk.Style().configure("TButton", background=negro, foreground=negro)

    def funcionIngresar (ventana):

        abrir_ventana1(ventana)


    boton_ingresar = Button(ventana_principal,
                            text="Ingresar",
                            bg=negro,
                            fg=blanco,
                            command=lambda:funcionIngresar(ventana_principal),
                            font=letra_pequena,
                            activebackground=gris,
                            activeforeground=negro)
    boton_ingresar.place(x=638, y=630)











