# Sistema de Alquiler de Vehículos

Aplicación de línea de comandos (CLI) en Python para gestionar clientes,
vehículos y reservas de una empresa de alquiler. Integra tres módulos
independientes desarrollados en equipo: Clientes, Vehículos y Reservas,
con un adaptador que mantiene sincronizado el estado del vehículo entre
el gestor de reservas y el inventario.

## Integrantes

| Integrante | Módulo |
|---|---|
| Oscar García | Vehículos (`vehiculos.py`), integración (`main.py`) |
| Alexander Madrid | Clientes (`clientes.py`) |
| Danilo González | Reservas (`modulo_reservas.py`) |

## Requisitos

- Python 3.10 o superior
- Sin librerías externas (solo módulos de la biblioteca estándar)

## Cómo ejecutar

```bash
python3 main.py
```

## Ejemplo de flujo

```
1. Módulo Clientes → Registrar cliente
   Nombre: María López  |  DUI: 04321234-5  |  Teléfono: 7000-1111

2. Módulo Vehículos → Registrar vehículo
   Placa: P123-456  |  Marca: Toyota  |  Modelo: Corolla  |  Año: 2023

3. Módulo Reservas → Crear reserva
   Cliente: María López  |  Vehículo: P123-456
   Fecha inicio: 2026-07-01  |  Fecha fin: 2026-07-05
   → ✅ Reserva #1 creada
   → El vehículo P123-456 queda en estado "Alquilado"
   → Al cancelar la reserva, vuelve a "Disponible"
```

## Pruebas unitarias

```bash
python3 -m unittest test_vehiculos test_clientes test_reservas -v
```

Las suites `test_vehiculos` y `test_clientes` usan `unittest.TestCase`.
`test_reservas` es una demo funcional ejecutable directamente:

```bash
python3 test_reservas.py
```

## Estructura del proyecto

```
sistema-alquiler-vehiculos/
├── main.py               # Punto de entrada: integra los tres módulos
├── clientes.py           # Módulo Clientes: registro, listado, eliminación
├── vehiculos.py          # Módulo Vehículos: CRUD y control de estado
├── modulo_reservas.py    # Módulo Reservas: creación, validación, cancelación
├── test_vehiculos.py     # Pruebas unitarias — Vehículos (Oscar)
├── test_clientes.py      # Pruebas unitarias — Clientes (Alexander)
├── test_reservas.py      # Demo funcional — Reservas (Danilo)
└── README.md
```
