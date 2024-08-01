python 

es un lenguaje de alto nivel interrpretado. es conocido por su sintaxis clara y legible lo que facilita el aprendizage y la estructura del codigo.
admite multiples paradigmas de progra incluidos los paradigmas imperactivos orientados a objetos y funcional 

algunas caracteristicas son:

sintaxis simple y legible 

multi paradigma

bibliotecas estandar extensas

portabilidad

ineractividad

comunidad activa.

en la unidad emos visto varios programas que nos an ayudado a ver todo lo que es la estructura de python

y hemos visto algunas interfaces como:

'registrar nombre telefono y direccion' 

con este interfaz aprendimos a utilizar lo que son: label, entradas, mensajes de caja, buttons, la condicional if y libreria tkinter

import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    
    if nombre and direccion and telefono:
        with open('registros.txt', 'a') as file:
            file.write("Nombre: {nombre}\n")
            file.write("Direccion: {direccion}\n")
            file.write("Telefono: {telefono}\n")
            file.write("-" * 40 + "\n")
            
            
        entry_nombre.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        
        messagebox.showinfo("informacion", "datos registrados")
        messagebox.showwarning("advertencia", "todos los campos son obligatorios")

#definicion de interfaz, espacio de trabajo       
root = tk.Tk()
root.title("Registradora de datos")
root.geometry("400x300")

label = tk.Label(root, text="nombre")
label.pack(pady= 5)


entry_nombre = tk.Entry(root)
entry_nombre.pack(pady= 5)

label = tk.Label(root, text="telefono")
label.pack(pady= 5)

entry_telefono = tk.Entry(root)
entry_telefono.pack(pady= 5)

label = tk.Label(root, text="dirección")
label.pack(pady= 5)

entry_direccion = tk.Entry(root) 
entry_direccion.pack(pady= 5)


button = tk.Button(root, text="presionar boton", command=messagebox)
button.pack(pady= 5)



root.mainloop()
