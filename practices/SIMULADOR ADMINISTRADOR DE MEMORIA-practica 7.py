import tkinter as tk
from tkinter import ttk, messagebox

# Inicializamos los datos
programa = {
    0: "cargar 5, 1",
    1: "cargar 3, 2",
    2: "sumar 1, 2, 3",
    3: "imprimir 3"
}

variables = {
    1: 0,
    2: 0,
    3: 0
}

instrucciones = list(programa.values())
espacio_memoria = {}

# Actualizar valores en la tabla de variables
def actualizar_tabla_variables():
    """Actualiza la tabla de variables en la interfaz gráfica."""
    for item in tabla_variables.get_children():
        tabla_variables.delete(item)
    for var, val in variables.items():
        tabla_variables.insert("", "end", values=(var, val))

# Actualizar las instrucciones cargadas en memoria
def actualizar_tabla_instrucciones():
    """Actualiza la tabla de instrucciones en memoria."""
    for item in tabla_instrucciones.get_children():
        tabla_instrucciones.delete(item)
    for dir_mem, instruccion in espacio_memoria.items():
        tabla_instrucciones.insert("", "end", values=(dir_mem, instruccion))

# Simular la carga del programa en memoria
def cargar_programa():
    """Carga las instrucciones en memoria simulada."""
    espacio_memoria.clear()
    for i, instruccion in enumerate(instrucciones):
        espacio_memoria[i] = instruccion
    actualizar_tabla_instrucciones()
    messagebox.showinfo("Cargar Programa", "El programa se ha cargado en memoria.")

# Simular la asignación de memoria a las variables
def asignar_memoria_variables():
    """Asigna espacio de memoria a las variables."""
    for key in variables.keys():
        variables[key] = 0
    actualizar_tabla_variables()
    messagebox.showinfo("Asignar Memoria", "Se ha asignado espacio de memoria a las variables.")

# Ejecutar el programa paso a paso
indice_instruccion = 0
def ejecutar_instruccion():
    """Ejecuta una instrucción del programa paso a paso y actualiza el estado."""
    global indice_instruccion
    if indice_instruccion < len(instrucciones):
        instruccion = instrucciones[indice_instruccion]
        try:
            if instruccion.startswith("cargar"):
                _, valor, var = instruccion.replace(",", "").split(" ")
                variables[int(var)] = int(valor)
            elif instruccion.startswith("sumar"):
                _, var1, var2, var3 = instruccion.replace(",", "").split(" ")
                variables[int(var3)] = variables[int(var1)] + variables[int(var2)]
            elif instruccion.startswith("imprimir"):
                _, var = instruccion.replace(",", "").split(" ")
                resultado.set(f"Resultado: {variables[int(var)]}")
            # Actualizar interfaz gráfica
            actualizar_tabla_variables()
            indice_instruccion += 1
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar la instrucción: {str(e)}")
    else:
        messagebox.showinfo("Fin del Programa", "Todas las instrucciones han sido ejecutadas.")

# Reiniciar el programa
def reiniciar_programa():
    """Reinicia las variables y el programa."""
    global indice_instruccion
    indice_instruccion = 0
    for key in variables.keys():
        variables[key] = 0
    resultado.set("Resultado: ")
    espacio_memoria.clear()
    actualizar_tabla_variables()
    actualizar_tabla_instrucciones()

# Crear la ventana principal
root = tk.Tk()
root.title("Simulador de Administración de Memoria")

# Etiqueta de título
titulo = tk.Label(root, text="Simulador de Administración de Memoria", font=("Arial", 16))
titulo.pack(pady=10)

# Sección de memoria para variables
frame_variables = ttk.LabelFrame(root, text="Memoria de Variables")
frame_variables.pack(pady=10)

tabla_variables = ttk.Treeview(frame_variables, columns=("Variable", "Valor"), show="headings", height=5)
tabla_variables.heading("Variable", text="Variable")
tabla_variables.heading("Valor", text="Valor")
tabla_variables.pack()

# Sección de memoria para instrucciones
frame_instrucciones = ttk.LabelFrame(root, text="Memoria de Instrucciones")
frame_instrucciones.pack(pady=10)

tabla_instrucciones = ttk.Treeview(frame_instrucciones, columns=("Dirección", "Instrucción"), show="headings", height=5)
tabla_instrucciones.heading("Dirección", text="Dirección")
tabla_instrucciones.heading("Instrucción", text="Instrucción")
tabla_instrucciones.pack()

# Botones de control
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

boton_cargar = tk.Button(frame_botones, text="Cargar Programa", command=cargar_programa, bg="blue", fg="white", font=("Arial", 12))
boton_cargar.grid(row=0, column=0, padx=5)

boton_asignar = tk.Button(frame_botones, text="Asignar Memoria Variables", command=asignar_memoria_variables, bg="orange", fg="white", font=("Arial", 12))
boton_asignar.grid(row=0, column=1, padx=5)

boton_ejecutar = tk.Button(frame_botones, text="Ejecutar Instrucción", command=ejecutar_instruccion, bg="green", fg="white", font=("Arial", 12))
boton_ejecutar.grid(row=0, column=2, padx=5)

boton_reiniciar = tk.Button(frame_botones, text="Reiniciar Programa", command=reiniciar_programa, bg="red", fg="white", font=("Arial", 12))
boton_reiniciar.grid(row=0, column=3, padx=5)

# Etiqueta para mostrar el resultado
resultado = tk.StringVar(value="Resultado: ")
resultado_label = tk.Label(root, textvariable=resultado, font=("Arial", 14), fg="blue")
resultado_label.pack(pady=10)

# Iniciar el bucle de la aplicación
root.mainloop()

#SARMIENTO RUIZ EDGAR MAURICIO
#OSORIO RAMIREZ MARLENE MARICELA 
#CUEVAS HERNANDEZ ERIK ISRAEL