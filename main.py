from Modulos import registro_usuario
from Modulos import login
from Modulos import menu

def iniciar_programa():
    registro_usuario.asegurar_admin()
    while True:
        sesion = login.iniciar_sesion()
        if sesion is None:
            print("\nDemasiados intentos fallidos. Programa terminado.")
            return
        menu.ejecutar(sesion)

if __name__ == '__main__':
    iniciar_programa()
