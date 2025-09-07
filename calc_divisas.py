import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#Creo un diccionario de divisas
directorio_imágen = os.path.dirname(__file__)
ícono = os.path.join(directorio_imágen, "imagenes","ícono conversión.ico")

##Este es un diccionario de divisas
divisas = {
     "Peso argentino":"1",
     "Real brasileño":"250",
     "Dólar estadounidense":"1400",
     "Euro":"1500",
     "Guaraní paraguayo":"0.17"
}

#Esta es la función principal
def calculadora_de_divisas():
     global ventana
     try:
          if "ventana" in globals() and ventana.winfo_exists():
               ventana.lift()
               return
     except:
          pass
     ventana = tk.Toplevel()
     ventana.title("Conversor de divisas")
     ventana.geometry("700x500")
     ventana.config(bg="white")
     ventana.resizable(False, False)
     ventana.iconbitmap(ícono)
     ventana.columnconfigure(0, weight=1)
     cajas_de_texto(ventana)
     ventana.bind("<Return>", lambda e: convertir_divisas())
     return ventana

#Esta función guarda las cajas de texto para convertir el valor de divisas
def cajas_de_texto(ventana):
     global entry_monto, origen, destino, conversión_variable
     from calculadora_principal import formatearEntrada, color
     color_padre = ventana.cget('bg')
     entry_monto = tk.Entry(ventana, font=("Courier New", 20), bd=4, justify="left")
     entry_monto.config(state="normal")
     entry_monto.pack(pady=10)
     entry_monto.bind("<KeyRelease>", lambda e: formatearEntrada(entry_monto))
     tk.Label(ventana, text="Monto a ingresar", font=("Courier New", 20), bg=color_padre).pack()
     
     tk.Label(ventana, text="Convertir de:", font=("Courier New", 20), bg=color_padre).pack()
     origen = ttk.Combobox(ventana, values = list(divisas.keys()), font=("Courier New", 20), state="readonly")
     origen.set(list(divisas.keys())[0])
     origen.pack(pady=20)

     #Tasa a ingresar
     tk.Label(ventana, text="a:", font=("Courier New", 20), bg=color_padre).pack()
     destino = ttk.Combobox(ventana, values = list(divisas.keys()), font=("Courier New", 20), state="readonly")
     destino.set(list(divisas.keys())[1])
     destino.pack()
     
     tk.Button(ventana, text="Invertir", font=("Courier New", 20), command=convertir_divisas, bg=color["verde_oscuro"], fg="white").pack(pady=20)
     
     #Resultado esperado
     conversión_variable = tk.StringVar()
     tk.Label(ventana, textvariable=conversión_variable, font=("Courier New", 20, "bold"), bg=color_padre, fg=color["verde_oscuro"]).pack()
     
#Este calcula las divisas según lo planeado
def convertir_divisas():
     try:
          from calculadora_principal import formatearNúmeroResultado
          # Verifica si el widget sigue existiendo antes de acceder
          if not entry_monto.winfo_exists():
               conversión_variable.set("⚠️ La ventana fue cerrada.")
               return
          
          símbolo = {
               "Peso argentino": "$",
               "Real brasileño": "R$",
               "Dólar estadounidense": "USD$",
               "Euro": "€",
               "Guaraní paraguayo": "₲"
          }
          
          monto_str = entry_monto.get().strip().replace(".", "").replace(",", ".")
          if monto_str == "":
               
               conversión_variable.set("⚠️ Ingresá un número.")
               return
          de = origen.get()
          a = destino.get()
          
          monto_valor = str(monto_str)
          monto_origen = float(monto_valor) * float(divisas[de])
          conversión = monto_origen/float(divisas[a])
          conversión_variable.set(f"{símbolo[a]} {formatearNúmeroResultado(conversión)}")
     except ValueError:
          conversión_variable.set("⚠️ INGRESÁ UN NÚMERO VÁLIDO.")
