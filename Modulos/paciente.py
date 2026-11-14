from Modulos import datos

def crear_diccionario_paciente(no_identificacion, nombres, apellidos, no_telefono, email, direccion, genero, estado_civil):
    paciente = {
        "no. identificacion": no_identificacion,
        "nombre": nombres,
        "apellido": apellidos,
        "no. de telefono": no_telefono,
        "e-mail": email,
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil
    }
    return paciente

def buscar(no_identificacion):
    pacientes = cargar_pacientes()
    for paciente in pacientes:
        if paciente["no. identificacion"] == no_identificacion:
            return paciente
    return None

def existe(no_identificacion):
    return buscar(no_identificacion) is not None

def cargar_pacientes():
    return datos.cargar_datos()["pacientes"]