import os
from tkinter import *

#Creo un diccionario de divisas
directorio_imágen = os.path.dirname(__file__)
ícono = os.path.join(directorio_imágen, "imagenes","ícono conversión.ico")


#Esta es la función principal
def calculadora_de_divisas():
     global ventana
     ventana = Tk()
     ventana.title("Conversor de divisas")
     ventana.geometry("600x300")
     ventana.config(bg="white")
     ventana.resizable(False, False)
     ventana.iconbitmap(ícono)
     ventana.columnconfigure(0, weight=1)
     cajas_de_texto(ventana)
     # ventana.bind("<Return>", lambda event: convertir_divisas())
     return ventana

#Esta función guarda las cajas de texto para convertir el valor de divisas
def cajas_de_texto(ventana):
     global entry_monto, entry_tasa, conversión_variable
     #Monto a ingresar
     entry_monto = Entry(ventana, font=("Century", 10), bd=4, justify="left")
     entry_monto.config(state="normal")
     entry_monto.grid(row=0, column=1, padx=10, pady=10)
     Label(ventana, text="Monto a ingresar", font=("Century", 10), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")

     #Tasa a ingresar
     entry_tasa = Entry(ventana, font=("Century", 10), bd=4, justify="left")
     entry_tasa.config(state="normal")
     entry_tasa.grid(row=1, column=1, padx=10, pady=60, sticky="we")
     Label(ventana, text="Tasa a ingresar", font=("Century", 10), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
     
     #Resultado esperado
     conversión_variable = StringVar()
     Label(ventana, text="Resultado", font=("Century", 20), bg="white", fg="green").grid(row=2, column=0, padx=10, pady=70, sticky="w")
     Label(ventana, textvariable=conversión_variable, font=("Century", 20), bg="white", fg="green").grid(row=3, column=1)
     
divisa = calculadora_de_divisas()

#Este calcula las divisas según lo planeado
def convertir_divisas():
     try:
          monto_valor = float(entry_monto.get())
          tasa_valor = float(entry_tasa.get())
          conversión = monto_valor/tasa_valor
          conversión_variable.set(f"{conversión:.2f}")
     except ValueError:
          conversión_variable.set("ALGO SALIÓ MUY MAL")

divisa.mainloop()

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
