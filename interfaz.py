import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
class Formulario:
    def __init__(self):
        try:
            # Crear la ventana principal
            self.base = tk.Tk()
            self.base.title("Formulario")
            self.base.geometry("1300x400")


            groupBox1 = tk.LabelFrame(self.base, text="Datos del personal", padx=15, pady=15)
            groupBox1.grid(row=0, column=0, padx=10, pady=10)
            

            labelid = tk.Label(groupBox1, text="Id:", width=10,font=("Arial", 12)).grid(row=0, column=0,)
            texBoxid = tk.Entry(groupBox1, width=20, font=("Arial", 12))
            texBoxid.grid(row=0, column=1, padx=5, pady=5)            
            
            labelNombre = tk.Label(groupBox1, text="Nombres:", width=10,font=("Arial", 12)).grid(row=1, column=0,)
            texBoxNombre = tk.Entry(groupBox1, width=20, font=("Arial", 12))
            texBoxNombre.grid(row=1, column=1, padx=5, pady=5)

            labelApellidos = tk.Label(groupBox1, text="Apellidos:", width=10,font=("Arial", 12)).grid(row=2, column=0,)
            texBoxApellidos = tk.Entry(groupBox1, width=20, font=("Arial", 12))
            texBoxApellidos.grid(row=2, column=1,padx=5, pady=5)

            labelcc = tk.Label(groupBox1, text="CC:", width=10,font=("Arial", 12)).grid(row=0, column=0,)
            texBoxcc = tk.Entry(groupBox1, width=20, font=("Arial", 12))
            texBoxcc.grid(row=0, column=1, padx=5, pady=5)

            labelCargo = tk.Label(groupBox1, text="Cargo:", width=10,font=("Arial", 12)).grid(row=3, column=0,)
            seleccionCargo = tk.StringVar()
            combo= ttk.Combobox(groupBox1,values=[ "Malacatero", "Minero", "Administrativo"], textvariable=seleccionCargo, width=17, font=("Arial", 12))
            combo.grid(row=3, column=1,)
            seleccionCargo.set("Seleccione un cargo")

            Button(groupBox1, text="Guardar", width=10, font=("Arial", 12)).grid(row=4, column=0)
            Button(groupBox1, text="Modificar", width=10, font=("Arial", 12)).grid(row=4, column=1)
            Button(groupBox1, text="Eliminar", width=10, font=("Arial", 12)).grid(row=4, column=2)

            groupBox2 = tk.LabelFrame(self.base, text="lista de personal", padx=5, pady=5)
            groupBox2.grid(row=0, column=1, padx=5, pady=5)

            # Crear un árbol de vista (Treeview) para mostrar la lista de personal







            # Configurar las columnas
            tree = ttk.Treeview(groupBox2, columns=("id", "nombres", "apellidos", "cargo"), show="headings", height=15)
            tree.column("#1", anchor="center")
            tree.heading("#1", text="Id")
            tree.column("#2", anchor="center")
            tree.heading("#2", text="Nombres")
            tree.column("#3", anchor="center")
            tree.heading("#3", text="Apellidos")
            tree.column("#4", anchor="center")
            tree.heading("#4", text="Cargo")

            tree.pack()







            # Aquí puedes agregar widgets adicionales si es necesario

            self.base.mainloop()

        except ValueError as e:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Crear una instancia de la clase Formulario para mostrar la interfaz
Formulario()