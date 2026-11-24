import datos
import datos_carga_medicos

def diagnosticos():
    datos_json = datos.cargar_datos()
    lista_diagnosticos = datos_json["diagnosticos"]
    return lista_diagnosticos

def num_total_diagnosticos(no_identificacion):
    lista_diagnosticos = diagnosticos()
    cont = 0

    for diagnostico in lista_diagnosticos:
        if diagnostico["id_medico"] == no_identificacion:
            cont += 1

    return cont

def num_pacientes_distintos(no_identificacion):
    lista_diagnosticos = diagnosticos()

    lista_usuarios_distintos = []
    cont = 0
    for i, diagnostico in enumerate(lista_diagnosticos):
        j = i + 1
        for j, diagnostico in lista_diagnosticos:
            if diagnostico[i] == diagnostico[j] and diagnostico["id_medico"] == no_identificacion:
                cont += 1
        if cont == 0:
            lista_usuarios_distintos.append(diagnostico[i])
        else:
            cont = 0

    return len(lista_usuarios_distintos)

def prom_sintomas_por_consulta(no_identificacion):
    lista_diagnosticos = diagnosticos()

    suma = 0
    cont = 0
    prom = 0.0

    for diagnostico in lista_diagnosticos:
        if diagnostico["id_medico"] == no_identificacion:
            suma += len(diagnostico["sintomas"])
            cont += 1
    prom = suma / cont

    return prom

def prom_medicamentos_por_consulta(no_idenficacion):
    lista_diagnosticos = diagnosticos()

    sum_medicamentos = 0
    cont = 0
    prom = 0.0

    for diagnostico in lista_diagnosticos:
        if diagnostico["id_medico"] == no_idenficacion:
            sum_medicamentos += len(diagnostico["prescripcion_medica"])
            cont += 1
    prom = sum_medicamentos / cont
    return prom

def reporte(session):
    datos_json = datos.cargar_datos()
    lista_usuarios = datos_json["usuarios"]

    for usuario in lista_usuarios:
        if usuario["rol"] == "medico":
            id_medico = usuario["no. identificacion"]
            nombre_completo = usuario["nombre"] + " " + usuario["apellido"]
            total_diagnosticos = num_total_diagnosticos(id_medico)
            pacientes_distintos = num_pacientes_distintos(id_medico)
            promedio_sintomas_por_consulta = prom_sintomas_por_consulta(id_medico)
            promedio_medicamentos_por_consulta = prom_medicamentos_por_consulta(id_medico)

            dict_reporte = datos_carga_medicos.estructura_carga_medicos(id_medico, nombre_completo, total_diagnosticos, pacientes_distintos, promedio_sintomas_por_consulta, promedio_medicamentos_por_consulta)
            datos_carga_medicos.guardar_datos(dict_reporte)
