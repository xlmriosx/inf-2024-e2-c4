import tkinter as tk

def saludar():
    print('Hola')


ventana = tk.Tk()
ventana.title('Mi primera ventana con Tkinter')
ventana.geometry('800x600')

boton = tk.Button(ventana, text="SALUDAR!", font=('Arial', 18), command=saludar)
boton.pack()


ventana.mainloop()

# python .\prueba_tk.py