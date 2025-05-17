from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto, tkinter.font as fuenteDeLetra, tkinter.simpledialog as diálogo

#Colores
celeste_claro = "#BDE3FF"
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
            mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido 🫵🏻🤬😡: {errorDeValidación}")
    else:
        mensajeDeTexto.showinfo("FALTA DE SÍMBOLO", "ESCRIBIR EL SIGNO INDICADO DE SUMA ")

def restar():
    númeroA = 0
    númeroB = 0
    return

def multiplicar():
    númeroA = 0
    númeroB = 0
    return

def dividir():
    númeroA = 0
    númeroB = 0
    return

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


# -*- coding: utf-8 -*-
#defino la función con valor de devolución o de retorno llamada calculadora()
#que va todos los botones necesarios para los cálculos necesarios
def pantallaCalculadora(ventanaPrincipal):
    global anchura, altura, PantallaParaEscribirNúmeros, PantallaParaResultadoEjercicio
    anchura = min(360, 550)
    altura = 100
    
    PantallaParaEscribirNúmeros = Entry(ventanaPrincipal, font=("Century", 25), bg=celeste_claro, fg=celeste_oscuro, bd=1, justify="right")
    PantallaParaEscribirNúmeros.config(state="normal")
    PantallaParaEscribirNúmeros.place(x=0, y=0, width=anchura, height=altura)
    PantallaParaEscribirNúmeros.insert(0, "")
    PantallaParaEscribirNúmeros.focus_set()
    
    PantallaParaResultadoEjercicio = Entry(ventanaPrincipal, font=("Century" , 20), bg=celeste_claro, fg=celeste_oscuro, bd=1, justify="right")
    PantallaParaResultadoEjercicio.place(x=200, y=400, width=anchura-200, height=altura-50)
    PantallaParaResultadoEjercicio.config(state="readonly")
    
def Botón(ventanaPrincipal):
    
    BotónCalcular = Button(ventanaPrincipal, text="Calcular", font=("Century", 10), bg=celeste_claro, fg=negro, bd=1, justify="right", command=Calcular)
    BotónCalcular.place(x=0, y=400 + 15, width=(100//2) + 10, height=(50//2))
    BotónCalcular.config(state="normal")
    
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
    
    
def calculadora():
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Calculadora sencilla")
    ventanaPrincipal.geometry("360x640")
    ventanaPrincipal.maxsize(360, 640)
    ventanaPrincipal.minsize(360, 640)
    ventanaPrincipal.config(bg="white")
    ventanaPrincipal.resizable(10, 10)
    
    pantallaCalculadora(ventanaPrincipal)
    Botón(ventanaPrincipal)
    
    return ventanaPrincipal

#Defino una variable para disparar la interfaz gráfica de calculadora

calculadora_principal = calculadora()

calculadora_principal.mainloop()