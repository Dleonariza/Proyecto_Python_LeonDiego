import json

nom_arch = "Data/persistencia_de_datos.json"

def estructura_vacia():
    return {
        "usuarios": [],
        "pacientes": [],
        "diagnosticos": [],
        "historias": []
    }

def guardar_datos(datos: dict):
    try:
        with open(nom_arch, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print("No se pudo guardar datos")


def cargar_datos():
    try:
        with open(nom_arch, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return estructura_vacia()
