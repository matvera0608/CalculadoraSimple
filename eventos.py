from tkinter import *
import tkinter as tk

#Este espacio es para eventos como escribir ceros, resaltar botones, etc.
#Esta función escribe ceros en la pantalla de números, formateando la entrada
def escribirCeros(entrada_widget, núm):
    from calculadora_principal import formatearEntrada
    entrada_widget.insert(tk.END, núm)
    formatearEntrada(entrada_widget)


# Esta función resalta el botón al hacer clic y lo restaura al soltarlo usando bind para que se resalte y restaure el color del botón a nivel interno y visual.
# En comparación con el anterior, 
def clickearBotón(btn, colorResaltado, colorOrginal, letraOriginal):
    def resaltar(event):
        btn.config(bg=colorResaltado, fg=letraOriginal)
    def restaurar(event):
        btn.config(bg=colorOrginal, fg=letraOriginal)
    return resaltar, restaurar

def abrir__calculadora__de__divisas(event=None):
    from calc_divisas import calculadora_de_divisas
    calculadora_de_divisas()
    
def abrir__calculadora__de__primos(event=None):
    from detector_de_números_primos_y_compuestos import interfaz_detector
    interfaz_detector()