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

#Crearé una función que llame a las funciones aritméticas según los signos
#para el botón de Calcular
def Calcular():
    entrada = PantallaParaEscribirNúmeros.get()
    suma = "+" in entrada
    resta = "-" in entrada
    multiplicación = "*" in entrada
    división = ("/" in entrada) or ("÷" in entrada)
    
    #Esta condición es para especificar que operación debe realizar sin depender de llamar funciones matemáticas de forma particular
    if suma:
        sumar()
    elif resta:
        restar()
    elif multiplicación:
        multiplicar()
    elif división:
        dividir()

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
    
    if signoCorrecto:
        
        if noTieneDosOperandos:
            mensajeDeTexto.showerror("FORMATO NO VÁLIDO", f"Sólo están permitidos 2 números separados en -")
            return
        
        #creo un try-except para manejar mejor las excepciones o errores de validación
        try:
            númeroA = float(parte[0].strip())
            númeroB = float(parte[1].strip())
            resultado = int(númeroA - númeroB)
            mostrarResultado(resultado)
        except ValueError as errorDeValidación:
            mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")
    else:
        mensajeDeTexto.showinfo("FALTA DE SÍMBOLO", "ESCRIBIR EL SIGNO INDICADO DE RESTA ")

def multiplicar():
     #las variables necesarias
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.split("*")
    signoCorrecto = "*" in entrada
    noTieneDosOperandos = len(parte) != 2
    
    if signoCorrecto:
        
        if noTieneDosOperandos:
            mensajeDeTexto.showerror("FORMATO NO VÁLIDO", f"Sólo están permitidos 2 números separados en *")
            return
        
        #creo un try-except para manejar mejor las excepciones o errores de validación
        try:
            númeroA = float(parte[0].strip())
            númeroB = float(parte[1].strip())
            resultado = int(númeroA * númeroB)
            mostrarResultado(resultado)
        except ValueError as errorDeValidación:
            mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")
    else:
        mensajeDeTexto.showinfo("FALTA DE SÍMBOLO", "ESCRIBIR EL SIGNO INDICADO DE MULTIPLICACIÓN")

def dividir():
     #las variables necesarias
    entrada = PantallaParaEscribirNúmeros.get()
    parte = entrada.replace("÷", "/").split("/")
    signoCorrecto = ("/" in entrada) or ("÷" in entrada)
    noTieneDosOperandos = len(parte) != 2
    
    if signoCorrecto:
        
        if noTieneDosOperandos:
            mensajeDeTexto.showerror("FORMATO NO VÁLIDO", f"Sólo están permitidos 2 números separados en / o ÷")
            return
        
        #creo un try-except para manejar mejor las excepciones o errores de validación
        try:
            númeroA = float(parte[0].strip())
            númeroB = float(parte[1].strip())
            resultado = int(númeroA / númeroB)
            mostrarResultado(resultado)
        except ValueError as errorDeValidación:
            mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")
    else:
        mensajeDeTexto.showinfo("FALTA DE SÍMBOLO", "ESCRIBIR EL SIGNO INDICADO DE DIVISIÓN")

def sacarNPotencia():
    númeroA = 0
    númeroB = 0
    return

def sacarNRaíz():
    númeroA = 0
    númeroB = 0
    return

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
    ventanaPrincipal.columnconfigure(1, weight=1)
    PantallaParaEscribirNúmeros.insert(0, "")
    PantallaParaEscribirNúmeros.focus_set()
    
    PantallaParaResultadoEjercicio = Entry(ventanaPrincipal, font=("Century" , 20), bg=celeste_claro, fg=celeste_oscuro, bd=1, justify="right", state="readonly")
    PantallaParaResultadoEjercicio.grid(row=50, column=0, columnspan=15, padx=10, pady=50, sticky="we")

def Botón(ventanaPrincipal):
    
    BotónCalcular = Button(ventanaPrincipal, text="Calcular", font=("Century", 10), bg=celeste_claro, fg=negro, bd=1, justify="right", command=Calcular)
    BotónCalcular.place(x=0, y=400 + 15, width=(100//2) + 10, height=(50//2))
    BotónCalcular.config(state="normal")
    
    BotónBorrar = Button(ventanaPrincipal, text="Borrar", font=("Century", 10), bg=rojo_claro, fg=negro, bd=1, justify="right", command=borrarÚltimo)
    BotónBorrar.place(x=0, y=400 + 45, width=(100//2) + 10, height=(50//2))
    BotónBorrar.config(state="normal")
    
    BotónSuma = Button(ventanaPrincipal, text="+", font=("Century", 25//2), bg=rojo_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "+"))
    BotónSuma.place(x=+0, y=100, width=25, height=25)
    BotónSuma.config(state="normal")
    
    BotónResta = Button(ventanaPrincipal, text="-", font=("Century", 25//2), bg=amarillo_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "-"))
    BotónResta.place(x=+25, y=100, width=25, height=25)
    BotónResta.config(state="normal")
    
    BotónMultiplicación = Button(ventanaPrincipal, text="*", font=("Century", 25//2), bg=verde_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "*"))
    BotónMultiplicación.place(x=+50, y=100, width=25, height=25)
    BotónMultiplicación.config(state="normal")
    
    BotónDivisión = Button(ventanaPrincipal, text="÷", font=("Century", 25//2), bg=azul_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "÷"))
    BotónDivisión.place(x=+75, y=100, width=25, height=25)
    BotónDivisión.config(state="normal")
    
    BotónPotencia = Button(ventanaPrincipal, text="^", font=("Century", 25//2), bg=violeta_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "^"))
    BotónPotencia.place(x=+100, y=100, width=25, height=25)
    BotónPotencia.config(state="normal")
    
    BotónRaíz = Button(ventanaPrincipal, text="ⁿ√", font=("Century", 25//2), bg=naranja_oscuro, fg=negro, bd=1, justify="left", command=lambda: PantallaParaEscribirNúmeros.insert(tk.END, "ⁿ√"))
    BotónRaíz.place(x=+125, y=100, width=25, height=25)
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