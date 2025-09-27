from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto
from tkinter import ttk
import os
"""
watchmedo auto-restart --pattern="*.py" --recursive -- python detector_de_números_primos_y_compuestos.py #Este es para vigilar mi programa cada vez que reinicio la ejecución
"""
dir_imagen = os.path.dirname(__file__)
icono = os.path.join(dir_imagen, "imagenes", "íconos", "ícono detector.ico")

tamañoLetra = 15

def es_primo(número):
    if número < 2:
        return False
    for i in range(2, int(número**0.5) + 1):
        if número % i == 0:
            return False
    return True

def detectar_primo():
    try:
        valor = int(entryNúmero.get().strip().replace(".", "").replace(",", "."))
        if valor >= 2:
            if es_primo(valor):
                texto.config(text=f"{valor} es un número primo", fg="red")
            else:
                texto.config(text=f"{valor} es un número compuesto", fg="green")
        else:
            mensajeDeTexto.showwarning("ADVERTENCIA", "El valor no debe ser 0 ni 1 si querés saber que números es primo y compuesto")
        
    except ValueError:
        mensajeDeTexto.showerror("Error", "Por favor ingrese un número válido")

def mostrar_todos_los_divisores_compuestos():
    valor = int(entryNúmero.get().strip().replace(".", "").replace(",", "."))
    if valor >= 2 and not es_primo(valor):
        texto.config(text=f"Los divisores de {valor} son:")
    else:
        mensajeDeTexto.showwarning("ADVERTENCIA", "El valor no debe ser 0 ni 1 si querés saber que números es primo y compuesto")
    


interfaz = tk.Tk()
interfaz.title("Número primo o compuesto")
interfaz.geometry("600x200")
interfaz.config(bg="white")
interfaz.iconbitmap(icono)
interfaz.resizable(False, False)

marco = tk.Frame(interfaz)
marco.pack(padx=10, pady=10, fill="both", expand=True)

entryNúmero = tk.Entry(marco, font=("Courier New", tamañoLetra, "bold"), bd=4)

entryNúmero.grid(row=0, column=0, padx=10, pady=10, sticky="w")


texto = tk.Text(marco, width=30, height=10, font=("Courier New", tamañoLetra, "bold"), wrap="word")
texto.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
texto.config(state="disabled")

btnDetectar = tk.Button(marco, text="Detectar", font=("Courier New", tamañoLetra, "bold"), bg="blue", fg="white", bd=1, cursor="hand2", command=detectar_primo)
btnDetectar.grid(row=1, column=0, columnspan=2,padx=0, pady=20, sticky="w")
btnDetectar.bind("<Enter>", lambda e: btnDetectar.config(bg="red"))
btnDetectar.bind("<Leave>", lambda e: btnDetectar.config(bg="blue"))

interfaz.mainloop()