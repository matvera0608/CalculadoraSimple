from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto
import os
from tkinter import ttk
from calculadora_principal import color

"""
watchmedo auto-restart --pattern="*.py" --recursive -- python tablas_de_mult_y_div.py #Este es para vigilar mi programa cada vez que reinicio la ejecución
"""

dir_imagen = os.path.dirname(__file__)
icono = os.path.join(dir_imagen, "imagenes", "íconos", "ícono tabla mul y div.ico")

def calcular():
     try:
          núm = int(entryNúmero.get().strip())
          lím = int(entryLímite.get().strip())
          op = operación.get()
          
          
          tx_Resultado.config(state="normal")
          tx_Resultado.delete("1.0", tk.END)
          
          if op.lower() == "multiplicar":
               tx_Resultado.insert(tk.END, "TABLA DE MULTIPLICAR\n", "multiplicar")
               for index in range(1, lím+1):
                    tx_Resultado.insert(tk.END, f"{núm} × {index} = {núm * index}\n")
               tx_Resultado.config(state="disabled")
          elif op.lower() == "dividir":
               tx_Resultado.insert(tk.END, "TABLA DE DIVIDIR\n", "dividir")
               for index in range(núm * lím, núm - 1, -núm):
                    if index % núm == 0:
                         tx_Resultado.insert(tk.END, f"{index} ÷ {núm} = {index // núm}\n")
               tx_Resultado.config(state="disabled")
          
     except ValueError:
          mensajeDeTexto.showerror("Error", "Algo no está bien")
    

interfaz = tk.Tk()
interfaz.title("Tabla de multiplicación o división")
interfaz.config(bg="white")
interfaz.iconbitmap(icono)
interfaz.resizable(False, False)

color_fondo = interfaz.cget('bg')

operación = ttk.Combobox(interfaz, values=["Multiplicar", "Dividir"], state="readonly")
operación.grid(row=3, column=0, columnspan=2, pady=5)
operación.current(0)

tk.Label(interfaz, text="Número a multi o dividir: ", bg=color_fondo).grid(row=0, column=0, padx=5, pady=5, sticky="w")
entryNúmero = tk.Entry(interfaz, font=("Courier New", 15, "bold"), bd=4, width=5)
entryNúmero.grid(row=0, column=1, padx=5, pady=5)

tk.Label(interfaz, text="Límite máximo: ", bg=color_fondo).grid(row=1, column=0, padx=5, pady=5, sticky="w")
entryLímite = tk.Entry(interfaz, font=("Courier New", 15, "bold"), bd=4, width=5)
entryLímite.grid(row=1, column=1, padx=5, pady=5)

# marco = tk.Frame(interfaz, bg=color_fondo, bd=2, relief="groove")
# marco.grid(row=0, column=2, padx=10, pady=10, sticky="nsew", rowspan=2)

tx_Resultado = tk.Text(interfaz, width=30, height=15, font=("Courier New", 15, "bold"), state="disabled")
# desplazador = tk.Scrollbar(marco, command=texto.yview)
# desplazador.pack(side="right", fill="y")
tx_Resultado.tag_configure("multiplicar", foreground=color["azul"], font=("Courier New", 15, "bold"), justify="center")
tx_Resultado.grid(row=0, column=2, rowspan=4, padx=10, pady=5)
tx_Resultado.config(state="disabled")
tx_Resultado.tag_configure("dividir", foreground=color["rojo"], font=("Courier New", 15, "bold"), justify="center")
tx_Resultado.grid(row=0, column=2, rowspan=4, padx=10, pady=5)
tx_Resultado.config(state="disabled")

btnMostrar = tk.Button(interfaz, text="Mostrar", font=("Courier New", 15, "bold"), bg=color["azul"], fg="white", bd=1, cursor="hand2", command=calcular)
btnMostrar.grid(row=2, column=0, columnspan=2, pady=10)

interfaz.mainloop()