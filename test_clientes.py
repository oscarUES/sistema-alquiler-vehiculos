import os
import unittest
import clientes


class TestClientes(unittest.TestCase):

    def setUp(self):
        # Usa un archivo de datos temporal para no tocar el clientes.json real
        clientes.DATA_FILE = "clientes_test.json"
        if os.path.exists(clientes.DATA_FILE):
            os.remove(clientes.DATA_FILE)

    def tearDown(self):
        if os.path.exists(clientes.DATA_FILE):
            os.remove(clientes.DATA_FILE)

    def test_guardar_y_cargar(self):
        datos = [{"id": 1, "nombre": "Ana", "dui": "12345678-9",
                  "telefono": "7000-0000", "fecha_registro": "2026-01-01 00:00:00"}]
        clientes.guardar_clientes(datos)
        cargados = clientes.cargar_clientes()
        self.assertEqual(len(cargados), 1)
        self.assertEqual(cargados[0]["dui"], "12345678-9")

    def test_cargar_sin_archivo_devuelve_lista_vacia(self):
        self.assertEqual(clientes.cargar_clientes(), [])


if __name__ == "__main__":
    unittest.main()
