"""
Sistema de Alquiler de Vehiculos - LDP GT04
Punto de entrada: integra los modulos de Clientes, Vehiculos y Reservas.

El modulo de Reservas (Danilo) trabaja con objetos, mientras que Vehiculos y
Clientes usan diccionarios. VehiculoAdapter hace de puente: expone .estado e
.id_vehiculo que el GestorReservas espera, pero escribe los cambios sobre el
diccionario real del vehiculo (asi el estado "Alquilado" se refleja en el
listado de Vehiculos).
"""

import clientes
import vehiculos
from modulo_reservas import GestorReservas


class VehiculoAdapter:
    """Puente entre un vehiculo (diccionario) y el GestorReservas (objetos)."""

    def __init__(self, vdict):
        self._v = vdict

    @property
    def id_vehiculo(self):
        return self._v["placa"]

    @property
    def estado(self):
        return self._v["estado"]

    @estado.setter
    def estado(self, valor):
        self._v["estado"] = valor


def _seleccionar_cliente():
    clientes.listar_clientes()
    lista = clientes.cargar_clientes()
    if not lista:
        return None
    entrada = input("\nID del cliente: ").strip()
    if not entrada.isdigit():
        print("Error: ingrese un ID valido.")
        return None
    for c in lista:
        if c["id"] == int(entrada):
            return c
    print("Error: cliente no encontrado.")
    return None


def _seleccionar_vehiculo():
    vehiculos.listar_vehiculos()
    if len(vehiculos.vehiculos) == 0:
        return None
    placa = input("\nPlaca del vehiculo: ").strip().upper()
    v = vehiculos.buscar_vehiculo_por_placa(placa)
    if v is None:
        print("Error: vehiculo no encontrado.")
    return v


def menu_reservas(gestor, contador):
    while True:
        print("\n===== GESTION DE RESERVAS =====")
        print("1. Crear reserva")
        print("2. Listar reservas activas")
        print("3. Cancelar reserva")
        print("0. Volver al menu principal")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            cliente = _seleccionar_cliente()
            if cliente is None:
                continue
            vdict = _seleccionar_vehiculo()
            if vdict is None:
                continue
            f_inicio = input("Fecha inicio (YYYY-MM-DD): ").strip()
            f_fin = input("Fecha fin (YYYY-MM-DD): ").strip()
            try:
                contador[0] += 1
                resultado = gestor.crear_reserva(
                    contador[0], cliente["nombre"],
                    VehiculoAdapter(vdict), f_inicio, f_fin
                )
                if resultado is None:
                    contador[0] -= 1  # no se creo, libera el ID
            except ValueError:
                print("Error: formato de fecha invalido (use YYYY-MM-DD).")
                contador[0] -= 1
        elif opcion == "2":
            gestor.listar_reservas_activas()
        elif opcion == "3":
            gestor.listar_reservas_activas()
            entrada = input("ID de la reserva a cancelar: ").strip()
            if entrada.isdigit():
                gestor.cancelar_reserva(int(entrada))
            else:
                print("Error: ingrese un ID valido.")
        elif opcion == "0":
            break
        else:
            print("Opcion no valida.")


def menu_principal():
    gestor = GestorReservas()
    contador = [0]  # ID incremental de reservas (lista para mutarlo dentro del menu)
    while True:
        print("\n" + "=" * 50)
        print("        SISTEMA DE ALQUILER DE VEHICULOS")
        print("=" * 50)
        print("1. Clientes")
        print("2. Vehiculos")
        print("3. Reservas")
        print("0. Salir")
        print("=" * 50)
        opcion = input("Seleccione un modulo: ").strip()

        if opcion == "1":
            clientes.menu_clientes()
        elif opcion == "2":
            vehiculos.menu_vehiculos()
        elif opcion == "3":
            menu_reservas(gestor, contador)
        elif opcion == "0":
            print("\nGracias por usar el sistema!")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu_principal()
