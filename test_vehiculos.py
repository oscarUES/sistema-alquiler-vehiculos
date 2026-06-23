import unittest
import vehiculos


class TestVehiculos(unittest.TestCase):

    def setUp(self):
        # Aísla cada prueba con una lista limpia de vehículos
        vehiculos.vehiculos.clear()
        vehiculos.vehiculos.append({
            "id": 1, "placa": "ABC123", "marca": "Toyota",
            "modelo": "Corolla", "año": 2021, "estado": "Disponible"
        })

    def test_buscar_por_placa_existente(self):
        v = vehiculos.buscar_vehiculo_por_placa("abc123")
        self.assertIsNotNone(v)
        self.assertEqual(v["marca"], "Toyota")

    def test_buscar_por_placa_inexistente(self):
        self.assertIsNone(vehiculos.buscar_vehiculo_por_placa("XYZ999"))

    def test_generar_id_incremental(self):
        vehiculos.vehiculos.append({
            "id": vehiculos.generar_id(), "placa": "DEF456", "marca": "Kia",
            "modelo": "Rio", "año": 2022, "estado": "Disponible"
        })
        self.assertEqual(vehiculos.vehiculos[-1]["id"], 2)


if __name__ == "__main__":
    unittest.main()
