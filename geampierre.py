import tkinter as tk



def Getdata():
  Ln = tk.Label(frame, text=cname.get())
  Ln.pack()
  Ln1 = tk.Label(frame, text=clast.get())
  Ln1.pack()
  Ln2 = tk.Label(frame, text=cage.get())
  Ln2.pack()
  Ln3 = sexv.get()
  if Ln3 == 1:
   m =tk.Label(frame, text="Masculino")
   m.pack()
  elif Ln3 == 2:
   f =tk.Label(frame, text="Femenino")
   f.pack()
  
  elif Ln3 == 3:
   x =tk.Label(frame, text="Helicoptero de combate")
   x.pack()
  Ln4 = city.curselection()
  for index in Ln4:
   item = city.get(index)
  c =tk.Label(frame, text=item)
  c.pack()



ventana = tk.Tk()



ventana.title("Ventana1")

ventana.geometry("1280x720")

lname = tk.Label(ventana, text="cual es su nombre: ")
lname.grid(column=0, row= 1, sticky="w", pady= 5)
cname = tk.Entry(ventana, width=30)
cname.grid(column=1 , row= 1,sticky="w", pady= 5)


llast = tk.Label(ventana, text="cual es su apellido: ")
llast.grid(column= 0, row= 2,sticky="w", pady=5)
clast = tk.Entry(ventana, width=30)
clast.grid(column= 1, row= 2,sticky="w", pady= 5)

lage = tk.Label(ventana, text="cual es su edad: ")
lage.grid(column=0, row=3,sticky="w", pady= 5)
cage = tk.Entry(ventana, width=30)
cage.grid(column=1, row=3,sticky="w", pady=5)

sexv = tk.IntVar()
lsex = tk.Label(ventana, text="Sexo:")
lsex.grid(column=0, row=4, pady=5)

rmasc = tk.Radiobutton(ventana, text="Masculino", value=1, state="normal", variable=sexv)
rmasc.grid(column=0, row=5, pady=5)

rfem = tk.Radiobutton(ventana, text="Femenino", value=2, state="normal", variable=sexv)
rfem.grid(column=1, row= 5, pady= 5)
rna = tk.Radiobutton(ventana, text="cagasten", value=3, state="normal", variable=sexv)
rna.grid(column=3,row=5,pady=5)

city = tk.Listbox(ventana, width=30, selectmode="single")
city.insert(1, "medellin")
city.insert(2, "paris")
city.insert(3, "cartagena")
city.insert(4, "turbaco")
city.grid(column=0, row=6, pady=5)

rbutton= tk.Button(ventana, text="confirmar registro", command=Getdata)
rbutton.grid(column=7, row=7, pady=5)

frame = tk.Frame(ventana, width=200, height=200)
frame.grid(column=8, row=8, pady=8)
ventana.mainloop()