import mysql.connector
from datetime import datetime
from tipo_empleado import tipo_empleado
from rol import rol_empleado
import tkinter as tk
from tkinter import messagebox, ttk

class empleado(tipo_empleado, rol_empleado):
    def __init__(self, id_empleado, rut, nombre, direccion, telefono, correo_personal, fecha_inicio_contrato, salario, id_tipo_empleado, id_rol_empleado, habilitado_para_visualizar):
        tipo_empleado.__init__(self, id_tipo_empleado)
        rol_empleado.__init__(self, id_rol_empleado)
        self.id_empleado = id_empleado
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo_P = correo_personal
        self.fecha_inicio_contrato = fecha_inicio_contrato
        self.salario = salario
        self.habilitado_para_visualizar = habilitado_para_visualizar

    def validar_rut():
        pass

    def fecha_contrato():
        pass

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Empleados")

        labels = ['ID Empleado', 'RUT', 'Nombre', 'Dirección', 'Teléfono', 'Correo', 'Fecha Inicio', 'Salario', 'ID Tipo Empleado', 'ID Rol Empleado']
        self.entries = {}

        for label in labels:
            row = tk.Frame(self.root)
            lbl = tk.Label(row, text=label, width=20)
            ent = tk.Entry(row)
            lbl.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            row.pack(padx=5, pady=5)
            self.entries[label] = ent

        self.checkbox_var = tk.BooleanVar(value=True)
        self.checkbox = tk.Checkbutton(self.root, text="Habilitado para Visualizar", variable=self.checkbox_var)
        self.checkbox.pack(pady=5)

        self.btn_registrar = tk.Button(self.root, text="Registrar", command=self.registrar_empleado)
        self.btn_registrar.pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("ID Empleado", "RUT", "Nombre", "Dirección", "Teléfono", "Correo", "Fecha Inicio", "Salario", "ID Tipo Empleado", "ID Rol Empleado"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=120)
        
        self.tree.pack(pady=10, fill="both", expand=True)

        # Botón para deshabilitar empleados
        self.btn_deshabilitar = tk.Button(self.root, text="Deshabilitar Empleado", command=self.deshabilitar_empleado)
        self.btn_deshabilitar.pack(pady=10)

        self.mostrar_empleados()

    def registrar_empleado(self):
        try:
            id_empleado = self.entries['ID Empleado'].get()
            rut = self.entries['RUT'].get()
            nombre = self.entries['Nombre'].get()
            direccion = self.entries['Dirección'].get()
            telefono = self.entries['Teléfono'].get()
            correo = self.entries['Correo'].get()
            fecha_inicio = self.entries['Fecha Inicio'].get()
            salario = float(self.entries['Salario'].get())
            id_tipoempleado = self.entries['ID Tipo Empleado'].get()
            id_rol_empleado = self.entries['ID Rol Empleado'].get()
            habilitado_para_visualizar = self.checkbox_var.get()

            fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y").date()

            nuevo_empleado = empleado(id_empleado, rut, nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipoempleado, id_rol_empleado, habilitado_para_visualizar)
            self.guardar_empleado_bd(nuevo_empleado)
            self.mostrar_empleados()
            messagebox.showinfo("Registro", "Empleado registrado exitosamente!")
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Por favor, verifica que los datos sean correctos.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error de Base de Datos", f"Error: {err}")

    def guardar_empleado_bd(self, empleado):
        try:
            cnx = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                database="gestión de empleados"
            )
            cursor = cnx.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleados (
                    id_empleado VARCHAR(50) PRIMARY KEY,
                    rut VARCHAR(50),
                    nombre VARCHAR(100),
                    direccion VARCHAR(100),
                    telefono VARCHAR(20),
                    correo_personal VARCHAR(100),
                    fecha_inicio_contrato DATE,
                    salario DECIMAL(10, 2),
                    id_tipo_empleado VARCHAR(50),
                    id_rol_empleado VARCHAR(50),
                    habilitado_para_visualizar BOOLEAN
                )
            """)

            insertar = """
                INSERT INTO empleados (id_empleado, rut, nombre, direccion, telefono, correo_personal, fecha_inicio_contrato, salario, id_tipo_empleado, id_rol_empleado, habilitado_para_visualizar)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (empleado.id_empleado, empleado.rut, empleado.nombre, empleado.direccion, empleado.telefono, empleado.correo_P, empleado.fecha_inicio_contrato, empleado.salario, empleado.id_tipo_empleado, empleado.id_rol_empleado, empleado.habilitado_para_visualizar)
            cursor.execute(insertar, valores)

            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            raise

    def mostrar_empleados(self):
        try:
            cnx = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                database="gestión de empleados"
            )
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM empleados WHERE habilitado_para_visualizar = TRUE")
            rows = cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert("", tk.END, values=row)
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error de Base de Datos", f"Error: {err}")

    def deshabilitar_empleado(self):
        selected_item = self.tree.selection()
        if selected_item:
            empleado_id = self.tree.item(selected_item)['values'][0]
            try:
                cnx = mysql.connector.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password="",
                    database="gestión de empleados"
                )
                cursor = cnx.cursor()
                cursor.execute("UPDATE empleados SET habilitado_para_visualizar = FALSE WHERE id_empleado = %s", (empleado_id,))
                cnx.commit()
                cursor.close()
                cnx.close()
                messagebox.showinfo("Actualización", "Empleado deshabilitado exitosamente!")
                self.mostrar_empleados()
            except mysql.connector.Error as err:
                messagebox.showerror("Error de Base de Datos", f"Error: {err}")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para deshabilitar.")

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.checkbox_var.set(True)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
