import os
import json
from datetime import datetime

# Archivo para persistir los clientes
DATA_FILE = "clientes.json"

def cargar_clientes():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def guardar_clientes(clientes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=2)

def registrar_cliente():
    print("\n=== Registrar Nuevo Cliente ===")
    nombre = input("Nombre completo: ").strip()
    if not nombre:
        print("❌ El nombre es obligatorio.")
        return
    
    dui = input("DUI (ej: 12345678-9): ").strip()
    if not dui:
        print("❌ El DUI es obligatorio.")
        return
    
    telefono = input("Teléfono (ej: 7123-4567): ").strip()
    
    clientes = cargar_clientes()
    
    # Verificar si el DUI ya existe
    if any(c["dui"] == dui for c in clientes):
        print("❌ Ya existe un cliente con ese DUI.")
        return
    
    nuevo_cliente = {
        "id": len(clientes) + 1,
        "nombre": nombre,
        "dui": dui,
        "telefono": telefono,
        "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    clientes.append(nuevo_cliente)
    guardar_clientes(clientes)
    print("✅ Cliente registrado exitosamente!")

def listar_clientes():
    clientes = cargar_clientes()
    print("\n=== Lista de Clientes ===")
    if not clientes:
        print("No hay clientes registrados aún.")
        return
    
    print(f"{'ID':<4} {'Nombre':<30} {'DUI':<12} {'Teléfono':<15} {'Fecha Registro'}")
    print("-" * 80)
    for c in clientes:
        print(f"{c['id']:<4} {c['nombre']:<30} {c['dui']:<12} {c['telefono']:<15} {c['fecha_registro']}")

def eliminar_cliente():
    listar_clientes()
    clientes = cargar_clientes()
    if not clientes:
        return
    
    try:
        id_eliminar = int(input("\nIngrese el ID del cliente a eliminar: "))
        for i, c in enumerate(clientes):
            if c["id"] == id_eliminar:
                confirm = input(f"¿Eliminar a {c['nombre']} (DUI: {c['dui']})? (s/n): ").lower()
                if confirm == 's':
                    del clientes[i]
                    # Reajustar IDs
                    for idx, cliente in enumerate(clientes):
                        cliente["id"] = idx + 1
                    guardar_clientes(clientes)
                    print("✅ Cliente eliminado correctamente.")
                else:
                    print("Operación cancelada.")
                return
        print("❌ Cliente no encontrado.")
    except ValueError:
        print("❌ Ingrese un número válido.")

def menu_clientes():
    while True:
        print("\n" + "="*40)
        print("          MÓDULO CLIENTES")
        print("="*40)
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Eliminar cliente")
        print("0. Volver al menú principal")
        print("="*40)
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida.")

def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
        print("\n" + "="*50)
        print("          SISTEMA GESTIÓN - MENÚ PRINCIPAL")
        print("="*50)
        print("1. Módulo Clientes")
        print("2. Módulo X (próximamente)")
        print("3. Módulo Y (próximamente)")
        print("0. Salir del sistema")
        print("="*50)
        
        opcion = input("Seleccione un módulo: ").strip()
        
        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            print("\n🔧 Módulo en desarrollo...")
            input("Presione Enter para continuar...")
        elif opcion == "3":
            print("\n🔧 Módulo en desarrollo...")
            input("Presione Enter para continuar...")
        elif opcion == "0":
            print("\n👋 ¡Gracias por usar el sistema!")
            break
        else:
            print("❌ Opción inválida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    print("Iniciando sistema...")
    menu_principal()
