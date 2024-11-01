import mysql.connector
from datetime import datetime
from tipo_empleado import tipo_empleado
from rol import rol_empleado
import tkinter as tk
from tkinter import messagebox
class empleado(tipo_empleado, rol_empleado):
    def __init__(self,id_empleado,rut,nombre,direccion,telefono,correo_personal,fecha_inicio_contrato,salario,id_tipo_empleado, id_rol_empleado, habilitado_para_visualizar):
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

        # Crear etiquetas y entradas
        labels = ['ID Empleado', 'RUT', 'Nombre', 'Dirección', 'Teléfono', 'Correo', 'Fecha Inicio', 'Salario', 'ID Tipo Empleado', 'ID Rol Empleado']

        self.entries = {}

        for label in labels:
            row = tk.Frame(self.root)#crea el marco en la ventana principal
            lbl = tk.Label(row, text=label, width=20)#establece el ancho en este caso 20
            ent = tk.Entry(row)#el usuario puede ingresar informacion
            lbl.pack(side=tk.LEFT) # crea una etiqueta dentro del marco alineandola a la izquierda
            ent.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            row.pack(padx=5, pady=5)
            self.entries[label] = ent

        # Botón para registrar
        self.btn_registrar = tk.Button(self.root, text="Registrar", command=self.registrar_empleado)
        self.btn_registrar.pack(pady=10)

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

            fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y").date()

            nuevo_empleado = empleado(id_empleado, rut, nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipoempleado, id_rol_empleado )
            messagebox.showinfo("Registro", "Empleado registrado exitosamente!")

            self.guardar_empleado_bd(nuevo_empleado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, verifica que los datos sean correctos.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error de Base de Datos", f"Error: {err}")

    def guardar_empleado_bd(self, empleado):
        # Conectar a la base de datos
        try:
            cnx = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="gestión de empleados")
            cursor = cnx.cursor()

            # Crear la tabla si no existe
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
                    id_rol_empleado VARCHAR(50)
                )
            """)

            # Insertar los datos
            insertar = """
                INSERT INTO empleados (id_empleado, rut, nombre, direccion, telefono, correo_personal, fecha_inicio_contrato, salario, id_tipo_empleado, id_rol_empleado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (empleado.id_empleado, empleado.rut, empleado.nombre, empleado.direccion, empleado.telefono, empleado.correo_P, empleado.fecha_inicio_contrato, empleado.salario, empleado.id_tipo_empleado, empleado.id_rol_empleado)
            cursor.execute(insertar, valores)

            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            raise


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()