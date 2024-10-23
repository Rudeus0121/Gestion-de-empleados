from tipo_empleado import tipo_empleado
class empleado(tipo_empleado):
    def __init__(self,id_empleado,rut,nombre,direccion,telefono,correo_P,fecha_inicio_contrato,salario,id_tipo_empleado):
        super().__init__(id_tipo_empleado)
        self.id_empleado = id_empleado
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo_P = correo_P
        self.fecha_inicio_contrato = fecha_inicio_contrato
        self.salario = salario

    def validar_rut():
        pass
    def fecha_contrato():
        pass