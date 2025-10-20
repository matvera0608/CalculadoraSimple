from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto
from calculadora_principal import color, borrarTODO, escribirCeros, formatearEntrada
from operaciones import formatearNúmeroResultado, parsear
import os
"""
watchmedo auto-restart --pattern="*.py" --recursive -- python detector_de_números_primos_y_compuestos.py #Este es para vigilar mi programa cada vez que reinicio la ejecución
"""
dir_imagen = os.path.dirname(__file__)
icono = os.path.join(dir_imagen, "imagenes", "íconos", "ícono detector.ico")

def detectar_divisores(número):
    try:
        if número < 2:
            return False, []
        divisores = [índice for índice in range(1, número + 1) if número % índice == 0]
        return (len(divisores) == 2, divisores)
    except TypeError:
        mensajeDeTexto.showerror("Error de tipo", f"Se esperaba un número entero > 1, pero se recibió: {type(número).__name__}.")
        texto.config(state="disabled", fg=color["negro"])
        return False, []
    

def mostrar():
    try:
        valor = parsear(entryNúmero.get().strip())
        núm_format = formatearNúmeroResultado(valor)
        primo, divisores = detectar_divisores(valor)
        divisores = [formatearNúmeroResultado(d) for d in divisores]
        if valor < 2:
            mensajeDeTexto.showinfo("Resultado", f"El número {núm_format} no es ni primo ni compuesto. Además no puede ser 0, 1 ni negativo.")
            texto.delete(0, tk.END)
            texto.tag_configure("centrado", justify="center")
            texto.config(state="disabled", fg=color["negro"])
        else: 
            texto.config(state="normal")
            texto.delete("1.0", tk.END) #Borrar contenido anterior
            texto.tag_configure("centrado", justify="center")
            texto.insert(tk.END, "Resultado\n", "centrado")
            if primo:
                lbResultado.config(text="PRIMO", fg=color["rojo"])
                texto.insert(tk.END, "\n".join(divisores))
                texto.config(state="disabled", fg=color["rojo"])
            else:
                lbResultado.config(text="COMPUESTO", fg=color["verde"])
                texto.insert(tk.END, "\n".join(divisores))
                texto.config(state="disabled", fg=color["verde"])
    except:
        mensajeDeTexto.showerror("Error", "Por favor ingrese un número válido")

def interfaz_detector():
    
    global interfaz, entryNúmero, texto, lbResultado, color_fondo
    interfaz = tk.Toplevel()
    interfaz.title("Número primo o compuesto")
    interfaz.geometry("650x300")
    interfaz.config(bg="white")
    interfaz.iconbitmap(icono)
    interfaz.resizable(False, False)

    color_fondo = interfaz.cget('bg')

    entryNúmero = tk.Entry(interfaz, font=("Courier New", 15, "bold"), bd=4)
    entryNúmero.grid(row=0, column=0, padx=0, pady=10, sticky="wn")
    entryNúmero.bind("<Control-BackSpace>", lambda e: borrarTODO(entryNúmero))
    entryNúmero.bind("<Alt-0>", lambda e: escribirCeros(entryNúmero,"00"))
    entryNúmero.bind("<Control-0>", lambda e: escribirCeros(entryNúmero,"000"))
    entryNúmero.bind("<Return>", lambda e: mostrar())
    entryNúmero.bind("<KeyRelease>", lambda e: formatearEntrada(entryNúmero))


    marco = tk.Frame(interfaz, bg=color_fondo, bd=2, relief="groove")
    marco.grid(row=0, column=2, padx=10, pady=10, sticky="nsew", rowspan=2)

    texto = tk.Text(marco, width=30, height=10, font=("Courier New", 15, "bold"), wrap="word")

    desplazador = tk.Scrollbar(marco, command=texto.yview)
    desplazador.pack(side="right", fill="y")
    texto.tag_configure("centrado", justify="center")
    texto.insert(tk.END, "Resultado\n", "centrado")
    texto.pack(fill="both", expand=True)
    texto.config(state="disabled")

    lbResultado = tk.Label(marco, font=("Courier New", 15, "bold"), bg=color_fondo)
    lbResultado.pack(pady=5)

    btnDetectar = tk.Button(interfaz, text="Detectar", font=("Courier New", 15, "bold"), bg="blue", fg="white", bd=1, cursor="hand2", command=mostrar)
    btnDetectar.grid(row=1, column=0, columnspan=2, pady=20, sticky="n")
    btnDetectar.bind("<Enter>", lambda e: btnDetectar.config(bg="red"))
    btnDetectar.bind("<Leave>", lambda e: btnDetectar.config(bg="blue"))
