from empleado import empleado
class departamento(empleado):
    def __init__(self,id_departamento,nombre_departamento,telefono_departamento,id_empleado):
        super().__init__(id_empleado)
        self.id_departamento = id_departamento
        self.nombre_departamento = nombre_departamento
        self.telefono_departamento = telefono_departamento