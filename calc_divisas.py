import tkinter as tk

def convertir_divisa(monto, tasa):
     return monto * tasa

def calculadora_de_divisas():
     ventana = tk.Toplevel()
     ventana.title("Conversor de divisas")
     ventana.geometry("450x200")
     ventana.config(bg="white")
     return ventana