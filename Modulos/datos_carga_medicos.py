import json

carga_medicos = "Data/reporte_carga_medicos.json"

def estructura_carga_medicos(id_medico, nombre_completo, total_diagnosticos, pacientes_distintos, promedio_sintomas_por_consulta, promedio_medicamentos_por_consulta):
    return {
        "id_medico" : id_medico,
        "nombre_completo" : nombre_completo,
        "total_diagnosticos" : total_diagnosticos,
        "pacientes_distintos" : pacientes_distintos,
        "promedio_sintomas_por_consulta" : promedio_sintomas_por_consulta,
        "promedio_medicamentos_por_consulta" : promedio_medicamentos_por_consulta
    }

def estructura_vacia():
    return {
        "cargas_medicos" : []
    }


def guardar_datos(datos: dict):
    try:
        with open(carga_medicos, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print("No se pudo guardar datos")


def cargar_datos():
    try:
        with open(carga_medicos, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return estructura_vacia()

