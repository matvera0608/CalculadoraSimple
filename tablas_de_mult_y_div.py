from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto
import os
from calculadora_principal import color

dir_imagen = os.path.dirname(__file__)
icono = os.path.join(dir_imagen, "imagenes", "íconos", "ícono tabla mul y div.ico")

def calcular():
     try:
          núm = int(entryNúmero.get().strip())
          lím = int(entryLímite.get().strip())
          
          tx_Resultado.config(state="normal")
          tx_Resultado.delete("1.0", tk.END)
          
          tx_Resultado.insert(tk.END, "TABLA DE MULTIPLICAR\n", "titulo")
          for index in range(1, lím+1):
               tx_Resultado.insert(tk.END, f"{núm} × {index} = {núm * index}\n", "titulo")
          
     except ValueError:
          mensajeDeTexto.showerror("Error", "Algo no está bien")
    

interfaz = tk.Tk()
interfaz.title("Tabla de multiplicación o división")
interfaz.config(bg="white")
interfaz.iconbitmap(icono)
interfaz.resizable(False, False)

color_fondo = interfaz.cget('bg')

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
tx_Resultado.tag_configure("titulo", foreground=color["azul"], font=("Courier New", 15, "bold"))
tx_Resultado.grid(row=0, column=2, rowspan=3, padx=10, pady=5)
tx_Resultado.config(state="disabled")


btnMostrar = tk.Button(interfaz, text="Mostrar", font=("Courier New", 15, "bold"), bg=color["azul"], fg="white", bd=1, cursor="hand2", command=calcular)
btnMostrar.grid(row=2, column=0, columnspan=2, pady=10)

interfaz.mainloop()