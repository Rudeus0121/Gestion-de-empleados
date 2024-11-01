from proyecto_empleado import proyecto_empleado

class registro_tiempo(proyecto_empleado):
    def __init__(self, id_registrio_tiempo, fechas, horas_trabajadas, descripcion, id_proyecto_empleado, habilitado_para_visualizar):
        super().__init__(id_proyecto_empleado)
        self.id_resgitro_tiempo = id_registrio_tiempo
        self.fechas = fechas
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion
        self.habilitado_para_visualizar = habilitado_para_visualizar
    
    def validar_cantidad_horas_trabajadas():
        pass