from tkinter import *
from  tkinter import font
import colores
from colores import *
from MenuUsuBasic import abrir_menubc



#crea ventana con x dimenciones
principal = Tk()
principal.configure(bg=gris)
principal.title("Inicio Sesion Bar Arcaico")

ancho = 1355
alto = 750

#ajustas a pestaña
posx=int(principal.winfo_screenwidth()/2 - (ancho/2))
posy=int(principal.winfo_screenheight()/2 - (alto/2))

principal.geometry("{}x{}+{}+{}".format(ancho,alto,posx,posy))
principal.resizable(0, 0)





#titulo principal
titulo1 = Label(principal,
                text="Iniciar sesión",
                bg=gris,
                fg=negro,
                font=letra_grande)
titulo1.place(x=550,y=50)


#logo BarArcaico
imagen1 = ImageTk.PhotoImage(colores.imagen1)
Label_imagen1 = Label(principal, image = imagen1,border=0)
Label_imagen1.image = imagen1
Label_imagen1.place(x=600, y=150)



def funcionIngresar(ventana):
    principal.destroy()
    abrir_menubc(ventana)

boton_ingresar = Button(principal,
                        text="Ingresar",
                        bg=negro,
                        fg=blanco,
                        command=lambda: funcionIngresar(principal),
                        font=letra_pequena,
                        activebackground=gris,
                        activeforeground=negro)
boton_ingresar.place(x=640, y=600)


#Texto Usuario
contrasena = Label( text="Usuario: ", font=("Times New Roman", 20, "bold"),background=gris,foreground=negro)
contrasena.place(x=590, y=450)
#Caja Usuario
entry_usuario = Entry( width=30,border=2)
entry_usuario.place(x=700, y=460)



contrasena = Label( text="Contraseña: ", font=("Times New Roman", 20, "bold"),background=gris,foreground=negro)
contrasena.place(x=548, y=492)
entry_contrasena = Entry( width=30,border=2,show="*")
entry_contrasena.place(x=700, y=500)

#boton reactivo
""" 
tkinter.ttk.Style().configure("TButton", background=negro, foreground=blanco)
tkinter.ttk.Style().map("C.TButton",
foreground=[("pressed", azul_claro), ("active", negro)],
background= [("pressed", "!disabled", cyan), ("active", negro)])
"""

principal.mainloop()
