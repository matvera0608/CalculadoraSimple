from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto, tkinter.font as fuenteDeLetra, tkinter.simpledialog as diálogo
from calculadora_principal import calculadora

def convertir_divisa(monto, tasa):
     return monto * tasa

def calculadora_de_divisas():
     ventana = tk.Tk()
     ventana.title("Conversor de divisas")
     ventana.geometry("450x200")
     ventana.config(bg="white")
     
     return ventana

divisa = calculadora_de_divisas()

divisa.mainloop()