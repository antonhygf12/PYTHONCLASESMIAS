import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mostrarmensaje():
     messagebox.showinfo("informacion", "esto es un mensaje de prueba")

root = tk.Tk() 
root.title("widgets mas usados de tkinter") 
root.geometry("600x600")

label = tk.Label(root, text="esto es una etiqueta de texto")

label.pack(pady= 5)



button = tk.Button(root, text="presionar boton", command=mostrarmensaje)
button.pack(pady= 5)



entry = tk.Entry(root)

entry.pack(pady = 5)




textbox = tk.Text(root, height= 4, width= 40)
textbox.pack(pady = 5)




listbox = tk.Listbox(root)

listbox.insert(1, "elemento 1")

listbox.insert(2, "elemento 2")
listbox.insert(3, "elemento 3")
listbox.pack(pady= 5)


progressbar = ttk.Progressbar(root, orient= "horizontal", length= 200, mode= "determinate")

progressbar.pack(pady = 5)

progressbar['value'] = 50



notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text="pestaÃ±a 1")

notebook.add(frame2, text= "pestaÃ±a 2")
notebook.pack(pady= 5)


spinbox = tk.Spinbox(root, from_= 0, to = 10)

spinbox.pack(pady=5)


root.mainloop() 