from tkinter import *
from colores import *
from formulario import mostrar_formulario

#crea ventana con x dimenciones
principal = Tk()
principal.configure(bg=negro)
principal.title("Inicio Sesion Bar Arcaico")
principal.resizable(0, 0)
principal.geometry("1355x750")




#titulo principal
titulo1 = Label(principal,
                text="Iniciar sesión",
                bg="#090909",
                fg="#FFFFFF",
                font=letra_grande)
titulo1.place(x=550,y=50)
imagen1 = ImageTk.PhotoImage(imagen1)
Label_imagen1 = Label(principal, image = imagen1)
Label_imagen1.configure(border=0)
Label_imagen1.image = imagen1
Label_imagen1.place(x=600, y=185)

mostrar_formulario(principal)

principal.mainloop()