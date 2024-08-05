import tkinter as tk

ventana = tk.Tk()
ventana.title('Mi primera ventana con Tkinter')
ventana.geometry('800x600')

etiqueta = tk.Label(ventana, text='Hola mundo!', font=('Console', 20))
etiqueta.pack()

ventana.mainloop()

# python .\prueba_tk.py