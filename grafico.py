from tkinter import *

def click_boton():
	Label(root, text="¡No vuelvas a presionarlo!").grid(row=1, column=0)



root = Tk()
entrada = Entry(root)
entrada.grid(row=1, column=1)
frm = Frame()
frm.grid(row=0,column=0)
frm.config(width="800", height="600",bg="blue")

texto = Label(root, text="Logistica5.")
texto.grid(row=0, column=1)
#ttk.Label(frm, text="Logistica 5").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
boton1 = Button(root,
                text="Logistica5",
                bg="red",
                padx=50,
                pady=25,command=click_boton).grid(row=1, column=2)
root.mainloop()