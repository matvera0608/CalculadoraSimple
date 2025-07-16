from tkinter import *

#Creo un diccionario de divisas
divisas = {
     "USD": 1326,
     "BRL": 231,
     "PYG": 0.16
}

#Esta es la función principal
def calculadora_de_divisas():
     global ventana
     ventana = Tk()
     ventana.title("Conversor de divisas")
     ventana.geometry("450x300")
     ventana.config(bg="white")
     ventana.resizable(False, False)
     cajas_de_texto(ventana)
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

     conversión_variable = StringVar()
     Label(ventana, textvariable=conversión_variable, font=("Century", 12), bg="white", fg="green").grid(row=3, column=0, columnspan=2)
     
divisa = calculadora_de_divisas()

#Este calcula las divisas según lo planeado
def convertir_divisas():
     try:
          monto_valor = float(entry_monto.get())
          tasa_valor = float(entry_tasa.get())
          conversión = monto_valor/tasa_valor
          conversión_variable.set(f"resultado esperado: {conversión:.2f}")
     except ValueError as err_val:
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
