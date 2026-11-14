from Modulos import datos
from Modulos import usuario

CONTRASENIA_ADMIN = "admin123"

def crear_admin_base():
    datos_json = datos.cargar_datos()
    semilla_admin = usuario.crear_diccionario_usuario("0000", "Admin", "Administrador", "555 000111",
                                              "admin@acmeclinic.com", "Cl 185 # 26 – 85", "admin")
    semilla_admin["contrasenia"] = CONTRASENIA_ADMIN
    datos_json["usuarios"].append(semilla_admin)
    datos.guardar_datos(datos_json)

def asegurar_admin():
    if len(usuario.cargar_usuarios()) == 0:
        crear_admin_base()

def registrarUsuarios(no_identificacion, nombre, apellido, no_telefono, email, direccion, rol):
    datos_json = datos.cargar_datos()
    lista_usuarios = datos_json["usuarios"]

    if usuario.existe(no_identificacion):
        print("\nUsuario existente!")
        return

    if usuario.existe_email(email):
        print("\nEmail existente!")
        return

    usuario_creado = usuario.crear_diccionario_usuario(no_identificacion, nombre, apellido, no_telefono, email, direccion, rol)
    lista_usuarios.append(usuario_creado)
    datos.guardar_datos(datos_json)

    print("\nUsuario registrado!")
    print(f"\nContraseña asignada: {usuario_creado['contrasenia']}")