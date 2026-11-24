from Modulos import login
from Modulos import registro_paciente
from Modulos import registro_diagnostico
from Modulos import historia_clinica
from Modulos import reporte_carga_medicos

OPCIONES_ADMIN = {
    "1": ("Registrar usuario", login.sign_up),
    "2": ("Consultar historia clínica", historia_clinica.consultar_historia),
    # "3": ("Registrar paciente", registro_paciente.solicitar_paciente),  # Desactivado: por ahora el admin no registra pacientes
}

OPCIONES_MEDICO = {
    "1": ("Registrar paciente", registro_paciente.solicitar_paciente),
    "2": ("Registrar diagnóstico", registro_diagnostico.solicitar_diagnostico),
    "3": ("Consultar historia clínica", historia_clinica.consultar_historia),
    "4": ("Reporte carga médicos", reporte_carga_medicos.reporte)
}

OPCIONES_POR_ROL = {
    "admin": OPCIONES_ADMIN,
    "medico": OPCIONES_MEDICO,
}

def mostrar_menu(opciones):
    print("\n--- Menú principal ---")
    for clave in opciones:
        print(f"{clave}. {opciones[clave][0]}")
    print("0. Cerrar sesión")

def ejecutar(sesion):
    opciones = OPCIONES_POR_ROL[sesion["rol"]]
    while True:
        mostrar_menu(opciones)
        opcion = input("Opción: ").strip()
        if opcion == "0":
            print("\nSesión cerrada. ¡Hasta pronto!")
            break
        elif opcion in opciones:
            opciones[opcion][1](sesion)
        else:
            print("\nOpción no válida.")
