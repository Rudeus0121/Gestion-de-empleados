from empleado import empleado

class rol(empleado):
    def __init__(self, id_empleado, nombre_accesos, nombre_modulos):
        super().__init__(id_empleado)
        self.nombre_accesos = nombre_accesos
        self.nombre_modulos = nombre_modulos
        