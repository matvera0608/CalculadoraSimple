from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto, tkinter.font as fuenteDeLetra, tkinter.simpledialog as diálogo

#Colores
celeste_claro = "#BDE3FF"
rojo_claro = "#FFCBCB"
celeste_oscuro = "#003367"
blanco = "#FFFFFF"
negro = "#000000"
gris = "#808080"
rojo_oscuro = "#B10000"
amarillo_oscuro = "#BBB800"
verde_oscuro = "#009D00"
azul_oscuro = "#000AC0"
naranja_oscuro = "#CA7600"
violeta_oscuro = "#7F00CE"

# -*- coding: utf-8 -*-
#defino la función con valor de devolución o de retorno llamada calculadora()
#que va todos los botones necesarios para los cálculos necesarios
def pantallaCalculadora(ventanaPrincipal):
    global anchura, altura, PantallaParaEscribirNúmeros, PantallaParaResultadoEjercicio
    anchura = min(360, 550)
    altura = 100
    
    PantallaParaEscribirNúmeros = Entry(ventanaPrincipal, font=("Century", 25), bg=celeste_claro, fg=celeste_oscuro, bd=1, justify="right")
    PantallaParaEscribirNúmeros.config(state="normal")
    PantallaParaEscribirNúmeros.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="we")
    ventanaPrincipal.columnconfigure(0, weight=1)
    ventanaPrincipal.columnconfigure(1, weight=2)
    PantallaParaEscribirNúmeros.insert(0, "")
    PantallaParaEscribirNúmeros.focus_set()
    PantallaParaEscribirNúmeros.bind("<KeyRelease>", lambda event: formatearEntrada())
    
    PantallaParaResultadoEjercicio = Entry(ventanaPrincipal, font=("Century" , 20), bg=celeste_claro, fg=celeste_oscuro, bd=1, justify="right", state="readonly")
    PantallaParaResultadoEjercicio.grid(row=50, column=0, columnspan=15, padx=10, pady=550, sticky="we")

#esta función llamada Botón con el argumento puesto para obtener los datos de
#la función ventana principal contiene TODOS LOS BOTONES DE LA CALCULADORA
def Botón(ventanaPrincipal):
    
    altura = 25
    anchura = 25
    
    BotónCalcular = Button(ventanaPrincipal, text="Calcular", font=("Century", 10), bg=celeste_claro, fg=negro, bd=1, justify="right", command=Calcular)
    BotónCalcular.place(x=190, y=665, width=(100//2) + 10, height=(50//2))
    BotónCalcular.config(state="normal")
    
    BotónBorrar = Button(ventanaPrincipal, text="Borrar", font=("Century", 10), bg=rojo_claro, fg=negro, bd=1, justify="right", command=borrarÚltimo)
    BotónBorrar.place(x=260, y=665, width=(100//2) + 10, height=(50//2))
    BotónBorrar.config(state="normal")
    
    BotónBorrarTODO = Button(ventanaPrincipal, text="Borrar\ntodo", font=("Century", 10), bg=rojo_claro, fg=negro, bd=1, justify="center", command=borrarTODO)
    BotónBorrarTODO.place(x=330, y=660, width=(100//2) + 10, height=(50//2) + 5)
    BotónBorrarTODO.config(state="normal")
    
    BotónSuma = Button(ventanaPrincipal, text="+", font=("Century", 25), bg=rojo_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "+"))
    BotónSuma.place(x=50, y=100, width=anchura*2, height=altura*2)
    BotónSuma.config(state="normal")
    
    BotónResta = Button(ventanaPrincipal, text="-", font=("Century", 25), bg=amarillo_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "-"))
    BotónResta.place(x=100, y=100, width=anchura*2, height=altura*2)
    BotónResta.config(state="normal")
    
    BotónMultiplicación = Button(ventanaPrincipal, text="*", font=("Century", 25), bg=verde_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "*"))
    BotónMultiplicación.place(x=150, y=100, width=anchura*2, height=altura*2)
    BotónMultiplicación.config(state="normal")
    
    BotónDivisión = Button(ventanaPrincipal, text="÷", font=("Century", 25), bg=azul_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "÷"))
    BotónDivisión.place(x=200, y=100, width=anchura*2, height=altura*2)
    BotónDivisión.config(state="normal")
    
    BotónPotencia = Button(ventanaPrincipal, text="^", font=("Century", 25), bg=violeta_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "^"))
    BotónPotencia.place(x=250, y=100, width=anchura*2, height=altura*2)
    BotónPotencia.config(state="normal")
    
    BotónRaíz = Button(ventanaPrincipal, text="ⁿ√", font=("Century", 25), bg=naranja_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "ⁿ√"))
    BotónRaíz.place(x=300, y=100, width=anchura*2, height=altura*2)
    BotónRaíz.config(state="normal")
    
#Esta función muestra la interfaz de la calculadora principal para la ventana
def calculadora():
    global ventanaPrincipal
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Calculadora sencilla")
    ventanaPrincipal.geometry("400x700")
    ventanaPrincipal.maxsize(400, 700)
    ventanaPrincipal.minsize(400, 700)
    ventanaPrincipal.config(bg="white")
    ventanaPrincipal.resizable(10, 10)
    
    pantallaCalculadora(ventanaPrincipal)
    Botón(ventanaPrincipal)
    
    return ventanaPrincipal

#Crearé una función que formatea los números con . (punto) y , (coma)
#donde los puntos van en los millares y la coma en la milésima
def formatearNúmero():
    número = PantallaParaEscribirNúmeros.get()
    try:
        número = float(número.replace(",", "."))
        parteEntera = int(número)
        parteDecimal = abs(número - parteEntera)
        tieneDecimal = parteDecimal > 0
        
        expresiónEnteraFormateada = f"{parteEntera:,},".replace(",", ".")
        
        if tieneDecimal:
            expresiónDecimalFormateada = f"{parteDecimal:.10f}".split(".")[1].rstrip("0")
            resultado = f"{expresiónEnteraFormateada}, {expresiónDecimalFormateada}"
        else:
            resultado = expresiónEnteraFormateada
        
        PantallaParaEscribirNúmeros.delete(0, tk.END)
        PantallaParaEscribirNúmeros.insert(0, resultado)

    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")
        return "Error"

#Creé otra función para hacer el mismo formato deseado para el resultado del ejercicio
def formatearNúmeroResultado():
    número = PantallaParaResultadoEjercicio.get()
    try:
        número = float(número.replace(",", "."))
        parteEntera = int(número)
        parteDecimal = abs(número - parteEntera)
        tieneDecimal = parteDecimal > 0
        
        expresiónEnteraFormateada = f"{parteEntera},".replace(",", ".")
        
        if tieneDecimal:
            expresiónDecimalFormateada = f"{parteDecimal:.10f}".split(".")[1].rstrip("0")
            resultado = f"{expresiónEnteraFormateada}{expresiónDecimalFormateada}"
        else:
            resultado = expresiónEnteraFormateada
        
        PantallaParaResultadoEjercicio.delete(0, tk.END)
        PantallaParaResultadoEjercicio.insert(0, resultado)

    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")
        return "Error"

#Crearé una función que llame a las funciones aritméticas según los signos
#para el botón de Calcular
def Calcular():
    entrada = PantallaParaEscribirNúmeros.get()
    suma = "+" in entrada
    resta = "-" in entrada
    multiplicación = "*" in entrada
    división = ("/" in entrada) or ("÷" in entrada)
    potencia = "^" in entrada
    raiz = "ⁿ√" in entrada
    
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

#Esta sección tendrán funciones para los cálculos
def sumar():
    #las variables necesarias
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("+")
    signoCorrecto = "+" in entrada
    noTieneDosOperandos = len(parte) != 2
    
    
    if signoCorrecto:
        
        if noTieneDosOperandos:
            mensajeDeTexto.showerror("FORMATO NO VÁLIDO", f"Sólo están permitidos 2 números separados en +")
            return
        
        #creo un try-except para manejar mejor las excepciones o errores de validación
        try:
            númeroA = float(parte[0].strip())
            númeroB = float(parte[1].strip())
            resultado = int(númeroA + númeroB)
            mostrarResultado(resultado)
        except ValueError as errorDeValidación:
            mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")
    else:
        mensajeDeTexto.showinfo("FALTA DE SÍMBOLO", "ESCRIBIR EL SIGNO INDICADO DE SUMA ")

def restar():
    #las variables necesarias
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("-")
    signoCorrecto = "-" in entrada
    noTieneDosOperandos = len(parte) != 2
    
    
    if not signoCorrecto and noTieneDosOperandos:
        mensajeDeTexto.showerror("FORMATO NO VÁLIDO", f"Sólo están permitidos 2 números separados en +")
        return
    #Controlo con try-except para evitar cualquier fallo o excepción de signos 
    try:
        númeroA = convertirATipoFloat(parte[0].strip())
        númeroB = convertirATipoFloat(parte[1].strip())
        
        invalidación = númeroA is None or númeroB is None
        
        if invalidación:
            mensajeDeTexto.showerror("ERROR", "Hay un error inválido")
            return
        
        resultado = númeroA - númeroB
        
        mostrarResultado(resultado)
        
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def multiplicar():
     #las variables necesarias
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("*")
    signoCorrecto = "*" in entrada
    noTieneDosOperandos = len(parte) != 2
    
    
    if not signoCorrecto and noTieneDosOperandos:
        mensajeDeTexto.showerror("FORMATO NO VÁLIDO", f"Sólo están permitidos 2 números separados en +")
        return
    #Controlo con try-except para evitar cualquier fallo o excepción de signos 
    try:
        númeroA = convertirATipoFloat(parte[0].strip())
        númeroB = convertirATipoFloat(parte[1].strip())
        
        invalidación = númeroA is None or númeroB is None
        
        if invalidación:
            mensajeDeTexto.showerror("ERROR", "Hay un error inválido")
            return
        
        resultado = númeroA * númeroB
        
        mostrarResultado(resultado)
        
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def dividir():
     #las variables necesarias
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("÷")
    signoCorrecto = "÷" in entrada
    noTieneDosOperandos = len(parte) != 2
    
    
    if not signoCorrecto and noTieneDosOperandos:
        mensajeDeTexto.showerror("FORMATO NO VÁLIDO", f"Sólo están permitidos 2 números separados en +")
        return
    #Controlo con try-except para evitar cualquier fallo o excepción de signos 
    try:
        númeroA = convertirATipoFloat(parte[0].strip())
        númeroB = convertirATipoFloat(parte[1].strip())
        
        invalidación = númeroA is None or númeroB is None
        divisiónEntre0 = númeroB == 0
        
        if invalidación:
            mensajeDeTexto.showerror("ERROR", "Hay un error inválido")
            return
        
        if divisiónEntre0:
            PantallaParaResultadoEjercicio.insert(0, "NO SE DIVIDE POR CERO 😡")
            PantallaParaResultadoEjercicio.config(state="readonly")
        else:
            resultado = númeroA/númeroB
            mostrarResultado(resultado)
        
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def sacarNPotencia():
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("^")
    signoCorrecto = "^" in entrada
    noTieneDosOperandos = len(parte) != 2
    
    if signoCorrecto:
        
        #Acá compruebo que los datos permitan solamente 2 números nada más.
        if noTieneDosOperandos:
            mensajeDeTexto.showerror("FORMATO NO VÁLIDO", f"Sólo están permitidos 2 números separados en ^")
            return
        #el try es para controlar cualquier excepción de código
        try:
            númeroA = int(parte[0].strip())
            númeroB = int(parte[1].strip())
            resultado = int(númeroA ** númeroB)
            mostrarResultado(resultado)
        except ValueError as errorDeValidación:
            mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")
    else:
        mensajeDeTexto.showinfo("FALTA DE SÍMBOLO", "ESCRIBIR EL SIGNO INDICADO DE POTENCIA")
            
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
            númeroA = float(parte[1].strip())
            númeroB = float(parte[0].strip())
            if númeroB == 0 or númeroA == 0:
                mensajeDeTexto.showerror("ERROR", "El índice de la raíz no puede ser cero ni tampoco el radicando")
                return
            resultado = int(númeroA ** (1/númeroB))
            mostrarResultado(resultado)
        except ValueError as errorDeValidación:
            mensajeDeTexto.showinfo("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")
    else:
        mensajeDeTexto.showinfo("FALTA DE SÍMBOLO", "ESCRIBIR EL SIGNO INDICADO DE RAÍZ")

#En esta función sólo muestro el resultado según la operación matemática donde se llame
def mostrarResultado(res):
    PantallaParaResultadoEjercicio.config(state="normal")
    PantallaParaResultadoEjercicio.delete(0, tk.END)
    PantallaParaResultadoEjercicio.insert(tk.END, res)
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
    PantallaParaEscribirNúmeros.focus_set()


# -*- coding: utf-8 -*-
#defino la función con valor de devolución o de retorno llamada calculadora()
#que va todos los botones necesarios para los cálculos necesarios
def pantallaCalculadora(ventanaPrincipal):
    global anchura, altura, PantallaParaEscribirNúmeros, PantallaParaResultadoEjercicio
    anchura = min(360, 550)
    altura = 100
    
    PantallaParaEscribirNúmeros = Entry(ventanaPrincipal, font=("Century", 25), bg=celeste_claro, fg=celeste_oscuro, bd=1, justify="right")
    PantallaParaEscribirNúmeros.config(state="normal")
    PantallaParaEscribirNúmeros.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="we")
    ventanaPrincipal.columnconfigure(0, weight=1)
    ventanaPrincipal.columnconfigure(1, weight=2)
    PantallaParaEscribirNúmeros.insert(0, "")
    PantallaParaEscribirNúmeros.focus_set()
    
    PantallaParaResultadoEjercicio = Entry(ventanaPrincipal, font=("Century" , 20), bg=celeste_claro, fg=celeste_oscuro, bd=1, justify="right", state="readonly")
    PantallaParaResultadoEjercicio.grid(row=50, column=0, columnspan=15, padx=10, pady=550, sticky="we")
    

#esta función llamada Botón con el argumento puesto para obtener los datos de
#la función ventana principal contiene TODOS LOS BOTONES DE LA CALCULADORA
def Botón(ventanaPrincipal):
    
    altura = 25
    anchura = 25
    
    BotónCalcular = Button(ventanaPrincipal, text="Calcular", font=("Century", 10), bg=celeste_claro, fg=negro, bd=1, justify="right", command=Calcular)
    BotónCalcular.place(x=190, y=665, width=(100//2) + 10, height=(50//2))
    BotónCalcular.config(state="normal")
    
    BotónBorrar = Button(ventanaPrincipal, text="Borrar", font=("Century", 10), bg=rojo_claro, fg=negro, bd=1, justify="right", command=borrarÚltimo)
    BotónBorrar.place(x=260, y=665, width=(100//2) + 10, height=(50//2))
    BotónBorrar.config(state="normal")
    
    BotónBorrarTODO = Button(ventanaPrincipal, text="Borrar\ntodo", font=("Century", 10), bg=rojo_claro, fg=negro, bd=1, justify="center", command=borrarTODO)
    BotónBorrarTODO.place(x=330, y=660, width=(100//2) + 10, height=(50//2) + 5)
    BotónBorrarTODO.config(state="normal")
    
    BotónSuma = Button(ventanaPrincipal, text="+", font=("Century", 25), bg=rojo_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "+"))
    BotónSuma.place(x=50, y=100, width=anchura*2, height=altura*2)
    BotónSuma.config(state="normal")
    
    BotónResta = Button(ventanaPrincipal, text="-", font=("Century", 25), bg=amarillo_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "-"))
    BotónResta.place(x=100, y=100, width=anchura*2, height=altura*2)
    BotónResta.config(state="normal")
    
    BotónMultiplicación = Button(ventanaPrincipal, text="*", font=("Century", 25), bg=verde_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "*"))
    BotónMultiplicación.place(x=150, y=100, width=anchura*2, height=altura*2)
    BotónMultiplicación.config(state="normal")
    
    BotónDivisión = Button(ventanaPrincipal, text="÷", font=("Century", 25), bg=azul_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "÷"))
    BotónDivisión.place(x=200, y=100, width=anchura*2, height=altura*2)
    BotónDivisión.config(state="normal")
    
    BotónPotencia = Button(ventanaPrincipal, text="^", font=("Century", 25), bg=violeta_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "^"))
    BotónPotencia.place(x=250, y=100, width=anchura*2, height=altura*2)
    BotónPotencia.config(state="normal")
    
    BotónRaíz = Button(ventanaPrincipal, text="ⁿ√", font=("Century", 25), bg=naranja_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "ⁿ√"))
    BotónRaíz.place(x=300, y=100, width=anchura*2, height=altura*2)
    BotónRaíz.config(state="normal")
    
#Esta función muestra la interfaz de la calculadora principal para la ventana
def calculadora():
    global ventanaPrincipal
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Calculadora sencilla")
    ventanaPrincipal.geometry("400x700")
    ventanaPrincipal.maxsize(400, 700)
    ventanaPrincipal.minsize(400, 700)
    ventanaPrincipal.config(bg="white")
    ventanaPrincipal.resizable(10, 10)
    
    pantallaCalculadora(ventanaPrincipal)
    Botón(ventanaPrincipal)
    
    return ventanaPrincipal

#Defino una variable para disparar la interfaz gráfica de calculadora

calculadora_principal = calculadora()

calculadora_principal.mainloop()