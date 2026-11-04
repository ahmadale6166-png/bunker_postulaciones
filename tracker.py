import json
import os
from datetime import datetime

FILE_NAME = "postulaciones.json"

def cargar_datos():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_datos(datos):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def registrar_postulacion():
    print("\n--- 📝 REGISTRAR NUEVA POSTULACIÓN ---")
    empresa = input("Empresa: ").strip()
    puesto = input("Puesto / Vacante: ").strip()
    plataforma = input("Plataforma (ej: Get on Board, Mail, Bumeran): ").strip()
    estado = input("Estado (ej: Postulado, En revisión, Entrevista): ").strip() or "Postulado"
    
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    nueva = {
        "fecha": fecha,
        "empresa": empresa,
        "puesto": puesto,
        "plataforma": plataforma,
        "estado": estado
    }
    
    datos = cargar_datos()
    datos.append(nueva)
    guardar_datos(datos)
    print(f"\n✅ Postulación a '{empresa}' registrada con éxito.")

def listar_postulaciones():
    datos = cargar_datos()
    print("\n--- 📋 HISTORIAL DE POSTULACIONES ---")
    if not datos:
        print("No hay postulaciones registradas aún.")
        return
    for i, p in enumerate(datos, 1):
        print(f"{i}. [{p['fecha']}] {p['empresa']} - {p['puesto']} ({p['plataforma']}) | Estado: {p['estado']}")

def main():
    while True:
        print("\n=== 🎯 TRACKER DE POSTULACIONES (BÚNKER DIGITAL) ===")
        print("1. Registrar nueva postulación")
        print("2. Ver historial de postulaciones")
        print("3. Salir")
        opcion = input("Seleccioná una opción (1-3): ").strip()
        
        if opcion == "1":
            registrar_postulacion()
        elif opcion == "2":
            listar_postulaciones()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
