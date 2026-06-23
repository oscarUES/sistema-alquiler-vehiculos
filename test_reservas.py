import unittest
from modulo_reservas import GestorReservas

# Simulación de la estructura de la clase Vehículo para pruebas locales
class VehiculoSimulado:
    def __init__(self, id_vehiculo, estado="Disponible"):
        self.id_vehiculo = id_vehiculo
        self.estado = estado

def correr_pruebas_modulo():
    print("==================================================")
    print("  DEMO FUNCIONAL: MÓDULO RESERVAS                ")
    print("==================================================\n")
    
    gestor = GestorReservas()
    
    # Creación de objetos simulados para el entorno de prueba
    carro_disponible = VehiculoSimulado("P123-456", "Disponible")
    carro_mantenimiento = VehiculoSimulado("P789-012", "En Mantenimiento")
    
    # Ejecución de casos de prueba para validar la lógica de negocio
    print("👉 CASO 1: Intentar reservar un vehículo disponible...")
    gestor.crear_reserva(1, "Cliente Alfa", carro_disponible, "2026-06-01", "2026-06-05")
    
    print("\n👉 CASO 2: Intentar reservar el mismo vehículo en fechas que se solapan...")
    gestor.crear_reserva(2, "Cliente Beta", carro_disponible, "2026-06-03", "2026-06-08")
    
    print("\n👉 CASO 3: Intentar reservar un vehículo que se encuentra en mantenimiento...")
    gestor.crear_reserva(3, "Cliente Gamma", carro_mantenimiento, "2026-06-01", "2026-06-05")
    
    # Visualización del estado actual de las reservas en el sistema
    gestor.listar_reservas_activas()
    
    print("👉 CASO 4: Cancelar reserva activa para liberar el vehículo...")
    gestor.cancelar_reserva(1)
    
    # Verificación de que el estado del objeto cambió correctamente tras la cancelación
    print(f"Estado actual del vehículo P123-456: {carro_disponible.estado}")
    
    # Confirmación de que la lista de reservas activas se actualizó
    gestor.listar_reservas_activas()

class TestGestorReservas(unittest.TestCase):
    """Pruebas unitarias del GestorReservas (no modifica modulo_reservas.py)."""

    def setUp(self):
        self.gestor = GestorReservas()
        self.vehiculo = VehiculoSimulado("P123-456", "Disponible")

    def test_crear_reserva_marca_vehiculo_alquilado(self):
        self.gestor.crear_reserva(1, "Cliente Alfa", self.vehiculo,
                                  "2026-06-01", "2026-06-05")
        self.assertEqual(self.vehiculo.estado, "Alquilado")

    def test_validar_disponibilidad_rechaza_solapamiento(self):
        self.gestor.crear_reserva(1, "Cliente Alfa", self.vehiculo,
                                  "2026-06-01", "2026-06-05")
        disponible, _ = self.gestor.validar_disponibilidad(
            self.vehiculo, "2026-06-03", "2026-06-08")
        self.assertFalse(disponible)


if __name__ == "__main__":
    correr_pruebas_modulo()