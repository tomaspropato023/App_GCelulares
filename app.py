import tkinter as tk
from tkinter import messagebox
import clientes
import celulares
import repuestos

# Funciones para abrir las ventanas de gestión
def gestionar_clientes():
    ventana_clientes = tk.Toplevel(root)
    ventana_clientes.title("Gestión de Clientes")
    # Aquí puedes llamar a funciones de clientes.py para CRUD y mostrar la interfaz de cliente

def gestionar_celulares():
    ventana_celulares = tk.Toplevel(root)
    ventana_celulares.title("Gestión de Celulares")
    # Aquí puedes llamar a funciones de celulares.py para CRUD y mostrar la interfaz de celulares

def gestionar_repuestos():
    ventana_repuestos = tk.Toplevel(root)
    ventana_repuestos.title("Gestión de Repuestos")
    # Aquí puedes llamar a funciones de repuestos.py para CRUD y mostrar la interfaz de repuestos

# Configuración de la ventana principal
root = tk.Tk()
root.title("Menú de Gestión - Negocio de Reparación de Celulares")
root.geometry("300x200")

# Botones del menú principal
btn_clientes = tk.Button(root, text="Gestionar Clientes", command=gestionar_clientes)
btn_clientes.pack(pady=10)

btn_celulares = tk.Button(root, text="Gestionar Celulares", command=gestionar_celulares)
btn_celulares.pack(pady=10)

btn_repuestos = tk.Button(root, text="Gestionar Repuestos", command=gestionar_repuestos)
btn_repuestos.pack(pady=10)

# Iniciar el loop principal de Tkinter
root.mainloop()