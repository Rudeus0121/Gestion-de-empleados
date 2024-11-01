import mysql.connector
# Connect to server
cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="gestión de empleados")

# Get a cursor
cursor = cnx.cursor()

datos_departamento = [
    (1, 'Recursos Humanos', 101, True),
    (2, 'Finanzas', 102, True),
    (3, 'Marketing', 103, True)
]

datos_departamento_empleado = [
    (1, 1, 1, 1, True),
    (2, 2, 1, 2, True)
]

datos_empleados = [
    (1, 12345678, 'Juan Pérez', 'Calle Falsa 123', 5551234, 'juan@mail.com', '2024-01-01', 50000, 1, 1, True),
    (2, 87654321, 'Ana López', 'Avenida Siempreviva 742', 5555678, 'ana@mail.com', '2024-02-01', 55000, 2, 2, True)
]

datos_informe = [
    (1, 'Informe Mensual', '2024-10-01', 'Carpeta/Informes', 1, True),
    (2, 'Informe Anual', '2024-10-30', 'Carpeta/Informes', 2, True)
]

datos_proyecto = [
    (1, 'Proyecto A', 'Desarrollo de software', '2024-01-01', '2024-12-31', True),
    (2, 'Proyecto B', 'Investigación de mercado', '2024-02-01', '2024-11-30', True)
]

datos_proyecto_empleado = [
    (1, 1, 1, True),
    (2, 2, 2, True)
]

datos_registro_tiempo = [
    (1, '2024-10-01', 8, 'Revisión de código', 1, True),
    (2, '2024-10-02', 7, 'Documentación', 2, True)
]

datos_tipo_empleado = [
    (1, 'Permanente', 'Empleado de planta', True),
    (2, 'Temporal', 'Empleado contratado por proyecto', True)
]

# Insertar datos en cada tabla
try:
    cursor.executemany('INSERT INTO departamento (id_departamento, nombre_departamento, numero_departamento, habilitado_para_visualizar) VALUES (%s, %s, %s, %s)', datos_departamento)
    cursor.executemany('INSERT INTO departamento_empleado (id_departamento_empleado, id_empleado, id_departamento, id_tipo_empleado, habilitado_para_visualizar) VALUES (%s, %s, %s, %s, %s)', datos_departamento_empleado)
    cursor.executemany('INSERT INTO empleados (id_empleado, rut, nombre, direccion, telefono, correo_personal, fecha_inicio_contrato, salario, id_tipo_empleado, id_rol_empleado, habilitado_para_visualizar) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', datos_empleados)
    cursor.executemany('INSERT INTO informe (id_informe, nombre_informe, fecha_creacion, ubicacion, id_empleado, habilitado_para_visualizar) VALUES (%s, %s, %s, %s, %s, %s)', datos_informe)
    cursor.executemany('INSERT INTO proyecto (id_proyecto, nombre_proyecto, descripcion, fecha_inicio, fecha_fin, habilitado_para_visualizar) VALUES (%s, %s, %s, %s, %s, %s)', datos_proyecto)
    cursor.executemany('INSERT INTO proyecto_empleado (id_proyecto_empleado, id_empleado, id_proyecto, habilitado_para_visualizar) VALUES (%s, %s, %s, %s)', datos_proyecto_empleado)
    cursor.executemany('INSERT INTO registro_tiempo (id_registro_tiempo, fechas, horas_trabajadas, descripcion, id_proyecto_empleado, habilitado_para_visualizar) VALUES (%s, %s, %s, %s, %s, %s)', datos_registro_tiempo)
    cursor.executemany('INSERT INTO tipo_empleado (id_tipo_empleado, tipo_empleado, detalle_empleado, habilitado_para_visualizar) VALUES (%s, %s, %s, %s)', datos_tipo_empleado)

    # Guardar cambios
    cnx.commit()
    print("Datos insertados correctamente en todas las tablas excepto rol y modulos")

except Exception as e:
    print(f"Error al insertar datos: {e}")
    cnx.rollback()

finally:
    cursor.close()
    cnx.close()