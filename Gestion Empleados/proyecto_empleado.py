from empleado import empleado
from proyecto import proyecto
class proyecto_empleado(empleado, proyecto):
    def __init__(self,id_proyecto_empleado,id_empleado,id_proyecto, habilitado_para_visualizar):
        empleado().__init__(id_empleado)
        proyecto().__init__(id_proyecto)
        self.id_proyecto_empleado = id_proyecto_empleado
        self.habilitado_para_visualizar = habilitado_para_visualizar
