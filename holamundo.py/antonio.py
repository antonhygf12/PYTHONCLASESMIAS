import tkinter as tk 
from tkinter import mesagebox   

def mensaje ()
mesagebox showinfo ("nombre de la caja de texto", "mensaje" )
root = tk.Tk ()
root.title("interfaz simple")
root.geometry("300*200")
boton=tk.Button(root,text="haz clic aqui", comando mensaje)
boton.pack(pady=20)
root.main loop
