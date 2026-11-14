DOMINIO_CORPORATIVO = "@acmeclinic.com"

def pedir_texto(etiqueta):
    while True:
        valor = input(f"{etiqueta}: ").strip()
        if valor != "":
            return valor
        print("\nEste campo no puede estar vacío.")

def pedir_identificacion(etiqueta):
    while True:
        valor = pedir_texto(etiqueta)
        if valor.isdigit():
            return valor
        print("\nDebe contener solo números.")

def pedir_telefono(etiqueta):
    while True:
        valor = pedir_texto(etiqueta)
        if valor.replace(" ", "").isdigit():
            return valor
        print("\nDebe contener solo números (se permiten espacios).")

def email_valido(valor, dominio):
    if " " in valor or valor.count("@") != 1:
        return False
    usuario, servidor = valor.split("@")
    return usuario != "" and "." in servidor and not servidor.startswith(".") and not servidor.endswith(".") and valor.endswith(dominio)

def pedir_email(etiqueta, dominio=""):
    while True:
        valor = pedir_texto(etiqueta).lower()
        if email_valido(valor, dominio):
            return valor
        if dominio == "":
            print("\nE-mail no válido. Ejemplo: nombre@correo.com")
        else:
            print(f"\nDebe ser un e-mail corporativo: nombre{dominio}")

def pedir_opcion(etiqueta, opciones):
    while True:
        valor = input(f"{etiqueta} ({' / '.join(opciones)}): ").strip().lower()
        if valor in opciones:
            return valor
        print(f"\nOpción no válida, elige: {', '.join(opciones)}.")

def pedir_entero(etiqueta):
    while True:
        valor = pedir_texto(etiqueta)
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("\nDebe ingresar un número entero mayor que 0.")
