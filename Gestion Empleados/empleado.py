from tipo_empleado import tipo_empleado
from rol import rol_empleado
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class empleado(tipo_empleado, rol_empleado):
    def __init__(self,id_empleado,rut,nombre,direccion,telefono,correo_personal,fecha_inicio_contrato,salario,id_tipo_empleado, id_rol_empleado):
        tipo_empleado().__init__(id_tipo_empleado)
        rol_empleado().__init__(id_rol_empleado)
        self.id_empleado = id_empleado
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo_P = correo_personal
        self.fecha_inicio_contrato = fecha_inicio_contrato
        self.salario = salario

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

            nuevo_empleado = empleado(id_empleado, rut, nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipoempleado, id_rol_empleado )
            messagebox.showinfo("Registro", "Empleado registrado exitosamente!")

            # Aquí puedes agregar código para guardar el empleado en una base de datos o archivo

        except ValueError:
            messagebox.showerror("Error", "Por favor, verifica que los datos sean correctos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()