from Modulos import datos
from Modulos import paciente
from Modulos import usuario

def diagnosticos_del_paciente(id_paciente):
    lista_diagnosticos = []
    for diagnostico in datos.cargar_datos()["diagnosticos"]:
        if diagnostico["id_paciente"] == id_paciente:
            lista_diagnosticos.append(diagnostico)
    return lista_diagnosticos

def nombre_medico(id_medico):
    medico = usuario.buscar(id_medico)
    if medico is None:
        return id_medico
    return f"{medico['nombre']} {medico['apellido']}"

def mostrar_encabezado(datos_paciente):
    print("\n===== DATOS DEL PACIENTE =====")
    for clave in datos_paciente:
        etiqueta = clave.replace("_", " ").capitalize()
        print(f"{etiqueta}: {datos_paciente[clave]}")

def mostrar_medicamentos(prescripcion):
    print("  Medicamentos:")
    if len(prescripcion) == 0:
        print("    Ninguno")
    for medicamento in prescripcion:
        detalle = prescripcion[medicamento]
        print(f"    - {medicamento}: {detalle['cantidad']} unidades, {detalle['dosis']} veces al día, {detalle['dias']} días")

def mostrar_consulta(numero, diagnostico):
    print(f"\nConsulta {numero}")
    print(f"  Fecha: {diagnostico['fecha']}")
    print(f"  Médico: {nombre_medico(diagnostico['id_medico'])}")
    print(f"  Síntomas: {', '.join(diagnostico['sintomas'])}")
    print(f"  Diagnóstico: {diagnostico['diagnostico']}")
    mostrar_medicamentos(diagnostico["prescripcion_medica"])

def mostrar_consultas(lista_diagnosticos):
    print("\n===== CONSULTAS =====")
    if len(lista_diagnosticos) == 0:
        print("\nSin consultas registradas.")

    for i in range(len(lista_diagnosticos) - 1, -1, -1):
        mostrar_consulta(i + 1, lista_diagnosticos[i])

def consultar_historia(sesion):
    print("\n--- Historia clínica ---")
    id_paciente = input("No. identificación del paciente: ").strip()
    datos_paciente = paciente.buscar(id_paciente)
    if datos_paciente is None:
        print("\nEl paciente no está registrado.")
        return
    mostrar_encabezado(datos_paciente)
    mostrar_consultas(diagnosticos_del_paciente(id_paciente))
    input("\n--- Pressione ENTER para continuar ---")
