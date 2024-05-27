from tkinter import *
from tkinter import messagebox

ventana = Tk()

ventana.title = "LOGIN"
ventana.geometry("800x500")
ventana.configure(background="blue")
ventana.resizable(FALSE, FALSE)


frame1 = Frame(ventana,bg="white")
frame2 = Frame(ventana,bg="blue")


frame1.place(x=0,y=0,width=400,height=800)
frame2.place(x=400,y=0,width=400,height=800)

titulo = Label(ventana, text="Inicio Sesion", bg= "white",font= "arial 14")
titulo.place(x=500, y=80, width=200)


usuario = Label(ventana, text= "nombre de usuario: ", bg="white",font= "arial 14")
usuario.place(x=410, y= 140, width=200)
medidas1= Entry(ventana, bg="white",bd= 3)
medidas1.place(x= 600, y=140,width=120)

contraseña = Label(ventana, text= "contraseña: ", bg="white",font= "arial 14")
contraseña.place(x= 420, y=200, width=200)
medidas2= Entry(ventana, width=30, bd=3)
medidas2.place(x=600, y=200, width= 120)

def iniciar():
    messagebox.showinfo("","la sesion esta activa")

boton_sesion = Button(ventana,background= "white",text="ingresar",font= "helvetica 12",command=iniciar)
boton_sesion.place(x=550,y=300,width= 100)


ventana.mainloop()