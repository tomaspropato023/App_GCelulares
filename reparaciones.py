from config import conectar_db
from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, END, messagebox
from datetime import datetime

# Crear Reparación
def crear_reparacion():
    try:
        id_celular = int(entry_id_celular.get())
        fecha_ingreso = entry_fecha_ingreso.get()
        fecha_estimada_entrega = entry_fecha_estimada_entrega.get()
        estado = entry_estado.get()
        
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reparaciones (id_celular, fecha_ingreso, fecha_estimada_entrega, estado)
            VALUES (%s, %s, %s, %s)
        """, (id_celular, fecha_ingreso, fecha_estimada_entrega, estado))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Éxito", "Reparación agregada exitosamente.")
        limpiar_campos()
        mostrar_reparaciones()
    except ValueError:
        messagebox.showerror("Error", "El ID del celular debe ser un número entero y las fechas deben estar en formato YYYY-MM-DD.")

# Leer Reparaciones
def obtener_reparaciones():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT reparaciones.id_reparacion, reparaciones.id_celular, celulares.marca, celulares.modelo,
               reparaciones.fecha_ingreso, reparaciones.fecha_estimada_entrega, reparaciones.fecha_real_entrega,
               reparaciones.estado
        FROM reparaciones
        JOIN celulares ON reparaciones.id_celular = celulares.id_celular
    """)
    reparaciones = cursor.fetchall()
    conn.close()
    return reparaciones

# Mostrar Reparaciones en Listbox
def mostrar_reparaciones():
    lista_reparaciones.delete(0, END)
    for reparacion in obtener_reparaciones():
        lista_reparaciones.insert(END, f"{reparacion[0]} - Celular: {reparacion[2]} {reparacion[3]} - "
                                        f"Ingreso: {reparacion[4]} - Est. Entrega: {reparacion[5]} - "
                                        f"Real Entrega: {reparacion[6]} - Estado: {reparacion[7]}")

# Actualizar Reparación
def actualizar_reparacion():
    try:
        id_reparacion = int(entry_id_reparacion.get())
        id_celular = int(entry_id_celular.get())
        fecha_estimada_entrega = entry_fecha_estimada_entrega.get()
        fecha_real_entrega = entry_fecha_real_entrega.get()
        estado = entry_estado.get()
        
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE reparaciones 
            SET id_celular=%s, fecha_estimada_entrega=%s, fecha_real_entrega=%s, estado=%s
            WHERE id_reparacion=%s
        """, (id_celular, fecha_estimada_entrega, fecha_real_entrega, estado, id_reparacion))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Éxito", "Reparación actualizada exitosamente.")
        limpiar_campos()
        mostrar_reparaciones()
    except ValueError:
        messagebox.showerror("Error", "El ID de la reparación y del celular deben ser enteros y las fechas deben estar en formato YYYY-MM-DD.")

# Eliminar Reparación
def eliminar_reparacion():
    try:
        id_reparacion = int(entry_id_reparacion.get())
        
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reparaciones WHERE id_reparacion=%s", (id_reparacion,))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Éxito", "Reparación eliminada exitosamente.")
        limpiar_campos()
        mostrar_reparaciones()
    except ValueError:
        messagebox.showerror("Error", "Por favor, selecciona una reparación válida.")

# Limpiar campos
def limpiar_campos():
    entry_id_reparacion.delete(0, END)
    entry_id_celular.delete(0, END)
    entry_fecha_ingreso.delete(0, END)
    entry_fecha_estimada_entrega.delete(0, END)
    entry_fecha_real_entrega.delete(0, END)
    entry_estado.delete(0, END)

# Configuración de la ventana principal
root = Tk()
root.title("Gestión de Reparaciones")
root.geometry("600x600")

# Widgets para el CRUD de Reparaciones
Label(root, text="ID Reparación").pack()
entry_id_reparacion = Entry(root)
entry_id_reparacion.pack()

Label(root, text="ID Celular").pack()
entry_id_celular = Entry(root)
entry_id_celular.pack()

Label(root, text="Fecha Ingreso (YYYY-MM-DD)").pack()
entry_fecha_ingreso = Entry(root)
entry_fecha_ingreso.pack()

Label(root, text="Fecha Estimada de Entrega (YYYY-MM-DD)").pack()
entry_fecha_estimada_entrega = Entry(root)
entry_fecha_estimada_entrega.pack()

Label(root, text="Fecha Real de Entrega (YYYY-MM-DD)").pack()
entry_fecha_real_entrega = Entry(root)
entry_fecha_real_entrega.pack()

Label(root, text="Estado").pack()
entry_estado = Entry(root)
entry_estado.insert(0, "En proceso")  # Estado predeterminado
entry_estado.pack()

# Botones de acción
Button(root, text="Agregar Reparación", command=crear_reparacion).pack(pady=5)
Button(root, text="Actualizar Reparación", command=actualizar_reparacion).pack(pady=5)
Button(root, text="Eliminar Reparación", command=eliminar_reparacion).pack(pady=5)

# Listbox para mostrar reparaciones
lista_reparaciones = Listbox(root, width=80)
lista_reparaciones.pack(pady=10)

# Scrollbar para Listbox
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
lista_reparaciones.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_reparaciones.yview)

# Cargar lista de reparaciones
mostrar_reparaciones()

# Iniciar el loop de Tkinter
root.mainloop()