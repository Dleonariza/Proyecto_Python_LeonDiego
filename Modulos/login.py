from Modulos import usuario
from Modulos import registro_usuario
from Modulos import validaciones

ROLES = ("admin", "medico")
INTENTOS = 3

def iniciar_sesion():
    print("\n--- INCIO DE SESION ---")
    for intento in range(INTENTOS):
        email = input("\nE-mail: ").strip().lower()
        contrasenia = input("Contraseña: ").strip()

        usuario_logueado = usuario.buscar_por_credenciales(email, contrasenia)
        if usuario_logueado is not None:
            print(f"\nBienvenido, {usuario_logueado['nombre']} {usuario_logueado['apellido']}!")
            return usuario_logueado

        print(f"\nCredenciales incorrectas. Intentos restantes: {INTENTOS - intento - 1}")
    return None

def sign_up(sesion):
    if sesion is None:
        print("\nDebe iniciar sesión para registrar usuarios.")
        return
    if sesion["rol"] != "admin":
        print("\nSolo un administrador puede registrar usuarios.")
        return

    print("\n--- Registro de nuevo usuario ---")
    no_identificacion = validaciones.pedir_identificacion("No. identificación")
    nombre = validaciones.pedir_texto("Nombre")
    apellido = validaciones.pedir_texto("Apellido")
    no_telefono = validaciones.pedir_telefono("No. de teléfono")
    email = validaciones.pedir_email("E-mail", validaciones.DOMINIO_CORPORATIVO)
    direccion = validaciones.pedir_texto("Dirección")
    rol = validaciones.pedir_opcion("Rol", ROLES)

    registro_usuario.registrarUsuarios(no_identificacion, nombre, apellido, no_telefono, email, direccion, rol)
