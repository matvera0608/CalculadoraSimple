from tkinter import *
import tkinter as tk, tkinter.messagebox as mensajeDeTexto

def parsear(texto):
    try:
        númLimpio = texto.replace(".", "").replace(",", ".")
        valor = float(númLimpio)
        if valor.is_integer():
            valor = int(valor)
        return valor
    except ValueError:
        return None

#Esta función es similar a la anterior pero formatea el resultado final
def formatearNúmeroResultado(valor):
    try:
        if isinstance(valor, str):
            valor = parsear(valor)
        if valor is None:
            return "Error"

        if isinstance(valor, float) and not valor.is_integer():
            parteEntera, parteDecimal = str(valor).split(".")
            parteEntera = f"{int(parteEntera):,}".replace(",", ".")
            parteDecimal = parteDecimal.rstrip("0")
            return f"{parteEntera},{parteDecimal}" if parteDecimal else parteEntera
        else:
            return f"{int(valor):,}".replace(",", ".")
    except Exception:
        return "Error"

#Crearé una función que llame a las funciones aritméticas según los signos para el botón de Calcular
def Calcular(PantallaEntrada, PantallaSalida):
    entrada = PantallaEntrada.get()
    #Esta función calcula la expresión completa como una operación combinada
    def calcularExpresiónCompleta():
        try:
            resultado = eval(expresión)
            mostrarResultado(resultado, PantallaSalida)
        except Exception:
            mensajeDeTexto.showerror("ERROR", "La expresión es inválida")
            return
        
    def normalizarExpresión(expresión):
        mapa = {
            "÷÷": "//",
            "÷": "/",
            "×": "*",
            "^": "**",
            ",": ".",
            }
        
        for exp, equi in mapa.items():
            expresión = expresión.replace(exp, equi)
        return expresión
    expresión = normalizarExpresión(entrada)
    #Esta condición es para especificar que operación debe realizar sin depender de llamar funciones matemáticas de forma particular
    if "÷÷" in expresión or "//" in expresión:   # división entera
        resultado = dividirEntero(entrada)
        mostrarResultado(resultado, PantallaSalida)
        return
    elif "÷" in expresión or "/" in expresión:  # división normal
        resultado = dividir(entrada)
        mostrarResultado(resultado, PantallaSalida)
        return
    elif "*" in expresión or "×" in expresión:
        resultado = multiplicar(entrada)
        mostrarResultado(formatearNúmeroResultado(resultado), PantallaSalida)
        return
    elif "**" in expresión:
        resultado = sacarNPotencia(entrada)
        mostrarResultado(formatearNúmeroResultado(resultado), PantallaSalida)
        return
    elif "ⁿ√" in expresión:
        resultado = sacarNRaíz(entrada)
        mostrarResultado(formatearNúmeroResultado(resultado), PantallaSalida)
        return
    elif "+" in expresión:
        resultado = sumar(entrada)
        mostrarResultado(formatearNúmeroResultado(resultado), PantallaSalida)
        return
    elif "-" in expresión:
        resultado = restar(entrada)
        mostrarResultado(formatearNúmeroResultado(resultado), PantallaSalida)
        return
    elif "%" in expresión:
        resultado = sacarPorcentaje(entrada)
        mostrarResultado(formatearNúmeroResultado(resultado), PantallaSalida)
        return
    else:
        pass
      
    operadores = "+-*/÷×"
    
    siHaySignos_o_Paréntesis = any(op in entrada for op in operadores) or "(" in entrada or ")" in entrada

    if siHaySignos_o_Paréntesis:
        calcularExpresiónCompleta()
        return
    
#Esta sección tendrán funciones para los cálculos
def sumar(entrada):
    parte = entrada.split("+")
        #creo un try-except para manejar mejor las excepciones o errores de validación
    try:
        #este resultado ya hace suma dinámica con n cantidad de números
        partes = [float(p.strip().replace(".", "").replace(",", ".")) 
                        for p in parte if p.strip() != ""]
       
        #Creo una condición para que me obligue a poner mínimo 2 números para hacer la operación.
        falta_de_operandos = len(partes) < 2
        if falta_de_operandos:
            return
        
        return sum(partes)
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def restar(entrada):
    parte = entrada.split("-")
    try:
        partes = [float(p.strip().replace(".", "").replace(",", ".")) for p in parte if p.strip() != ""]
        if len(partes) < 2:
            mensajeDeTexto.showerror("Error", "Faltan operandos para restar.")
            return
        resultado = partes[0]
        for n in partes[1:]:
            resultado -= n
        
        return resultado
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def multiplicar(entrada):
    parte = entrada.split("*")
    try:
        números = []
        for p in parte:
            if p.strip() == "":
                continue
            if "%" in p:
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
        return resultado
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def dividir(entrada, resultadoWidget=None):
    from calculadora_principal import color
     #las variables necesarias
    parte = entrada.replace("÷","/").split("/")
    #Controlo con try-except para evitar cualquier fallo o excepción de signos 
    try:
        #Acá hago la división de cantidad enésima de números, es decir, más de 2 en adelante.
        números = [float(p.strip().replace(".", "").replace(",", ".")) for p in parte if p.strip() != ""]
        
        falta_de_operandos = len(números) < 2
        
        if falta_de_operandos:
            mensajeDeTexto.showerror("Error", "Faltan operandos para dividir.")
            return
        
        resultado = números[0]
        print(f"{entrada}, {parte}")
        #Acá itero para ir restando los números hasta llegar a negativo
        for n in números[1:]:
            divisiónEntre0 = n == 0
            if divisiónEntre0:
                resultadoWidget.config(state="normal", font=("Courier New", 10), fg=color["rojo_anaranjado"])
                resultadoWidget.delete(0, tk.END)
                resultadoWidget.insert(0, "NO SE DIVIDE POR CERO 😡")
                resultadoWidget.config(state="readonly")
                return
            resultado /= n
            resultadoWidget.config(state="normal", font=("Courier New", 30))
            
        mostrarResultado(resultado)
        
        # Mostrar el módulo (resto) de la división cuando sea posible y son 2 números enteros
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def dividirEntero(entrada, resultadoWidget=None, resto=None, color=None):
    #las variables necesarias
    parte = entrada.replace("÷÷", "//").split("//")
    #Controlo con try-except para evitar cualquier fallo o excepción de signos 
    try:
        #Acá hago la división de cantidad enésima de números, es decir, más de 2 en adelante.
        números = [float(p.strip().replace(".", "").replace(",", ".")) for p in parte if p.strip() != ""]
        
        falta_de_operandos = len(números) < 2
        
        if falta_de_operandos:
            mensajeDeTexto.showerror("Error", "Faltan operandos para dividir.")
            return
        
        resultado = números[0]
        #Acá itero para ir restando los números hasta llegar a negativo
        for n in números[1:]:
            divisiónEntre0 = n == 0
            if divisiónEntre0:
                resultadoWidget.config(state="normal", font=("Courier New", 10), fg=color["rojo_anaranjado"])
                resultadoWidget.delete(0, tk.END)
                resultadoWidget.insert(0, "NO SE DIVIDE POR CERO 😡")
                resultadoWidget.config(state="readonly")
                return
            resultado //= n
           
            resultadoWidget.config(state="normal", font=("Courier New", 30))
            
        mostrarResultado(resultado)

        son_dos_o_más_enteros = len(números) >= 2 and all(n.is_integer() for n in números)

        if son_dos_o_más_enteros:
            resultado_módulo = int(números[0]) % int(números[1])
            resto.config(state="normal")
            resto.delete(0, tk.END)
            resto.insert(0, str(resultado_módulo))
            resto.config(state="readonly")   
        else:
            resto.config(state="normal")
            resto.delete(0, tk.END)
            resto.insert(0, "-")
            resto.config(state="readonly")     
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"No sirve usar cualquier valor inválido: {errorDeValidación}")

def sacarNPotencia(entrada):
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
            
def sacarNRaíz(entrada):
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
def sacarPorcentaje(entrada):
    tienePorcentaje = "%" not in entrada
    
    #Me acostumbro a poner try-except para refozar cualquier control de datos
    try:
        if tienePorcentaje:
            mensajeDeTexto.showinfo("FALTA DE SÍMBOLO", "ESCRIBIR EL SIGNO INDICADO DE PORCENTAJE AL ESPECIFICAR")
            return
        else:
            parte = entrada.replace("%", "").replace(".", "").replace(",", ".")
            número = float(parte)
            resultado = número/100
            mostrarResultado(resultado)
    except ValueError as errorDeValidación:
        mensajeDeTexto.showerror("ERROR", f"Algo no está bien: {errorDeValidación}")
    
#En esta función sólo muestro el resultado según la operación matemática donde se llame
def mostrarResultado(Resultado, WidgetResultado=None):
    
    if WidgetResultado:
        WidgetResultado.config(state="normal")
        WidgetResultado.delete(0, tk.END)
        WidgetResultado.insert(tk.END, Resultado)
        WidgetResultado.config(state="readonly")

#Esta función borra de a 1 número. No borra completamente al presionarlo
#el botón Borrar
def borrarÚltimo(Entrada):
    Entrada.config(state="normal")
    textoActual = Entrada.get()
    nuevoTexto = textoActual[:-1]
    Entrada.delete(0, tk.END)
    Entrada.insert(0, nuevoTexto)
    
#Esta función borra de a 1 número. No borra completamente al presionarlo
#el botón Borrar
def borrarTODO(Entrada, Resultado=None, Resto=None):
    Entrada.config(state="normal")
    Entrada.delete(0, tk.END)
    
    if Resultado:
        Resultado.config(state="normal")
        Resultado.delete(0, tk.END)
        Resultado.config(state="readonly")
    if Resto:
        Resto.config(state="normal")
        Resto.delete(0, tk.END)
        Resto.config(state="readonly")
    
    Entrada.focus_set()