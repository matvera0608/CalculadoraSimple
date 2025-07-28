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
     "PYG":"0.17"
}

#Esta es la función principal
def calculadora_de_divisas():
     global ventana
     try:
          if "ventana" in globals() and ventana.winfo_exists():
               ventana.lift()
               return
     except:
          pass  # por si ventana ya fue destruida
     
     ventana = tk.Toplevel()
     ventana.title("Conversor de divisas")
     ventana.geometry("600x300")
     ventana.config(bg="white")
     ventana.resizable(False, False)
     ventana.iconbitmap(ícono)
     ventana.columnconfigure(0, weight=1)
     cajas_de_texto(ventana)
     if entry_monto.winfo_exists():
          entry_monto.bind("<Return>", lambda e: convertir_divisas())
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
          from calculadora_principal import formatearNúmeroResultado
          # Verifica si el widget sigue existiendo antes de acceder
          if not entry_monto.winfo_exists():
               conversión_variable.set("⚠️ La ventana fue cerrada.")
               return
          monto_str = entry_monto.get().strip().replace(",", ".")
          if monto_str == "":
               conversión_variable.set("⚠️ Ingresá un número.")
               return
          de = origen.get()
          a = destino.get()
          
          monto_valor = str(monto_str)
          monto_origen = float(monto_valor) * float(divisas[de])
          conversión = monto_origen/float(divisas[a])
          conversión_variable.set(formatearNúmeroResultado(conversión))
          
     except ValueError:
          conversión_variable.set("⚠️ INGRESÁ UN NÚMERO VÁLIDO.")


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
