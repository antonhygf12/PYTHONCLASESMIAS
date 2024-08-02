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
´´´
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
´´´

en el siguiente programa nos enseño en esta unidad que podemos hacer que un programa tenga un numero como base y no reconozca a los demas 

este programa esta conformado por, libreria tkinter, labels, buttons, entrys y cajas de texto y tiene como base al número 5 y si se ingresa algun otro va a responder con 
valor no asignado 

'''

import tkinter as tk 
from tkinter import messagebox

def guardar_datos():
    numero = entry_numero.get()

    if numero ==5:
         messagebox.showinfo("informacion","pueba tecnica supeada")

    else:
      
        messagebox.showwarning("advertencia","valor no asignado")
     
root = tk.Tk()
root.title("prueba tecnica 1")
root.geometry("400x300")

label = tk.Label(root, text="ingresa el número correspondiente")
label.pack(pady= 5)


entry_numero = tk.Entry()
entry_numero.pack(pady= 5)


button = tk.Button(root, text="ejecutar", command=messagebox)
button.pack(pady= 5)




root.mainloop()

'''


uno de los ultimos prgramas q vimos fue a usar la libreria "random" y el ".choice"  
la función que tiene este programa nada más es tirar mensajes aleatorios puestos por el usuario y asignados una una variable de distinto nombre 

'''
import random
diccionario={
    'clave': "hola",
    'clave1': "que tal",
    'clave2': "bien"
    
} 
Variable= random.choice(list(diccionario.values()))
print(Variable)
'''



aqui concluye un poco de lo que fatima y yo (antonio) emos aprendido esta unidad 
agradecidos con su persona y perdone si no es mucho.
