"""
Módulo: Gestión de Vehículos
Sistema de Alquiler de Vehículos - LDP GT04
Autor: Oscar García
"""

# Lista que almacena todos los vehículos registrados
vehiculos = []

# Estado válidos para un vehículo
ESTADOS = ["Disponible", "Alquilado", "En Mantenimiento"]


def mostrar_menu_vehiculos():
    print("\n===== GESTIÓN DE VEHÍCULOS =====")
    print("1. Registrar vehículo")
    print("2. Listar vehículos")
    print("3. Actualizar estado de vehículo")
    print("4. Eliminar vehículo")
    print("0. Volver al menú principal")
    print("================================")


def generar_id():
    if len(vehiculos) == 0:
        return 1
    ultimo_id = vehiculos[-1]["id"]
    return ultimo_id + 1


def buscar_vehiculo_por_placa(placa):
    for v in vehiculos:
        if v["placa"].upper() == placa.upper():
            return v
    return None


def registrar_vehiculo():
    print("\n--- Registrar nuevo vehículo ---")

    placa = input("Placa: ").strip().upper()
    if placa == "":
        print("Error: La placa no puede estar vacía.")
        return

    if buscar_vehiculo_por_placa(placa) is not None:
        print(f"Error: Ya existe un vehículo con la placa {placa}.")
        return

    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    while True:
        año_str = input("Año: ").strip()
        if año_str.isdigit() and 1900 <= int(año_str) <= 2026:
            año = int(año_str)
            break
        print("Error: Ingrese un año válido (1900 - 2026).")

    vehiculo = {
        "id": generar_id(),
        "placa": placa,
        "marca": marca,
        "modelo": modelo,
        "año": año,
        "estado": "Disponible"
    }

    vehiculos.append(vehiculo)
    print(f"\nVehículo registrado con éxito. ID asignado: {vehiculo['id']}")


def listar_vehiculos():
    print("\n--- Lista de vehículos ---")

    if len(vehiculos) == 0:
        print("No hay vehículos registrados.")
        return

    print(f"{'ID':<5} {'Placa':<10} {'Marca':<12} {'Modelo':<15} {'Año':<6} {'Estado'}")
    print("-" * 65)

    for v in vehiculos:
        print(f"{v['id']:<5} {v['placa']:<10} {v['marca']:<12} {v['modelo']:<15} {v['año']:<6} {v['estado']}")


def actualizar_estado_vehiculo():
    print("\n--- Actualizar estado de vehículo ---")
    listar_vehiculos()

    if len(vehiculos) == 0:
        return

    placa = input("\nIngrese la placa del vehículo: ").strip().upper()
    vehiculo = buscar_vehiculo_por_placa(placa)

    if vehiculo is None:
        print(f"Error: No se encontró ningún vehículo con placa {placa}.")
        return

    print(f"\nVehículo: {vehiculo['marca']} {vehiculo['modelo']} ({vehiculo['placa']})")
    print(f"Estado actual: {vehiculo['estado']}")
    print("\nEstados disponibles:")

    for i, estado in enumerate(ESTADOS):
        print(f"{i + 1}. {estado}")

    while True:
        opcion_str = input("Seleccione nuevo estado: ").strip()
        if opcion_str.isdigit() and 1 <= int(opcion_str) <= len(ESTADOS):
            nuevo_estado = ESTADOS[int(opcion_str) - 1]
            break
        print("Error: Opción no válida.")

    if nuevo_estado == vehiculo["estado"]:
        print("El vehículo ya tiene ese estado.")
        return

    vehiculo["estado"] = nuevo_estado
    print(f"Estado actualizado a: {nuevo_estado}")


def eliminar_vehiculo():
    print("\n--- Eliminar vehículo ---")
    listar_vehiculos()

    if len(vehiculos) == 0:
        return

    placa = input("\nIngrese la placa del vehículo a eliminar: ").strip().upper()
    vehiculo = buscar_vehiculo_por_placa(placa)

    if vehiculo is None:
        print(f"Error: No se encontró ningún vehículo con placa {placa}.")
        return

    if vehiculo["estado"] == "Alquilado":
        print("Error: No se puede eliminar un vehículo que está alquilado.")
        return

    confirmacion = input(f"¿Está seguro de eliminar el vehículo {placa}? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        return

    vehiculos.remove(vehiculo)
    print(f"Vehículo {placa} eliminado con éxito.")


def menu_vehiculos():
    while True:
        mostrar_menu_vehiculos()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_vehiculo()
        elif opcion == "2":
            listar_vehiculos()
        elif opcion == "3":
            actualizar_estado_vehiculo()
        elif opcion == "4":
            eliminar_vehiculo()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
