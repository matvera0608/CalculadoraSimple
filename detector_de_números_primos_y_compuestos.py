from tkinter import *
import tkinter as tk
import os

interfaz = tk.Tk()
interfaz.title("Número primo o compuesto")
interfaz.geometry("450x200")
interfaz.config(bg="white")


def es_primo(número):
    if número < 2:
        return False
    for i in range(2, int(número**0.5) + 1):
        if número % i == 0:
            return False
    return True

def detectar_primo():
    try:
        valor = int(PantallaParaEscribirNúmeros.get().replace(".", "").replace(",", "."))
        if es_primo(valor):
            mensajeDeTexto.showinfo("Primo", f"✅ El número {valor} es primo")
        else:
            mensajeDeTexto.showinfo("Primo", f"❌ El número {valor} es compuesto")
    except ValueError:
        mensajeDeTexto.showerror("Error", "Por favor ingrese un número válido")


interfaz.mainloop()