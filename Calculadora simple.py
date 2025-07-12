from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto, tkinter.font as fuenteDeLetra, tkinter.simpledialog as diálogo

"""
EN ESTA SECCIÓN DEFINO LAS FUNCIONES DE PANTALLA 
Y BOTONES DE LA CALCULADORA PERSONALIZADA.
"""

# Diccionario de colores
color = {
"celeste_claro": "#B4E0FF",
"rojo_claro": "#FFCBCB",
"celeste_oscuro": "#003E67",
"beige": "#A8A862",
"blanco": "#FFFFFF",
"negro": "#000000",
"gris": "#AAAAAA",
"rojo_oscuro": "#B10000",
"rojo_resaltado": "#B66666",
"amarillo_oscuro": "#BBB800",
"amarillo_resaltado": "#BEBD61",
"verde_oscuro": "#009D00",
"verde_resaltado":"#67B167",
"azul_oscuro": "#000AC0",
"azul_claro": "#000AC0",
"naranja_oscuro": "#CA7600",
"naranja_resaltado": "#C79653",
"violeta_oscuro": "#7F00CE",
"violeta_claro": "#A36BC5"
}

# -*- coding: utf-8 -*-
#defino la función con valor de devolución o de retorno llamada calculadora()
#que va todos los botones necesarios para los cálculos necesarios
def pantallaCalculadora(ventanaPrincipal):
    global PantallaParaEscribirNúmeros, PantallaParaResultadoEjercicio, PantallaRestoDivisión

    for i in range(8):
        ventanaPrincipal.columnconfigure(i, weight=0)

    PantallaParaEscribirNúmeros = Entry(ventanaPrincipal, font=("Century", 30), bg=color["celeste_claro"], fg=color["celeste_oscuro"], bd=4, justify="right")
    PantallaParaEscribirNúmeros.config(state="normal")
    PantallaParaEscribirNúmeros.grid(row=0, column=0, columnspan=15, padx=10, pady=10, sticky="we")
    ventanaPrincipal.columnconfigure(0, weight=1)
    ventanaPrincipal.columnconfigure(1, weight=2)
    PantallaParaEscribirNúmeros.insert(0, "")
    PantallaParaEscribirNúmeros.focus_set()
    PantallaParaEscribirNúmeros.bind("<KeyRelease>", lambda event: formatearEntrada())
    PantallaParaEscribirNúmeros.bind("<Return>", lambda e: Calcular())
    PantallaParaEscribirNúmeros.bind("<BackSpace>", lambda e: borrarÚltimo())
    PantallaParaEscribirNúmeros.bind("<Control-BackSpace>", lambda e: borrarTODO())

    PantallaParaResultadoEjercicio = Entry(ventanaPrincipal, font=("Century" , 30), bg=color["gris"], fg=color["negro"], bd=4, justify="right", state="readonly")
    PantallaParaResultadoEjercicio.grid(row=50, column=0, columnspan=15, padx=10, pady=50, sticky="we")
    
    # Suponiendo que las otras dos Entry usan columnspan=15,
    # podemos usar columnspan=8 (aproximadamente la mitad de 15) para esta Entry.
    PantallaRestoDivisión = Entry(ventanaPrincipal, font=("Century",15), bg=color["gris"], fg=color["negro"], bd=4, justify="right", state="readonly")
    PantallaRestoDivisión.grid(row=10, column=2, columnspan=2, padx=5, sticky="nsew")
    módulo = Label(ventanaPrincipal, text="Resto de la división:", font=("Century", 10), bg=color["blanco"], fg=color["negro"])
    módulo.grid(row=10, column=0, columnspan=2,padx=5, sticky="w")
    

#esta función llamada Botón con el argumento puesto para obtener los datos de
#la función ventana principal contiene TODOS LOS BOTONES DE LA CALCULADORA
def Botón(ventanaPrincipal):
    
    #Acá creo una lista con todos los botones correspondientes
    #de la calculadora
    botones = [
    ("00", 1, 0, 1, 2), ("000", 1, 2, 1, 2),
    ("%", 2, 0, 1, 1), ("ⁿ√", 2, 1, 1, 1), ("^", 2, 2, 1, 1), ("÷", 2, 3, 1, 1),
    ("7", 3, 0, 1, 1), ("8", 3, 1, 1, 1), ("9", 3, 2, 1, 1), ("*", 3, 3, 1, 1),
    ("4", 4, 0, 1, 1), ("5", 4, 1, 1, 1), ("6", 4, 2, 1, 1), ("-", 4, 3, 1, 1),
    ("1", 5, 0, 1, 1), ("2", 5, 1, 1, 1), ("3", 5, 2, 1, 1), ("+", 5, 3, 2, 1),
    ("0", 6, 0, 1, 2), (",", 6, 2, 1, 1)
    ]
    
    # Voy a crear un for para armar una matriz de botones
    # de la calculadora personalizada, aplicando colores según el diccionario.
    for texto, fila, columna, tramoFila, tramoColumna in botones:
        # Asigno colores diferentes para operadores y para números.
        if texto in ("+"):
            btn_fondo = color["rojo_oscuro"]
            btn_letra = color["blanco"]
        elif texto in ("-"):
            btn_fondo = color["amarillo_oscuro"]
            btn_letra = color["blanco"]
        elif texto in ("*"):
            btn_fondo = color["azul_oscuro"]
            btn_letra = color["blanco"]
        elif texto in ("÷"):
            btn_fondo = color["verde_oscuro"]
            btn_letra = color["blanco"]  
        elif texto in ("^"):
            btn_fondo = color["naranja_oscuro"]
            btn_letra = color["blanco"]
        elif texto in ("ⁿ√"):
            btn_fondo = color["violeta_oscuro"]
            btn_letra = color["blanco"]
        elif texto in ("%"):
            btn_fondo = color["negro"]
            btn_letra = color["blanco"]
        elif texto in ("00", "000", "0", ",", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            # Para los números, uso un color claro y un texto oscuro.
            btn_fondo = color["beige"]
            btn_letra = color["negro"]
        else:
            btn_fondo = color["celeste_claro"]
            btn_letra = color["celeste_oscuro"]
            
        # La variable btn corresponde al botón
        btn = Button(ventanaPrincipal, text=texto, width=1, height=1, font=("Century", int(30/2), "bold"),
        bg=btn_fondo, fg=btn_letra, command=lambda value=texto: [PantallaParaEscribirNúmeros.insert(END, value), formatearEntrada()])
        btn.grid(row=fila, column=columna, rowspan=tramoFila, columnspan=tramoColumna, sticky="nsew", padx=1, pady=1)

    BotónCalcular = Button(ventanaPrincipal, text="Calcular", font=("Century", 10), bg=color["celeste_claro"], fg=color["negro"], bd=1, justify="right", command=Calcular)
    BotónCalcular.grid(row=7, column=2, padx=1, pady=1, sticky="nsew")
    

    BotónBorrar = Button(ventanaPrincipal, text="Borrar", font=("Century", 10), bg=color["rojo_claro"], fg=color["negro"], bd=1, justify="right", command=borrarÚltimo)
    BotónBorrar.grid(row=7, column=3, padx=1, pady=1, sticky="nsew")

    BotónBorrarTODO = Button(ventanaPrincipal, text="Borrar\ntodo", font=("Century", 10), bg=color["rojo_claro"], fg=color["negro"], bd=1, justify="center", command=borrarTODO)
    BotónBorrarTODO.grid(row=8, column=3, padx=1, pady=0, sticky="nsew")

    #Este for ayuda a ajustar todas las filas y columnas lo más proporcionalmente
    #posible para que la calculadora se vea bien
    for i in range(9):
        ventanaPrincipal.grid_rowconfigure(i, weight=1, minsize=60)
    for j in range(4):
        ventanaPrincipal.grid_columnconfigure(j, weight=1, minsize=80)
        
    ventanaPrincipal.grid_columnconfigure(3, minsize=100)
    BotónBorrarTODO.config(wraplength=60)

#Esta función muestra la interfaz de la calculadora principal para la ventana
def calculadora():
    global ventanaPrincipal
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Calculadora sencilla")
    ventanaPrincipal.geometry("350x800")
    ventanaPrincipal.config(bg="white")

    pantallaCalculadora(ventanaPrincipal)
    Botón(ventanaPrincipal)

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
            parteEntera = f"{int(parteEntera):,}".replace(",", ".")
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
    signos = ["+", "-", "*", "/", "%", "^", "ⁿ√", "(", ")"]
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
            if númeroActual.strip():
                númeroFormateado = formatearNúmero(númeroActual.strip())
                if númeroFormateado == "Error":
                    return
                nuevaEntrada += númeroFormateado
                númeroActual = ""
            
            bloqueoParéntesisDobles = caracter == "(" and nuevaEntrada and nuevaEntrada[-1] == "("
            
            if bloqueoParéntesisDobles:
                i += 1
                continue
            multiplicaciónImplícita = nuevaEntrada and (nuevaEntrada[-1].isdigit or nuevaEntrada[-1] == ")" or not nuevaEntrada in signos) and caracter  == "("
                
            if multiplicaciónImplícita:
                nuevaEntrada += "*"
                
                nuevaEntrada += caracter
                
            elif not nuevaEntrada or nuevaEntrada[-1] not in signos or nuevaEntrada[-1] in "()":
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
    
  
# def insertarMil():
#     PantallaParaEscribirNúmeros.insert(tk.END, "000")
#     formatearEntrada()  # Se ejecuta el formateo completo

#Crearé una función que llame a las funciones aritméticas según los signos
#para el botón de Calcular
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
                PantallaParaResultadoEjercicio.config(state="normal")
                PantallaParaResultadoEjercicio.delete(0, tk.END)
                PantallaParaResultadoEjercicio.insert(0, "NO SE DIVIDE POR CERO 😡", )
                PantallaParaResultadoEjercicio.config(state="readonly")
                return
            resultado //= n
            
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

calculadora_principal = calculadora()

calculadora_principal.mainloop()