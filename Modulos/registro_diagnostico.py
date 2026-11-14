from Modulos import datos
from Modulos.usuario import existe_medico
from Modulos import paciente
from Modulos import validaciones

def crear_diccionario_diagnostico(fecha, lista_sintomas:list, diagnostico, prescripcion_medica:dict, id_paciente, id_medico):
    dict_diagnostico = {
        "fecha" : fecha,
        "id_paciente": id_paciente,
        "id_medico": id_medico,
        "sintomas":lista_sintomas,
        "diagnostico":diagnostico,
        "prescripcion_medica":prescripcion_medica
    }
    return dict_diagnostico

def determinar_dato_faltante(paciente_existe, medico_existe):
    if not paciente_existe and not medico_existe:
        return "paciente y médico"
    elif not paciente_existe:
        return "paciente"
    else:
        return "médico"

def registrar_diagnostico(fecha, lista_sintomas:list, diagnostico, prescripcion_medica:dict, id_paciente, id_medico):
    datos_json = datos.cargar_datos()
    lista_diagnosticos = datos_json["diagnosticos"]

    paciente_existe = paciente.existe(id_paciente)
    medico_existe = existe_medico(id_medico)

    if paciente_existe and medico_existe:
        registro = crear_diccionario_diagnostico(fecha, lista_sintomas,diagnostico, prescripcion_medica, id_paciente, id_medico)
        lista_diagnosticos.append(registro)
        datos.guardar_datos(datos_json)

        print("\nDiagnostico registrado correctamente!")
    else:
        print(f"\nDebe estar registrado {determinar_dato_faltante(paciente_existe, medico_existe)}!")

DIAS_POR_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def dias_del_mes(mes, anio):
    if mes == 2 and es_bisiesto(anio):
        return 29
    return DIAS_POR_MES[mes - 1]

def fecha_valida(texto):
    partes = texto.split("/")
    if len(partes) != 3:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
    dia = int(partes[0])
    mes = int(partes[1])
    anio = int(partes[2])
    if len(partes[2]) != 4 or not 1 <= mes <= 12:
        return False
    return 1 <= dia <= dias_del_mes(mes, anio)

def pedir_fecha():
    while True:
        fecha = input("Fecha del diagnóstico (dd/mm/aaaa): ").strip()
        if fecha_valida(fecha):
            return fecha
        print("\nFecha inválida. Use el formato dd/mm/aaaa, por ejemplo 13/11/2026.")

def pedir_sintomas():
    texto = input("Síntomas (separados por coma): ")
    lista_sintomas = []
    for sintoma in texto.split(","):
        sintoma = sintoma.strip()
        if sintoma != "":
            lista_sintomas.append(sintoma)
    return lista_sintomas

def pedir_prescripcion():
    prescripcion = {}
    agregar = input("\n¿Agregar un medicamento? (s/n): ").strip().lower()
    while agregar == "s":
        medicamento = validaciones.pedir_texto("Medicamento")
        prescripcion[medicamento] = {
            "cantidad": validaciones.pedir_entero("Cantidad"),
            "dosis": validaciones.pedir_entero("Dosis (veces al día)"),
            "dias": validaciones.pedir_entero("Días de tratamiento"),
        }
        agregar = input("\n¿Agregar otro medicamento? (s/n): ").strip().lower()
    return prescripcion

def solicitar_diagnostico(sesion):
    print("\n--- Registro de nuevo diagnóstico ---")
    id_paciente = validaciones.pedir_identificacion("No. identificación del paciente")
    fecha = pedir_fecha()
    lista_sintomas = pedir_sintomas()
    diagnostico = validaciones.pedir_texto("Diagnóstico")
    prescripcion_medica = pedir_prescripcion()

    registrar_diagnostico(fecha, lista_sintomas, diagnostico, prescripcion_medica, id_paciente, sesion["no. identificacion"])