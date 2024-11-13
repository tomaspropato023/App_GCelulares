import tkinter as tk
from tkinter import messagebox
import subprocess

# Funciones para abrir los archivos de gestión en ventanas independientes
def gestionar_clientes():
    try:
        subprocess.Popen(["python", "clientes.py"])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo clientes.py: {e}")

def gestionar_celulares():
    try:
        subprocess.Popen(["python", "celulares.py"])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo celulares.py: {e}")

def gestionar_repuestos():
    try:
        subprocess.Popen(["python", "repuestos.py"])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo repuestos.py: {e}")

def gestionar_reparaciones():
    try:
        subprocess.Popen(["python", "reparaciones.py"])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo reparaciones.py: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Menú de Gestión - Negocio de Reparación de Celulares")
root.geometry("300x250")

# Botones del menú principal
btn_clientes = tk.Button(root, text="Gestionar Clientes", command=gestionar_clientes)
btn_clientes.pack(pady=10)

btn_celulares = tk.Button(root, text="Gestionar Celulares", command=gestionar_celulares)
btn_celulares.pack(pady=10)

btn_repuestos = tk.Button(root, text="Gestionar Repuestos", command=gestionar_repuestos)
btn_repuestos.pack(pady=10)

btn_reparaciones = tk.Button(root, text="Gestionar Reparaciones", command=gestionar_reparaciones)
btn_reparaciones.pack(pady=10)

# Iniciar el loop principal de Tkinter
root.mainloop()
