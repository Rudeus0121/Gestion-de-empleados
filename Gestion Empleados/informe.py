from empleado import empleado

class informe(empleado):
    def __init__(self, id_informe, nombre_informe, fecha_creacion, ubicacion, id_empleado, habilitado_para_visualizar):
        super().__init__(id_empleado)
        self.id_informe = id_informe
        self.nombre_informe = nombre_informe
        self.fecha_creacion = fecha_creacion
        self.ubicacion = ubicacion
        self.habilitado_para_visualizar = habilitado_para_visualizar

    def generar_n_informes():
        pass

    def exportar_informe():
        pass 