import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk 

class trabajador:
    def __init__(self):
        try:
            # Crear la ventana principal
            self.base = tk.Tk()
            self.base.title("Entrada")
            self.base.geometry("1200x400")

            # Grupo 1: Ingreso de cédula de ciudadanía
            groupBox1 = tk.LabelFrame(self.base, text="Ingreso de cedula de ciudadania", padx=15, pady=15)
            groupBox1.grid(row=0, column=0, padx=10, pady=10)

            labelcc = tk.Label(groupBox1, text="CC:", width=10, font=("Arial", 12))
            labelcc.grid(row=0, column=0)
            texBoxcc = tk.Entry(groupBox1, width=20, font=("Arial", 12))
            texBoxcc.grid(row=0, column=1, padx=5, pady=5)

            # Grupo 2: Observaciones
            groupBox = tk.LabelFrame(self.base, text="Observaciones", padx=15, pady=15)
            groupBox.grid(row=1, column=0, padx=10, pady=10)

            labelObservaciones = tk.Label(groupBox, text="Observaciones sobre los Insumos:", font=("Arial", 12))
            labelObservaciones.grid(row=0, column=0, sticky="w")

            texBoxtext = tk.Text(groupBox, width=50, height=5, font=("Arial", 12))
            texBoxtext.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky="w")

            # Botón Enviar
            btnEnviar = Button(self.base, text="Enviar", font=("Arial", 12), command=self.enviar_datos)
            btnEnviar.grid(row=1, column=1, pady=10, padx=10, sticky="w")

            # Botones con imágenes
            groupBoxButtons = tk.LabelFrame(self.base, text="inventario", padx=15, pady=15)
            groupBoxButtons.grid(row=0, column=1, padx=10, pady=10)

            

            # Cargar imágenes
            img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\sergi\OneDrive - UNIVERSIDAD DE CUNDINAMARCA\Escritorio\P_minas\Imagenes\pico.png").resize((50, 50)))
            img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\sergi\OneDrive - UNIVERSIDAD DE CUNDINAMARCA\Escritorio\P_minas\Imagenes\linterna.png").resize((50, 50)))
            img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\sergi\OneDrive - UNIVERSIDAD DE CUNDINAMARCA\Escritorio\P_minas\Imagenes\casco-de-construccion.png").resize((50, 50)))
            img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\sergi\OneDrive - UNIVERSIDAD DE CUNDINAMARCA\Escritorio\P_minas\Imagenes\bota-de-senderismo.png").resize((50, 50)))

            # Crear botones con imágenes
            btn1 = Button(groupBoxButtons, image=img1, text="Pico", compound="top", width=80, height=80)
            btn1.grid(row=0, column=0, padx=10, pady=10)

            btn2 = Button(groupBoxButtons, image=img2, text="Linterna", compound="top", width=80, height=80)
            btn2.grid(row=0, column=1, padx=10, pady=10)

            btn3 = Button(groupBoxButtons, image=img3, text="Casco", compound="top", width=80, height=80)
            btn3.grid(row=0, column=2, padx=10, pady=10)

            btn4 = Button(groupBoxButtons, image=img4, text="Botas", compound="top", width=80, height=80)
            btn4.grid(row=0, column=3, padx=10, pady=10)

            self.img1 = img1
            self.img2 = img2
            self.img3 = img3
            self.img4 = img4

            # Crear un árbol de vista (Treeview) para mostrar la lista de personal

            self.base.mainloop()

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def enviar_datos(self):
        #"Enviar"

        messagebox.showinfo("Información", "Datos enviados correctamente.")

trabajador()