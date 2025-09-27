from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto
import os
"""
watchmedo auto-restart --pattern="*.py" --recursive -- python detector_de_números_primos_y_compuestos.py #Este es para vigilar mi programa cada vez que reinicio la ejecución
"""
dir_imagen = os.path.dirname(__file__)
icono = os.path.join(dir_imagen, "imagenes", "íconos", "ícono detector.ico")

def detectar_divisores(número):
    if número < 2:
        return False
    divisores = []
    for índice in range(1, número + 1):
        if número % índice == 0:
            divisores.append(índice)
    return (len(divisores) == 2, divisores)
    

def mostrar():
    try:
        valor = int(entryNúmero.get().strip())
        primo, divisores = detectar_divisores(valor)
        
        texto.config(state="normal")
        texto.delete("1.0", tk.END)
        
        if valor >= 2:
            if primo:
                texto.config()
            else:
                texto.config()
        else:
            mensajeDeTexto.showwarning("ADVERTENCIA", "El valor no debe ser 0 ni 1 si querés saber que números es primo y compuesto")
        
        texto.insert(tk.END, f"Divisores: {', '.join(map(str, divisores))}")
        texto.config(state="normal")
        
    except ValueError:
        mensajeDeTexto.showerror("Error", "Por favor ingrese un número válido")
        
    
interfaz = tk.Tk()
interfaz.title("Número primo o compuesto")
interfaz.geometry("600x350")
interfaz.config(bg="white")
interfaz.iconbitmap(icono)
interfaz.resizable(False, False)

entryNúmero = tk.Entry(interfaz, font=("Courier New", 15, "bold"), bd=4)
entryNúmero.grid(row=0, column=0, padx=0, pady=10, sticky="wn")

marco = tk.LabelFrame(interfaz, text="Resultado", font=("Courier New", 10, "bold"), bg="white",fg="blue", bd=2, relief="groove")
marco.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

texto = tk.Text(marco, width=40, height=15, font=("Courier New", 10, "bold"), wrap="word")
texto.pack(fill="both", expand=True)
texto.config(state="disabled")

btnDetectar = tk.Button(interfaz, text="Detectar", font=("Courier New", 15, "bold"), bg="blue", fg="white", bd=1, cursor="hand2", command=mostrar)
btnDetectar.grid(row=1, column=0, columnspan=1, padx=5, pady=0, sticky="ws")
btnDetectar.bind("<Enter>", lambda e: btnDetectar.config(bg="red"))
btnDetectar.bind("<Leave>", lambda e: btnDetectar.config(bg="blue"))

interfaz.mainloop()