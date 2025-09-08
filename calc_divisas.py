import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#Creo un diccionario de divisas
directorio_imágen = os.path.dirname(__file__)
ícono = os.path.join(directorio_imágen, "imagenes","ícono conversión.ico")

##Este es un diccionario de divisas
divisas = {
    "peso argentino": {
        "valor": 1.0,
        "imagen": "peso argentino.png"
    },
    "real brasileño": {
        "valor": 260.0,
        "imagen": "real.png"
    },
    "dólar estadounidense": {
        "valor": 1420.0,
        "imagen": "dólar.png"
    },
    "euro": {
        "valor": 1500.0,
        "imagen": "euro.png"
    },
    "guaraní paraguayo": {
        "valor": 0.17,
        "imagen": "guaraní.png"
    }
}

def cargar_imagen(nombre_imágen):
     rutaCompleta = os.path.join(directorio_imágen, "imagenes", nombre_imágen)
     if not os.path.exists(rutaCompleta):
          print(f"La imágen no se encuentra en esta ruta {rutaCompleta}")
          return None
     else:
          try:
               imágen = Image.open(rutaCompleta).resize((30, 30))
               return ImageTk.PhotoImage(imágen)
          except Exception as e:
               print(f"Error al cargar la imagen: {e}")
               return None

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

     ventana.invertir = cargar_imagen("invertir.png")
     ventana.imagenes = {}
     for nombre_divisa, datos in divisas.items():
        if "imagen" in datos:
          ventana.imagenes[nombre_divisa] = cargar_imagen(datos["imagen"])

     cajas_de_texto(ventana)
     ventana.bind("<Return>", lambda e: convertir_divisas())
     
     return ventana

#Esta función guarda las cajas de texto para convertir el valor de divisas
def cajas_de_texto(ventana):
     from calculadora_principal import color
     from calculadora_principal import formatearEntrada
     global entry_monto, origen, destino, conversión_variable, etiquetaDestino, etiquetaOrigen
     color_padre = ventana.cget('bg')
    
     etiquetaOrigen = tk.Label(ventana, bg=color_padre)
     etiquetaOrigen.pack()
     etiquetaDestino = tk.Label(ventana, bg=color_padre)
     etiquetaDestino.pack()

     entry_monto = tk.Entry(ventana, font=("Courier New", 20), bd=4, justify="left")
     entry_monto.config(state="normal")
     entry_monto.pack(pady=10)
     entry_monto.bind("<KeyRelease>", lambda e: formatearEntrada(entry_monto))

     
     # from calculadora_principal import formatearEntrada
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

     origen.bind("<<ComboboxSelected>>", lambda e: actualizar_imagen(e, origen, etiquetaOrigen))

     #Tasa a ingresar
     tk.Label(ventana, text="a", font=("Courier New", 20), bg=color_padre).pack()
     destino = ttk.Combobox(ventana, values = list(divisas.keys()), font=("Courier New", 20), state="readonly")
     destino.set(list(divisas.keys())[1])
     destino.pack()
     destino.bind("<<ComboboxSelected>>", lambda e: actualizar_imagen(e, destino, etiquetaDestino))

     # Crear un frame para ubicar el botón a la derecha
     frmInvertir = tk.Frame(ventana, bg=color_padre)
     frmInvertir.place(relx=1.0, rely=1.0, x=-50, y=-225, anchor="se")

     tk.Button(frmInvertir, image=ventana.invertir, command=invertir_divisas, bg=color_padre).pack()
     #Resultado esperado
     conversión_variable = tk.StringVar()
     tk.Label(ventana, textvariable=conversión_variable, font=("Courier New", 20, "bold"), bg=color_padre, fg=color["verde_oscuro"]).pack()
 
#Este calcula las divisas según lo planeado
def convertir_divisas():
     try:
          from calculadora_principal import formatearNúmeroResultado
     #Tasa a ingresar
     tk.Label(ventana, text="a:", font=("Courier New", 20), bg=color_padre).pack()
     destino = ttk.Combobox(ventana, values = list(divisas.keys()), font=("Courier New", 20), state="readonly")
     destino.set(list(divisas.keys())[1])
     destino.pack()
     
     tk.Button(ventana, text="Invertir", font=("Courier New", 20), command=convertir_divisas, bg=color["verde_oscuro"], fg="white").pack(pady=20)
     
     tk.Button(ventana, image=ventana.invertir, bg=color_padre).pack(padx=60)
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
               "peso argentino": "$",
               "real brasileño": "R$",
               "dólar estadounidense": "USD$",
               "euro": "€",
               "guaraní paraguayo": "₲"
          }
          
          monto_str = entry_monto.get().strip().replace(".", "").replace(",", ".")
          if monto_str == "":
               conversión_variable.set("⚠️ Ingresá un número.")
               return
          de = origen.get()
          a = destino.get()

          monto_valor = float(monto_str)
          monto_origen = monto_valor * divisas[de]["valor"]
          conversión = monto_origen/divisas[a]["valor"]
          conversión_variable.set(f"{símbolo[a]} {formatearNúmeroResultado(conversión)}")
     except ValueError:
          conversión_variable.set("⚠️ INGRESÁ UN NÚMERO VÁLIDO.")

#Esta función es para invertir la divisa según corresponda
def invertir_divisas():
     val_destino = destino.get() #este es un valor obtenido del dinero convertido
     val_origen = origen.get() #este es un valor obtenido del dinero convertido
     
     origen.set(val_destino)
     destino.set(val_origen)
     
     convertir_divisas()


def actualizar_imagen(evento, comboboxWidget, etiquetaImagen):
     divisaSeleccionada = comboboxWidget.get()
     imagen = ventana.imagenes.get(divisaSeleccionada)
     if imagen:
          etiquetaImagen.config(image=imagen)
          etiquetaImagen.image = imagen
     else:
          etiquetaImagen.config(image='')
          etiquetaImagen.image = None

