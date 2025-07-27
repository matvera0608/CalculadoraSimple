import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
#Creo un diccionario de divisas
directorio_imágen = os.path.dirname(__file__)
ícono = os.path.join(directorio_imágen, "imagenes","ícono conversión.ico")

##Este es un diccionario de divisas
divisas = {
     "ARS":"1",
     "BRL":"230",
     "USD":"1320",
     "EUR":"1500",
     "PYG":"0.11"
}

#Esta es la función principal
def calculadora_de_divisas():
     global ventana
     ventana = tk.Toplevel()
     ventana.title("Conversor de divisas")
     ventana.geometry("600x300")
     ventana.config(bg="white")
     ventana.resizable(False, False)
     ventana.iconbitmap(ícono)
     ventana.columnconfigure(0, weight=1)
     cajas_de_texto(ventana)
     ventana.bind("<Return>", lambda event: convertir_divisas())
     return ventana

#Esta función guarda las cajas de texto para convertir el valor de divisas
def cajas_de_texto(ventana):
     global entry_monto, origen, destino, conversión_variable
     #Monto a ingresar
     entry_monto = tk.Entry(ventana, font=("Century", 10), bd=4, justify="left")
     entry_monto.config(state="normal")
     entry_monto.pack(pady=5)
     tk.Label(ventana, text="Monto a ingresar", font=("Century", 10), bg="white").pack()
     
     tk.Label(ventana, text="Convertir de:", font=("Century", 12)).pack()
     origen = ttk.Combobox(ventana, values = list(divisas.keys()), font=("Century", 10), state="readonly")
     origen.set("ARS")
     origen.pack()

     #Tasa a ingresar
     tk.Label(ventana, text="A:", font=("Century", 12)).pack()
     destino = ttk.Combobox(ventana, values = list(divisas.keys()), font=("Century", 10), state="readonly")
     destino.set("")
     destino.pack()
     
     
     #Resultado esperado
     conversión_variable = tk.StringVar()
     tk.Label(ventana, textvariable=conversión_variable, font=("Century", 20), bg="white", fg="green").pack()
     
#Este calcula las divisas según lo planeado
def convertir_divisas():
     try:
          from calculadora_principal import formatearEntrada, formatearNúmero
          # Verifica si el widget sigue existiendo antes de acceder
          if entry_monto.winfo_exists():
               monto_str = formatearEntrada(entry_monto.get())
               de = origen.get()
               a = destino.get()
               
               monto_valor = float(monto_str)
               monto_origen = monto_valor * float(divisas[de])
               conversión = monto_origen/float(divisas[a])
               conversión_variable.set(formatearNúmero(conversión))
     except ValueError:
          conversión_variable.set("⚠️ INGRESÁ UN NÚMERO VÁLIDO.")
     except tk.TclError:
          conversión_variable.set("⚠️ La ventana fue cerrada.")


# 📜 Lista de valores de sticky:
# Valor   Significado
# "n"     Norte → arriba
# "s"     Sur → abajo
# "e"     Este → derecha
# "w"     Oeste → izquierda
# "ne"    Arriba a la derecha
# "nw"    Arriba a la izquierda
# "se"    Abajo a la derecha
# "sw"    Abajo a la izquierda
# "ns"    Se estira verticalmente
# "ew"    Se estira horizontalmente
# "nsew"  Se estira completamente (ocupa todo)** ⬅️ más usado
