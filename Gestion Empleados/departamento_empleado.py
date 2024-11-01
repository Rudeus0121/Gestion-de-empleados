from empleado import empleado
from tipo_empleado import tipo_empleado
from departamento import departamento
class departamento_empleado(empleado, tipo_empleado):
    def __init__(self,id_departamento_empleado,id_empleado,id_tipo_empleado,id_departamento, habilitado_para_visualizar):
        empleado().__init__(id_empleado)
        tipo_empleado().__init__(id_tipo_empleado)
        departamento().__init__(id_departamento)
        self.id_departamento_empleado = id_departamento_empleado
        self.habilitado_para_visualizar = habilitado_para_visualizar
        
    def validar_asignacion():
        pass