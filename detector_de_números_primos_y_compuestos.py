from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto
import os

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
                lbResultado.config(text=f"{valor} es un número primo", fg="red")
            else:
                lbResultado.config(text=f"{valor} es un número compuesto", fg="green")
        else:
            mensajeDeTexto.showwarning("ADVERTENCIA", "El valor no debe ser 0 ni 1 si querés saber que números es primo y compuesto")
        
    except ValueError:
        mensajeDeTexto.showerror("Error", "Por favor ingrese un número válido")

interfaz = tk.Tk()
interfaz.title("Número primo o compuesto")
interfaz.geometry("450x200")
interfaz.config(bg="white")
interfaz.iconbitmap(icono)
interfaz.resizable(False, False)


entryNúmero = tk.Entry(interfaz, font=("Courier New", tamañoLetra, "bold"), bd=4)
entryNúmero.pack(anchor="center")

btnDetectar = tk.Button(interfaz, text="Detectar", font=("Courier New", tamañoLetra, "bold"), bg="blue", fg="white", bd=1, cursor="hand2", command=detectar_primo)
btnDetectar.pack(side="bottom", pady=10)
btnDetectar.bind("<Enter>", lambda e: btnDetectar.config(bg="red"))
btnDetectar.bind("<Leave>", lambda e: btnDetectar.config(bg="blue"))


lbResultado = tk.Label(interfaz, font=("Courier New", tamañoLetra, "bold"), bg="white")
lbResultado.pack(pady=5)

interfaz.mainloop()