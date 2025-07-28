import os
from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto, tkinter.font as fuenteDeLetra, tkinter.simpledialog as diálogo
from calc_divisas import calculadora_de_divisas


"""
EN ESTA SECCIÓN DEFINO LAS FUNCIONES DE PANTALLA 
Y BOTONES DE LA CALCULADORA PERSONALIZADA.
"""

# Diccionario de colores
color = {
    "celeste_claro": "#B4E0FF",
    "rojo_claro": "#FFCBCB",
    "celeste_oscuro": "#003E67",
    "beige": "#A5A55F",
    "beige_resaltado": "#B7B78A",
    "blanco": "#FFFFFF",
    "negro": "#000000",
    "negro_resaltado": "#242424",
    "gris": "#AAAAAA",
    "rojo_anaranjado": "#FF3C00",
    "rojo": "#FF0000",
    "rojo_resaltado": "#FF5A5A",
    "amarillo": "#FFFB00",
    "amarillo_resaltado": "#FFFC4C",
    "verde": "#0DFF00",
    "verde_resaltado":"#8AFF7B",
    "azul": "#000DFF",
    "azul_resaltado": "#6C73FF",
    "naranja": "#FF7300",
    "naranja_resaltado": "#FFC16A",
    "violeta": "#9D00FF",
    "violeta_resaltado": "#CD7BFF"
}

directorio_imágen = os.path.dirname(__file__)
ícono = os.path.join(directorio_imágen, "imagenes","ícono.ico")

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
    TamañoFijo.grid(row=0, column=0, columnspan=8, padx=4, pady=(8, 4), sticky="nsew")
    TamañoFijo.grid_propagate(False)  # Impide que el tamaño del Frame se ajuste al contenido
    TamañoFijo.columnconfigure(0, weight=1)
    TamañoFijo.rowconfigure(0, weight=1)
    TamañoFijo.rowconfigure(1, weight=1)

    PantallaParaEscribirNúmeros = Entry(TamañoFijo, font=("Century", 30), bg=color["celeste_claro"], fg=color["celeste_oscuro"], bd=4, justify="right")
    PantallaParaEscribirNúmeros.grid(row=0, column=0, sticky="nsew", padx=10, pady=(4, 2))
    PantallaParaEscribirNúmeros.insert(0, "")
    PantallaParaEscribirNúmeros.focus_set()
    PantallaParaEscribirNúmeros.bind("<KeyRelease>", lambda e: formatearEntrada())
    PantallaParaEscribirNúmeros.bind("<Return>", lambda e: Calcular())
    PantallaParaEscribirNúmeros.bind("<Control-BackSpace>", lambda e: borrarTODO())
    PantallaParaEscribirNúmeros.bind("<Alt-0>", lambda e: escribirCeros("00"))
    PantallaParaEscribirNúmeros.bind("<Control-0>", lambda e: escribirCeros("000"))


     # Resultado del ejercicio
    PantallaParaResultadoEjercicio = Entry(TamañoFijo, font=("Century", 30), bg=color["rojo_claro"], fg=color["negro"], bd=4, justify="right", state="readonly")
    PantallaParaResultadoEjercicio.grid(row=1, column=0, sticky="nsew", padx=10, pady=(2, 6))
    PantallaParaResultadoEjercicio.bind("<Control-C>", lambda e: mostrarResultado())
    PantallaParaResultadoEjercicio.propagate(False)

    # Proporcionalidad del módulo
    ventanaPrincipal.columnconfigure(0, weight=1)
    ventanaPrincipal.columnconfigure(1, weight=1)
    ventanaPrincipal.columnconfigure(2, weight=1)
    ventanaPrincipal.columnconfigure(3, weight=1)
    ventanaPrincipal.columnconfigure(4, weight=1)
    ventanaPrincipal.columnconfigure(5, weight=1)


    módulo = Label(ventanaPrincipal,text="Resto de la división:",font=("Century", 10),bg=ventanaPrincipal["bg"],fg=color["negro"])
    módulo.grid(row=2, column=0, columnspan=3, padx=6, pady = (0, 2), sticky="w")

    PantallaRestoDivisión = Entry(ventanaPrincipal, font=("Century", 15), bg=color["gris"], fg=color["negro"], bd=4, justify="right", state="readonly")
    PantallaRestoDivisión.grid(row=2, column=3, columnspan=5, padx=6, pady=(0, 2), sticky="nsew")


#esta función llamada Botón con el argumento puesto para obtener los datos de
#la función ventana principal contiene TODOS LOS BOTONES DE LA CALCULADORA
def Botón(ventanaPrincipal):
    botones = [
        ("00", 0, 0, 1, 2), ("000", 0, 2, 1, 2),
        ("%", 1, 0, 1, 1), ("ⁿ√", 1, 1, 1, 1), ("^", 1, 2, 1, 1), ("÷", 1, 3, 1, 1),
        ("7", 2, 0, 1, 1), ("8", 2, 1, 1, 1), ("9", 2, 2, 1, 1), ("×", 2, 3, 1, 1),
        ("4", 3, 0, 1, 1), ("5", 3, 1, 1, 1), ("6", 3, 2, 1, 1), ("-", 3, 3, 1, 1),
        ("1", 4, 0, 1, 1), ("2", 4, 1, 1, 1), ("3", 4, 2, 1, 1), ("+", 4, 3, 2, 1),
        ("0", 5, 0, 1, 1), (",", 5, 1, 1, 1), ("=", 5, 2, 1, 1)
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
        elif texto == "^":
            return color["naranja"], color["naranja_resaltado"], color["blanco"]
        elif texto == "ⁿ√":
            return color["violeta"], color["violeta_resaltado"], color["blanco"]
        elif texto == "%":
            return color["negro"], color["negro_resaltado"], color["blanco"]
        elif texto in ("00", "000", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "="):
            return color["beige"], color["beige_resaltado"], color["negro"]
        else:
            return color["celeste_claro"], color["celeste_oscuro"], color["blanco"]

    for texto, fila, columna, rowspan, columnspan in botones:
        btn_fondo, btn_fondoResaltado, btn_letra = obtener_color_botón(texto)
        boton = tk.Button(ventanaPrincipal, text=texto, font=("Century", 20, "bold"), bg=btn_fondo, fg=btn_letra, activebackground=btn_fondoResaltado, activeforeground=btn_letra,
                          width=4, height=2, command=lambda value=texto: [PantallaParaEscribirNúmeros.insert(END, value), formatearEntrada()], relief="flat", highlightthickness=0,
                          bd=0)
        boton.grid(row=fila + 3, column=columna + 1, rowspan=rowspan, columnspan=columnspan, padx=2, pady=6, sticky="nsew")
        
        resaltar, restaurar = clickearBotón(boton, btn_fondoResaltado, btn_fondo, btn_letra)
        boton.bind("<ButtonPress-1>", resaltar)
        boton.bind("<ButtonRelease-1>", restaurar)

        
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
    ventanaPrincipal.geometry("450x900")
    ventanaPrincipal.config(bg="white")
    ventanaPrincipal.iconbitmap(ícono)
    ventanaPrincipal.columnconfigure(0, weight=1)

    pantallaCalculadora(ventanaPrincipal)
    Botón(ventanaPrincipal)
    
    ventanaPrincipal.bind("<Alt-l>", abrir__calculadora__de__divisas)
    
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

#Crearé una función que formatea los números con . (punto) y , (coma)
#donde los puntos van en los millares y la coma en la milésima
def formatearNúmero(númeroComoTexto):
    #Controlo que no me permita cualquier signo que no sea punto
    try:
        #Voy a crear una variable llamada NúmeroLimpio para
        #formatear esctrictamente el número a escribir
        númeroLimpio = númeroComoTexto.replace(".", "").replace(",", ".")
        valor = float(númeroLimpio)
        #Acá formatea si y solo si es entero
        if valor.is_integer():
            return f"{int(valor):,}".replace(",", ".")
        else:
            parteEntera, parteDecimal = str(valor).split(".")
            parteEntera = f"{int(parteEntera):,}".replace(",", ".")
            return f"{parteEntera},{parteDecimal}"
    except ValueError:
        return "Error"

#Creé otra función para hacer el mismo formato deseado para el resultado del ejercicio
# Creé otra función para hacer el mismo formato deseado para el resultado del ejercicio
def formatearNúmeroResultado(valor):
    try:
        valor = float(valor)
        if valor.is_integer():
            return f"{int(valor):,}".replace(",", ".")
        else:
            parteEntera, parteDecimal = str(valor).split(".")
            parteEntera, parteDecimal = f"{valor:.10f}".rstrip("0").rstrip(".").split(".")
            return f"{parteEntera},{parteDecimal}"
    except:
        return str(valor)

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
def formatearEntrada(*args):
    entrada = PantallaParaEscribirNúmeros.get()
    if not entrada or entrada[-1] == ",":
        return
    
    entradaProcesada = entrada.replace("÷", "/").replace("×", "*")
    signos = ["+", "-", "*", "/", "%", "^", "ⁿ√"]
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
        if caracter in signos:
            es_paréntesis_apertura = caracter == "(" #Así quedó, me costó un montón identar. Existe en vscode una manera de identar sin tener que ser manualmente?
            es_paréntesis_cierre = caracter == ")"
            if es_paréntesis_apertura:
                if númeroActual.strip():
                    númeroFormateado = formatearNúmero(númeroActual.strip())
                    if númeroFormateado == "Error":
                        return
                    nuevaEntrada += númeroFormateado
                    númeroActual = ""
                if nuevaEntrada: #Acá puse dos lógicas a la vez para no tener poner tantos if, porque quedaría demasiado engorroso.
                    último_número = nuevaEntrada[-1]
                
                    if último_número.isdigit():
                        nuevaEntrada += "*("
                
                    elif último_número == "(" and len(nuevaEntrada) > 1 and nuevaEntrada[-2].isdigit():
                        nuevaEntrada += "*("
                
                    elif último_número != "(":
                        nuevaEntrada += "("
                    else:
                        i += 1
                        continue
                else:
                    nuevaEntrada += "("
            ##Este es otro bloque para el paréntesis de cierre. No sé si está bien así bien identado?.
            ##Estoy enfrentando un problema, cuando escribo un número con unidad de mil me limpió el punto.
            elif es_paréntesis_cierre:
                if not nuevaEntrada or nuevaEntrada[-1] in signos:
                    i += 1
                    continue
                
                if nuevaEntrada.count("(") > nuevaEntrada.count(")"):
                    nuevaEntrada += ")"
                else:
                    i += 1
                    continue
            else:
                if númeroActual.strip():
                    númeroFormateado = formatearNúmero(númeroActual.strip())
                    if númeroFormateado == "Error":
                        return
                    nuevaEntrada += númeroFormateado
                    númeroActual = ""
                nuevaEntrada += caracter
        else:
            númeroActual += caracter
        i += 1

    # Añadir el último número si quedó algo
    if númeroActual.strip():
        númeroFormateado = formatearNúmero(númeroActual.strip())
        if númeroFormateado == "Error":
            return
        nuevaEntrada += númeroFormateado

    # Mostrar en pantalla
    PantallaParaEscribirNúmeros.delete(0, tk.END)
    PantallaParaEscribirNúmeros.insert(0, nuevaEntrada)
    
    return nuevaEntrada.strip().replace(",", ".")
    
# --- EVENTOS PARA USAR TECLADO ---

#Crearé una función que llame a las funciones aritméticas según los signos para el botón de Calcular
def Calcular():
    entrada = PantallaParaEscribirNúmeros.get()
    #Esta función calcula la expresión completa como una operación combinada
    def calcularExpresiónCompleta():
        try:
            expresión = entrada.replace(".", "")
            expresión = expresión.replace(",", ".")  # convertir coma a punto decimal
            expresión = expresión.replace("×", "*").replace("÷", "/")
            expresión = expresión.replace("%", "/100")  # manejar porcentaje
            resultado = eval(expresión)
            mostrarResultado(resultado)
        except Exception:
            mensajeDeTexto.showerror("ERROR", "La expresión es inválida")
            return
    
    operadores = "+-*/÷×"
    
    cantidad_de_signos = sum(entrada.count(op) for op in operadores)
    
    siHaySignos_o_Paréntesis = cantidad_de_signos > 1 or ("(" in entrada or ")" in entrada)
    
    if siHaySignos_o_Paréntesis:
        calcularExpresiónCompleta()
        return
    
    suma = "+" in entrada
    resta = "-" in entrada
    multiplicación = ("×" in entrada) or ("*" in entrada)
    división = ("/" in entrada) or ("÷" in entrada)
    potencia = "^" in entrada
    raiz = "ⁿ√" in entrada
    porcentaje = "%" in entrada
    
    #Esta condición es para especificar que operación debe realizar sin depender de llamar funciones matemáticas de forma particular
    if suma:
        sumar()
    elif resta:
        restar()
    elif multiplicación:
        multiplicar()
    elif división:
        dividir()
    elif potencia and not raiz:
        sacarNPotencia()
    elif raiz:
        sacarNRaíz()
    elif porcentaje:
        sacarPorcentaje()
    else:
        mensajeDeTexto.showinfo("ADVERTENCIA", "No se ha detectado ninguna operación")
    
#Esta sección tendrán funciones para los cálculos
def sumar():
    #las variables necesarias
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("+")
        #creo un try-except para manejar mejor las excepciones o errores de validación
    try:
        #este resultado ya hace suma dinámica con n cantidad de números
        partes = [float(p.strip().replace(".", "").replace(",", ".")) 
                        for p in parte if p.strip() != ""]
       
        #Creo una condición para que me obligue a poner mínimo 2 números para hacer la operación.
        falta_de_operandos = len(partes) < 2
        if falta_de_operandos:
            mensajeDeTexto.showerror("Error", "Faltan operandos para sumar.")
            return
        resultado = sum(partes)
        mostrarResultado(resultado)
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def restar():
    #las variables necesarias
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("-")
    #Controlo con try-except para evitar cualquier fallo o excepción de signos 
    try:
        partes = [float(p.strip().replace(",", ".")) for p in parte if p.strip() != ""]
        falta_de_operandos = len(partes) < 2
        if falta_de_operandos:
            mensajeDeTexto.showerror("Error", "Faltan operandos para restar.")
            return
        resultado = partes[0]
        #Acá itero para ir restando los números hasta llegar a negativo
        for n in partes[1:]:
            resultado -= n
        mostrarResultado(resultado)
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def multiplicar():
    #las variables necesarias
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("*")
    
    #Controlo con try-except para evitar cualquier fallo o excepción de signos 
    try:
        #Acá hago la multiplicación de cantidad enésima de números, es decir, más de 2 en adelante.
        números = []
        
        # Este bucle recorre cada parte separada por el operador '*'.
        # Si la parte contiene un porcentaje ('%'), lo convierte al valor decimal correspondiente.
        # Por ejemplo, para calcular 60 * 80%, convierte '80%' en 0.8 y realiza la multiplicación: 60 * 0.8 = 48.
        for p in parte:
            if p.strip() == "":
                continue
            if "%" in p:
            # Elimina el símbolo '%' y convierte el número a decimal dividiéndolo por 100
                p = p.replace("%", "")
                n = float(p.strip().replace(".", "").replace(",", "."))/100
            else:
                n = float(p.strip().replace(".", "").replace(",", "."))
            números.append(n)
        
        falta_de_operandos = len(números) < 2
        
        if falta_de_operandos:
            mensajeDeTexto.showerror("Error", "Faltan operandos para multiplicar.")
            return
            
        resultado = 1
        #Acá itero para ir restando los números hasta llegar a negativo
        for n in números:
            resultado *= n
        mostrarResultado(resultado)
        
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def dividir():
     #las variables necesarias
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.replace("÷", "/").split("/")
    #Controlo con try-except para evitar cualquier fallo o excepción de signos 
    try:
        #Acá hago la división de cantidad enésima de números, es decir, más de 2 en adelante.
        números = [float(p.strip().replace(".", "").replace(",", ".")) for p in parte if p.strip() != ""]
        
        falta_de_operandos = len(números) < 2
        
        if falta_de_operandos:
            mensajeDeTexto.showerror("Error", "Faltan operandos para multiplicar.")
            return
        
        resultado = números[0]
        #Acá itero para ir restando los números hasta llegar a negativo
        for n in números[1:]:
            divisiónEntre0 = n == 0
            if divisiónEntre0:
                PantallaParaResultadoEjercicio.config(state="normal", font=("Century", 10), fg=color["rojo_anaranjado"])
                PantallaParaResultadoEjercicio.delete(0, tk.END)
                PantallaParaResultadoEjercicio.insert(0, "NO SE DIVIDE POR CERO 😡")
                PantallaParaResultadoEjercicio.config(state="readonly")
                return
            resultado //= n
            PantallaParaResultadoEjercicio.config(state="normal", font=("Century", 30))
            
        mostrarResultado(resultado)
        
        son_dos_o_más_enteros = len(números) >= 2 and all(n.is_integer() for n in números)
        # Mostrar el módulo (resto) de la división cuando sea posible y son 2 números enteros
        if son_dos_o_más_enteros:
            resultado_módulo = int(números[0]) % int(números[1])
            PantallaRestoDivisión.config(state="normal")
            PantallaRestoDivisión.delete(0, tk.END)
            PantallaRestoDivisión.insert(0, str(resultado_módulo))
            PantallaRestoDivisión.config(state="readonly")   
        else:
            PantallaRestoDivisión.config(state="normal")
            PantallaRestoDivisión.delete(0, tk.END)
            PantallaRestoDivisión.insert(0, "-")
            PantallaRestoDivisión.config(state="readonly")   
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def sacarNPotencia():
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("^")
    
    #el try es para controlar cualquier excepción de código
    try:
        números = [float(p.strip().replace(",", ".")) for p in parte if p.strip() != ""]
        
        NotieneDosOperandos = len(números) < 2
        
        if NotieneDosOperandos:
            mensajeDeTexto.showerror("Error", "Faltan operandos para calcular potencia.")
            return
        #Acá itero para calcular potencias múltiples siempre de derecha
        #a izquierda
        resultado = números[-1]
        for base in reversed(números[:-1]):
            resultado = base ** resultado
            
        mostrarResultado(resultado)
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")
            
def sacarNRaíz():
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("ⁿ√")
    signoCorrecto = "ⁿ√" in entrada
    noTieneDosOperandos = len(parte) != 2

    if signoCorrecto:

        #Acá compruebo que los datos permitan solamente 2 números nada más.
        if noTieneDosOperandos:
            mensajeDeTexto.showerror("FORMATO NO VÁLIDO", f"Sólo están permitidos 2 números separados en ⁿ√")
            return

        try:
            númeroA = float(parte[1].strip().replace(".", "").replace(",", "."))
            númeroB = float(parte[0].strip().replace(".", "").replace(",", "."))
            if númeroB == 0 or númeroA == 0:
                mensajeDeTexto.showerror("ERROR", "El índice de la raíz no puede ser cero ni tampoco el radicando")
                return
            resultado = (númeroA ** (1/númeroB))
            mostrarResultado(resultado)
        except ValueError as errorDeValidación:
            mensajeDeTexto.showinfo("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")
    else:
        mensajeDeTexto.showinfo("FALTA DE SÍMBOLO", "ESCRIBIR EL SIGNO INDICADO DE RAÍZ")

#Saco el porcentaje de cada número puesto
def sacarPorcentaje():
    entrada = PantallaParaEscribirNúmeros.get()
    
    tienePorcentaje = "%" not in entrada
    
    #Me acostumbro a poner try-except para refozar cualquier control de datos
    try:
        if tienePorcentaje:
            mensajeDeTexto.showinfo("FALTA DE SÍMBOLO", "ESCRIBIR EL SIGNO INDICADO DE PORCENTAJE AL ESPECIFICAR")
            return
        else:
            parte = entrada.replace("%", "").strip()
            número = float(parte)
            resultado = número/100
            mostrarResultado(resultado)
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"Algo no está bien: {errorDeValidación}")
    
#En esta función sólo muestro el resultado según la operación matemática donde se llame
def mostrarResultado(res):
    resultadoFormateado = formatearNúmeroResultado(res)
    PantallaParaResultadoEjercicio.config(state="normal")
    PantallaParaResultadoEjercicio.delete(0, tk.END)
    PantallaParaResultadoEjercicio.insert(tk.END, resultadoFormateado)
    PantallaParaResultadoEjercicio.config(state="readonly")

#Esta función borra de a 1 número. No borra completamente al presionarlo
#el botón Borrar
def borrarÚltimo():
    PantallaParaEscribirNúmeros.config(state="normal")
    textoActual = PantallaParaEscribirNúmeros.get()
    nuevoTexto = textoActual[:-1]
    PantallaParaEscribirNúmeros.delete(0, tk.END)
    PantallaParaEscribirNúmeros.insert(0, nuevoTexto)
    
#Esta función borra de a 1 número. No borra completamente al presionarlo
#el botón Borrar
def borrarTODO():
    PantallaParaEscribirNúmeros.config(state="normal")
    PantallaParaEscribirNúmeros.delete(0, tk.END)
    
    PantallaParaResultadoEjercicio.config(state="normal")
    PantallaParaResultadoEjercicio.delete(0, tk.END)
    PantallaParaResultadoEjercicio.config(state="readonly")
    PantallaRestoDivisión.config(state="normal")
    PantallaRestoDivisión.delete(0, tk.END)
    PantallaRestoDivisión.config(state="readonly")
    PantallaParaEscribirNúmeros.focus_set()

#Este espacio es para eventos como escribir ceros, resaltar botones, etc.
#Esta función escribe ceros en la pantalla de números, formateando la entrada
def escribirCeros(núm):
    PantallaParaEscribirNúmeros.insert(tk.END, núm)
    formatearEntrada()

# Esta función resalta el botón al hacer clic y lo restaura al soltarlo usando bind para que se resalte y restaure el color del botón a nivel interno y visual.
# En comparación con el anterior, 
def clickearBotón(btn, colorResaltado, colorOrginal, letraOriginal):
    def resaltar(event):
        btn.config(bg=colorResaltado, fg=letraOriginal)
    def restaurar(event):
        btn.config(bg=colorOrginal, fg=letraOriginal)
    return resaltar, restaurar

def abrir__calculadora__de__divisas(event=None):
    calculadora_de_divisas()

calculadora_principal = calculadora()
calculadora_principal.mainloop()
