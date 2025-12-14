import os
from tkinter import *
import tkinter as tk
from operaciones import *
from eventos import *
from diseño import color

""" EN ESTA SECCIÓN DEFINO LAS FUNCIONES DE PANTALLA 
Y BOTONES DE LA CALCULADORA PERSONALIZADA. """

directorio_imágen = os.path.dirname(__file__)
ícono = os.path.join(directorio_imágen, "imagenes", "íconos","ícono.ico")

# -*- coding: utf-8 -*-
#defino la función con valor de devolución o de retorno llamada calculadora()
#que va todos los botones necesarios para los cálculos necesarios

def pantallaCalculadora(ventanaPrincipal):
    global PantallaParaEscribirNúmeros, PantallaParaResultadoEjercicio, PantallaRestoDivisión
    
    # Configurar la grilla principal para permitir redimensionamiento si se desea
    for i in range(6):
        ventanaPrincipal.columnconfigure(i, weight=1)
    for i in range(20):
        ventanaPrincipal.rowconfigure(i, weight=1)


    TamañoFijo = tk.Frame(ventanaPrincipal, width=330, height=120)
    TamañoFijo.grid(row=0, column=0, columnspan=8, sticky="nsew")
    TamañoFijo.grid_propagate(False)  # Impide que el tamaño del Frame se ajuste al contenido
    TamañoFijo.columnconfigure(0, weight=1)
    TamañoFijo.rowconfigure(0, weight=1)
    TamañoFijo.rowconfigure(1, weight=1)
    
    # Pantalla para escribir el número y el resultado
    PantallaParaEscribirNúmeros = Entry(TamañoFijo, font=("Courier New", 30), bg=color["celeste_claro"], fg=color["celeste_oscuro"], bd=4, justify="left")
    PantallaParaEscribirNúmeros.grid(row=0, column=0, sticky="nsew")
    PantallaParaEscribirNúmeros.insert(0, "")
    PantallaParaEscribirNúmeros.focus_set()
    PantallaParaEscribirNúmeros.bind("<Return>", lambda e: Calcular(PantallaParaEscribirNúmeros, PantallaParaResultadoEjercicio, PantallaRestoDivisión))
    PantallaParaEscribirNúmeros.bind("<KeyRelease>", lambda e: formatearEntrada(PantallaParaEscribirNúmeros))
    PantallaParaEscribirNúmeros.bind("<Control-BackSpace>", lambda e: borrarTODO(PantallaParaEscribirNúmeros, PantallaParaResultadoEjercicio, PantallaRestoDivisión))
    PantallaParaEscribirNúmeros.bind("<Alt-0>", lambda e: escribirCeros(PantallaParaEscribirNúmeros,"00"))
    PantallaParaEscribirNúmeros.bind("<Control-0>", lambda e: escribirCeros(PantallaParaEscribirNúmeros,"000"))
    
    
    PantallaParaResultadoEjercicio = Entry(TamañoFijo, font=("Courier New", 30), fg=color["negro"], bd=4, justify="right", state="readonly")
    PantallaParaResultadoEjercicio.grid(row=1, column=0, sticky="nsew")
    PantallaParaResultadoEjercicio.propagate(False)

    # Proporcionalidad del módulo
    ventanaPrincipal.columnconfigure(0, weight=1)
    ventanaPrincipal.columnconfigure(1, weight=1)
    ventanaPrincipal.columnconfigure(2, weight=1)
    ventanaPrincipal.columnconfigure(3, weight=1)
    ventanaPrincipal.columnconfigure(4, weight=1)
    ventanaPrincipal.columnconfigure(5, weight=1)


    módulo = Label(ventanaPrincipal,text="Resto de la división:",font=("Courier New", 10),bg=ventanaPrincipal["bg"],fg=color["negro"])
    módulo.grid(row=2, column=0, columnspan=2, sticky="w")

    PantallaRestoDivisión = Entry(TamañoFijo, width=10, font=("Courier New", 15), bg=color["gris"], fg=color["negro"], bd=4, justify="right", state="readonly")
    PantallaRestoDivisión.grid(row=2, column=0,columnspan=1, pady=(0, 2), sticky="nsew")


#esta función llamada Botón con el argumento puesto para obtener los datos de
#la función ventana principal contiene TODOS LOS BOTONES DE LA CALCULADORA
def Botón(ventanaPrincipal):
    botones = [
        ("00", 0, 0, 1, 2), ("000", 0, 2, 1, 2),
        ("%", 1, 0, 1, 1), ("ⁿ√", 1, 1, 1, 1), ("^", 1, 2, 1, 1), ("÷", 1, 3, 1, 1),
        ("7", 2, 0, 1, 1), ("8", 2, 1, 1, 1), ("9", 2, 2, 1, 1), ("÷÷", 2, 3, 1, 1),
        ("4", 3, 0, 1, 1), ("5", 3, 1, 1, 1), ("6", 3, 2, 1, 1), ("×", 3, 3, 1, 1),
        ("1", 4, 0, 1, 1), ("2", 4, 1, 1, 1), ("3", 4, 2, 1, 1), ("-", 4, 3, 1, 1),
        ("0", 5, 0, 1, 1), (",", 5, 1, 1, 1), ("=", 5, 2, 1, 1), ("+", 5, 3, 1, 1)
    ]
    
    
    def obtener_color_botón(texto):
        if texto == "+":
            return color["rojo"], color["rojo_resaltado"], color["blanco"]
        elif texto == "-":
            return color["amarillo"], color["amarillo_resaltado"], color["blanco"]
        elif texto == "×":
            return color["azul"], color["azul_resaltado"], color["blanco"]
        elif texto == "÷":
            return color["verde"], color["verde_resaltado"], color["blanco"]
        elif texto == "÷÷":
            return color["azul_violáceo"], color["azul_violáceo_resaltado"], color["blanco"]
        elif texto == "^":
            return color["naranja"], color["naranja_resaltado"], color["blanco"]
        elif texto == "ⁿ√":
            return color["violeta"], color["violeta_resaltado"], color["blanco"]
        elif texto == "%":
            return color["negro"], color["negro_resaltado"], color["blanco"]
        elif texto in ("00", "000", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "="):
            return color["beige"], color["beige_resaltado"], color["negro_resaltado"]
        else:
            return color["celeste_claro"], color["celeste_oscuro"], color["blanco"]

    for texto, fila, columna, rowspan, columnspan in botones:
        btn_fondo, btn_fondoResaltado, btn_letra = obtener_color_botón(texto)
        boton = tk.Button(ventanaPrincipal, text=texto, font=("Courier New", 20, "bold"), bg=btn_fondo, fg=btn_letra, activebackground=btn_fondoResaltado, activeforeground=btn_letra,
                          width=4, height=2, command=lambda value=texto: [PantallaParaEscribirNúmeros.insert(END, value), formatearEntrada(entrada_widget=PantallaParaEscribirNúmeros)], relief="flat", highlightthickness=5,
                          bd=0, cursor="hand2")
        boton.grid(row=fila + 4, column=columna + 1, rowspan=rowspan, columnspan=columnspan, padx=2, pady=2, sticky="nsew")
        
        resaltar, restaurar = clickearBotón(boton, btn_fondoResaltado, btn_fondo, btn_letra)
        boton.bind("<ButtonPress-1>", resaltar)
        boton.bind("<ButtonRelease-1>", restaurar)
        boton.bind("<Enter>", lambda e, btn=boton: btn.config(relief="sunken"))
        boton.bind("<Leave>", lambda e, btn=boton: btn.config(relief="flat"))
        if boton["text"] == "=":
            boton.config(command= lambda: Calcular(PantallaParaEscribirNúmeros, PantallaParaResultadoEjercicio, PantallaRestoDivisión))

    for i in range(10):
        ventanaPrincipal.grid_rowconfigure(i, weight=1)
    for j in range(5):
        ventanaPrincipal.grid_columnconfigure(j, weight=1)
        
    ventanaPrincipal.grid_columnconfigure(1, minsize=100)


#Esta función muestra la interfaz de la calculadora principal para la ventana
def calculadora():
    global ventanaPrincipal
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("RamiroCalc")
    ventanaPrincipal.config(bg="white")
    ventanaPrincipal.iconbitmap(ícono)
    ventanaPrincipal.columnconfigure(0, weight=2)

    pantallaCalculadora(ventanaPrincipal)
    Botón(ventanaPrincipal)
    
    ventanaPrincipal.bind("<Alt-l>", abrir__calculadora__de__divisas)
    ventanaPrincipal.bind("<Alt-p>", abrir__calculadora__de__primos)
    
    return ventanaPrincipal


"""Esta función crea la ventana principal de la calculadora.

Returns:
    tkinter.Tk: La ventana principal de la calculadora.
1. Crea una ventana principal con título "Calculadora sencilla".
2. Configura el tamaño de la ventana a 400x700 píxeles
3. Establece el color de fondo de la ventana a blanco.
4. Desactiva la capacidad de cambiar el tamaño de la ventana.
5. Llama a las funciones pantallaCalculadora y Botón para configurar la interfaz de la calculadora.
6. Devuelve la ventana principal para que pueda ser utilizada por otras funciones o métodos
7. La función no toma argumentos y no tiene efectos secundarios fuera de la ventana creada.
8. La función no tiene un valor de retorno explícito, pero devuelve la ventana principal de la calculadora.
9. La función no tiene un valor de retorno explícito, pero devuelve la ventana principal de la calculadora.
10. La función no tiene un valor de retorno explícito, pero devuelve la ventana principal de la calculadora.
11. La función no tiene un valor de retorno explícito, pero devuelve la ventana principal de la calculadora.
12. La función no tiene un valor de retorno explícito, pero devuelve la ventana principal de la calculadora.
"""
""" 
EN ESTA SECCIÓN DEFINO LAS FUNCIONES QUE REALIZAN LOS CÁLCULOS
Y MANEJAN LA LÓGICA DE LA CALCULADORA.
"""

def formatearNúmero(númeroComoTexto):
    #Controlo que no me permita cualquier signo que no sea punto
    try:
        númeroLimpio = númeroComoTexto.replace(".", "").replace(",", ".")
        valor = float(númeroLimpio)
        if valor.is_integer():
            return f"{int(valor):,}".replace(",", ".")
        else:
            parteEntera, parteDecimal = str(valor).split(".")
            parteEntera = f"{int(parteEntera):,}".replace(",", ".")
            return f"{parteEntera},{parteDecimal}"
    except ValueError:
        return "Error"

#voy a crear una función que convierta a tipo float para que ambos
#números lean. Por ejemplo al escribir 1000 me ponga el punto de forma automática
def convertirATipoFloat(texto):
    
    texto_plano = str(texto).strip()
    limpiar_texto = texto_plano.replace(".", "").replace(",", ".")
    
    #crearé un try-except para manejar posible excepción y mantener robusta la conversión
    #así no tener que recibir mensajes molestos de excepción
    try:
        return float(limpiar_texto)
    except ValueError:
        return None

#En esta función solamente se formatea la entrada para la introducción de millares
#cuando presiono los 000 después de presionar un número diferente a 0 me pone automáticamente los puntos
def formatearEntrada(entrada_widget):
    entrada = entrada_widget.get()
    if not entrada:
        return
    entradaProcesada = entrada.replace("÷÷", "//").replace("×", "*").replace("÷", "/")
    signos = ["+", "-", "*", "/", "÷", "÷÷","//", "×" , "%", "^", "ⁿ√"]
    nuevaEntrada = ""
    númeroActual = ""
    i = 0
    
    #Se cambió de for a while, porque este bucle tiene más control. En cambio for solo recorre de a un carácter a la vez, sin saber qué viene después.
    #El while lo que tiene es que a pesar de que hay que crear un índice te deja manejar personalizadamente sin ser de un carácter a la vez.
    while i < len(entradaProcesada):
        # Detectar raíz enésima
        if entradaProcesada[i:i+2] == "ⁿ√":
            if númeroActual.strip():
                númeroFormateado = formatearNúmero(númeroActual.strip())
                if númeroFormateado == "Error":
                    return
                nuevaEntrada += númeroFormateado
                númeroActual = ""
            nuevaEntrada += "ⁿ√"
            i += 2
            continue
        
        caracter = entradaProcesada[i]
        
        #Controlo que el caracter esté en signo para formatear mejor y controlado.
        if caracter in signos or caracter in "(" or caracter in ")":
            
            es_paréntesis_apertura = caracter == "("
            es_paréntesis_cierre = caracter == ")"
            
            if númeroActual.strip():
                númeroFormateado = formatearNúmero(númeroActual.strip())
                if númeroFormateado == "Error":
                    return
                nuevaEntrada += númeroFormateado
                númeroActual = ""
            
            if es_paréntesis_apertura:
                
                
                if nuevaEntrada and (nuevaEntrada[-1].isdigit() or nuevaEntrada[-1] == ")"):
                    nuevaEntrada += "*("
                else:
                    nuevaEntrada += "("
                
            elif es_paréntesis_cierre:
                if númeroActual.strip():
                    númeroFormateado = formatearNúmero(númeroActual.strip())
                    if númeroFormateado == "Error":
                        return
                    nuevaEntrada += númeroFormateado
                    númeroActual = ""
                
                if nuevaEntrada.count("(") > nuevaEntrada.count(")"):
                    nuevaEntrada += ")"
               
            elif not es_paréntesis_apertura and not es_paréntesis_cierre:
                nuevaEntrada += caracter
        else:
            númeroActual += caracter
        i += 1
    
    TieneComa = "," in númeroActual and númeroActual.rstrip("0").endswith(",")

    if TieneComa:
        nuevaEntrada += númeroActual
        
    elif númeroActual.strip():
        númeroFormateado = formatearNúmero(númeroActual.strip())
        if númeroFormateado == "Error":
            return
        nuevaEntrada += númeroFormateado
        
    

    # Mostrar en pantalla
    entrada_widget.delete(0, tk.END)
    entrada_widget.insert(0, nuevaEntrada)
    
if __name__ == "__main__":
    calculadora_principal = calculadora()
    calculadora_principal.mainloop()