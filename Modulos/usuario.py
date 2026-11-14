import random
from Modulos import datos

def cargar_usuarios():
    return datos.cargar_datos()["usuarios"]

def buscar(no_identificacion):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["no. identificacion"] == no_identificacion:
            return usuario
    return None

def existe(no_identificacion):
    return buscar(no_identificacion) is not None

def existe_medico(no_identificacion):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["no. identificacion"] == no_identificacion and usuario["rol"] == "medico":
            return True
    return False

def existe_email(email):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["e-mail"] == email:
            return True
    return False

def buscar_por_credenciales(email, contrasenia):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["e-mail"] == email and usuario["contrasenia"] == contrasenia:
            return usuario
    return None

def crear_diccionario_usuario(no_identificacion, nombre, apellido, no_telefono, email, direccion, rol):
    usuario = {
        "no. identificacion": no_identificacion,
        "nombre": nombre,
        "apellido": apellido,
        "no. de telefono": no_telefono,
        "e-mail": email,
        "direccion": direccion,
        "contrasenia": generar_contrasenia(),
        "rol": rol
    }
    return usuario

def generar_contrasenia():
    contrasenia = ""
    for i in range(8):
        contrasenia += str(random.randint(0, 9))
    return contrasenia