from Modulos import datos
from Modulos import paciente
from Modulos import validaciones

ESTADOS_CIVILES = ("soltero", "casado", "viudo", "divorciado", "union libre")

def registrar_paciente(no_identificacion, nombres, apellidos, no_telefono, email, direccion, genero, estado_civil):
    datos_json = datos.cargar_datos()
    lista_pacientes = datos_json["pacientes"]

    if paciente.existe(no_identificacion):
        print("\nEl paciente ya existe!")
        return
    paciente_creado = paciente.crear_diccionario_paciente(no_identificacion, nombres, apellidos, no_telefono, email, direccion, genero, estado_civil)
    lista_pacientes.append(paciente_creado)
    datos.guardar_datos(datos_json)

    print("\nPaciente registrado correctamente!")

def solicitar_paciente(sesion):
    print("\n--- Registro de nuevo paciente ---")
    no_identificacion = validaciones.pedir_identificacion("No. identificación")
    nombres = validaciones.pedir_texto("Nombres")
    apellidos = validaciones.pedir_texto("Apellidos")
    no_telefono = validaciones.pedir_telefono("No. de teléfono")
    email = validaciones.pedir_email("E-mail")
    direccion = validaciones.pedir_texto("Dirección")
    genero = validaciones.pedir_texto("Género")
    estado_civil = validaciones.pedir_opcion("Estado civil", ESTADOS_CIVILES)

    registrar_paciente(no_identificacion, nombres, apellidos, no_telefono, email, direccion, genero, estado_civil)
