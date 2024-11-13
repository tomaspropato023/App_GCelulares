from config import conectar_db
from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, END, messagebox

# Crear Celular
def crear_celular():
    try:
        id_cliente = int(entry_id_cliente.get())
        marca = entry_marca.get()
        modelo = entry_modelo.get()
        if id_cliente and marca and modelo:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO celulares (id_cliente, marca, modelo) VALUES (%s, %s, %s)", (id_cliente, marca, modelo))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Celular registrado con éxito.")
            entry_id_cliente.delete(0, END)
            entry_marca.delete(0, END)
            entry_modelo.delete(0, END)
            mostrar_celulares()
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
    except ValueError:
        messagebox.showerror("Error", "El ID del cliente debe ser un número.")

# Leer Celulares
def obtener_celulares():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT celulares.id_celular, clientes.nombre, celulares.marca, celulares.modelo 
        FROM celulares 
        JOIN clientes ON celulares.id_cliente = clientes.id_cliente
    """)
    celulares = cursor.fetchall()
    conn.close()
    return celulares

# Mostrar Celulares en Listbox
def mostrar_celulares():
    lista_celulares.delete(0, END)
    for celular in obtener_celulares():
        lista_celulares.insert(END, f"{celular[0]} - {celular[1]} - {celular[2]} - {celular[3]}")

# Actualizar Celular
def actualizar_celular():
    try:
        id_celular = int(entry_id.get())
        id_cliente = int(entry_id_cliente.get())
        marca = entry_marca.get()
        modelo = entry_modelo.get()
        if id_cliente and marca and modelo:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE celulares SET id_cliente=%s, marca=%s, modelo=%s WHERE id_celular=%s", (id_cliente, marca, modelo, id_celular))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Celular actualizado exitosamente.")
            entry_id.delete(0, END)
            entry_id_cliente.delete(0, END)
            entry_marca.delete(0, END)
            entry_modelo.delete(0, END)
            mostrar_celulares()
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
    except ValueError:
        messagebox.showerror("Error", "ID del celular y del cliente deben ser números.")

# Eliminar Celular
def eliminar_celular():
    try:
        id_celular = int(entry_id.get())
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM celulares WHERE id_celular=%s", (id_celular,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Celular eliminado exitosamente.")
        entry_id.delete(0, END)
        entry_id_cliente.delete(0, END)
        entry_marca.delete(0, END)
        entry_modelo.delete(0, END)
        mostrar_celulares()
    except ValueError:
        messagebox.showerror("Error", "Por favor, selecciona un celular válido.")

# Función para manejar la selección en la lista
def seleccionar_celular(event):
    seleccion = lista_celulares.get(lista_celulares.curselection())
    id_celular, cliente_nombre, marca, modelo = seleccion.split(" - ")
    entry_id.delete(0, END)
    entry_id.insert(END, id_celular)
    entry_id_cliente.delete(0, END)
    entry_id_cliente.insert(END, cliente_nombre)  # Para mostrar cliente de referencia, si se desea otro dato, cambiar aquí
    entry_marca.delete(0, END)
    entry_marca.insert(END, marca)
    entry_modelo.delete(0, END)
    entry_modelo.insert(END, modelo)

# Configuración de la ventana principal
root = Tk()
root.title("Gestión de Celulares")
root.geometry("500x500")

# Widgets para el CRUD de Celulares
Label(root, text="ID Celular").pack()
entry_id = Entry(root)
entry_id.pack()

Label(root, text="ID Cliente").pack()
entry_id_cliente = Entry(root)
entry_id_cliente.pack()

Label(root, text="Marca").pack()
entry_marca = Entry(root)
entry_marca.pack()

Label(root, text="Modelo").pack()
entry_modelo = Entry(root)
entry_modelo.pack()

# Botones de acción
Button(root, text="Registrar Celular", command=crear_celular).pack(pady=5)
Button(root, text="Actualizar Celular", command=actualizar_celular).pack(pady=5)
Button(root, text="Eliminar Celular", command=eliminar_celular).pack(pady=5)

# Listbox para mostrar celulares
lista_celulares = Listbox(root, width=60)
lista_celulares.pack(pady=10)

# Scrollbar para Listbox
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
lista_celulares.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_celulares.yview)

# Cargar lista de celulares y manejar selección
lista_celulares.bind("<<ListboxSelect>>", seleccionar_celular)
mostrar_celulares()

# Iniciar el loop de Tkinter
root.mainloop()