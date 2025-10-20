import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#Creo un diccionario de divisas
directorio_imágen = os.path.dirname(__file__)
ícono = os.path.join(directorio_imágen, "imagenes", "íconos", "ícono conversión.ico")

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
    "dólar": {
        "valor": 1425.0,
        "imagen": "dólar.png"
    },
    "euro": {
        "valor": 1750.0,
        "imagen": "euro.png"
    },
    "guaraní": {
        "valor": 0.15,
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
     from calculadora_principal import formatearEntrada, escribirCeros, borrarTODO
     global entry_monto, origen, destino, conversión_variable, etiquetaDestino, etiquetaOrigen, color_padre
     color_padre = ventana.cget('bg')
     

     entry_monto = tk.Entry(ventana, font=("Courier New", 20), bd=4, justify="left")
     entry_monto.config(state="normal")
     entry_monto.pack(pady=10)
     entry_monto.bind("<Control-BackSpace>", lambda e: borrarTODO(entry_monto))
     entry_monto.bind("<KeyRelease>", lambda e: formatearEntrada(entry_monto))
     entry_monto.bind("<Alt-0>", lambda e: escribirCeros(entry_monto, "00"))
     entry_monto.bind("<Control-0>", lambda e: escribirCeros(entry_monto, "000"))

     tk.Label(ventana, text="Monto a ingresar", font=("Courier New", 20), bg=color_padre).pack()
     
     tk.Label(ventana, text="Convertir de", font=("Courier New", 20), bg=color_padre).pack()
     
     frm_Origen = tk.Frame(ventana, bg=color_padre)
     frm_Origen.pack(pady=10)
     
     etiquetaOrigen = tk.Label(frm_Origen, bg=color_padre)
     etiquetaOrigen.pack(side="left", padx=5)
     
     origen = ttk.Combobox(frm_Origen, values = list(divisas.keys()), font=("Courier New", 20), state="readonly")
     origen.set(list(divisas.keys())[0])
     origen.pack(side="left", configure=actualizar_imagen("<Configure>", origen, etiquetaOrigen))
     origen.bind("<<ComboboxSelected>>", lambda e: actualizar_imagen(e, origen, etiquetaOrigen))
     
     #Tasa a ingresar
     tk.Label(ventana, text="a", font=("Courier New", 20), bg=color_padre).pack()
     
     frm_Destino = tk.Frame(ventana, bg=color_padre)
     frm_Destino.pack(pady=10)
     
     etiquetaDestino = tk.Label(frm_Destino, bg=color_padre)
     etiquetaDestino.pack(side="left", padx=5)
     
     destino = ttk.Combobox(frm_Destino, values = list(divisas.keys()), font=("Courier New", 20), state="readonly")
     destino.set(list(divisas.keys())[1])
     destino.pack(side="left", configure=actualizar_imagen("<Configure>", destino, etiquetaDestino))
     destino.bind("<<ComboboxSelected>>", lambda e: actualizar_imagen(e, destino, etiquetaDestino))

     frmConvertir = tk.Frame(ventana, bg=color_padre)
     frmConvertir.pack(fill="x", pady=5)


     btnInvertir = tk.Button(frm_Destino, image=ventana.invertir, bg=color_padre, command=invertir_divisas, cursor="hand2")
     btnInvertir.pack(side="left", padx=10)
     btnInvertir.bind("<Enter>", lambda e: btnInvertir.config(bg=color_padre))
     btnInvertir.bind("<Leave>", lambda e: btnInvertir.config(bg=color_padre))

     btnConvertir = tk.Button(frmConvertir, text="Convertir",font=("Courier New", 20, "bold"), bg=color["verde_claro"], command=convertir_divisas, relief="flat", highlightthickness=0, bd=2, cursor="hand2")
     btnConvertir.pack(anchor="center")
     btnConvertir.bind("<Enter>", lambda e: btnConvertir.config(bg=color["verde_oscuro"]))
     btnConvertir.bind("<Leave>", lambda e: btnConvertir.config(bg=color["verde_claro"]))
     
     #Resultado esperado
     conversión_variable = tk.StringVar()
     tk.Label(ventana, textvariable=conversión_variable, font=("Courier New", 20, "bold"), bg=color_padre, fg=color["verde_oscuro"]).pack()
     
#Este calcula las divisas según lo planeado
def convertir_divisas():
     try:
          from operaciones import formatearNúmeroResultado

          # Verifica si el widget sigue existiendo antes de acceder
          if not entry_monto.winfo_exists():
               conversión_variable.set("⚠️ La ventana fue cerrada.")
               return
          
          símbolo = {
               "peso argentino": "$",
               "real brasileño": "R$",
               "dólar": "USD$",
               "euro": "€",
               "guaraní": "₲"
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
     
     actualizar_imagen(None, origen, etiquetaOrigen)
     actualizar_imagen(None, destino, etiquetaDestino)
     

def actualizar_imagen(evento=None, comboboxWidget=None, etiquetaImagen=None):
     divisaSeleccionada = comboboxWidget.get()
     imagen = ventana.imagenes.get(divisaSeleccionada)
     if imagen:
          etiquetaImagen.config(image=imagen)
          etiquetaImagen.image = imagen
     else:
          etiquetaImagen.config(image='')
          etiquetaImagen.image = None