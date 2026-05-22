from datetime import datetime

class Reserva:
    def __init__(self, id_reserva, cliente, vehiculo, fecha_inicio, fecha_fin):
        self.id_reserva = id_reserva
        self.cliente = cliente  
        self.vehiculo = vehiculo  
        # Convierte las fechas de texto (YYYY-MM-DD) a objetos datetime para operar con ellas
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        self.fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        self.activa = True

class GestorReservas:
    def __init__(self):
        self.lista_reservas = []

    def validar_disponibilidad(self, vehiculo, f_inicio_str, f_fin_str):
        # 1. Validación de estado base del vehículo
        if vehiculo.estado == "En Mantenimiento":
            return False, "El vehículo está en mantenimiento."
        
        nueva_inicio = datetime.strptime(f_inicio_str, "%Y-%m-%d")
        nueva_fin = datetime.strptime(f_fin_str, "%Y-%m-%d")
        
        # 2. Validación de solapamiento de rangos de fechas
        for res in self.lista_reservas:
            if res.vehiculo.id_vehiculo == vehiculo.id_vehiculo and res.activa:
                # Comprueba si el nuevo rango de fechas se cruza con una reserva existente
                if nueva_inicio <= res.fecha_fin and nueva_fin >= res.fecha_inicio:
                    return False, f"Vehículo no disponible. Ya reservado del {res.fecha_inicio.strftime('%Y-%m-%d')} al {res.fecha_fin.strftime('%Y-%m-%d')}."
        
        return True, "Vehículo disponible."

    def crear_reserva(self, id_reserva, cliente, vehiculo, f_inicio, f_fin):
        disponible, mensaje = self.validar_disponibilidad(vehiculo, f_inicio, f_fin)
        
        if disponible:
            nueva_reserva = Reserva(id_reserva, cliente, vehiculo, f_inicio, f_fin)
            self.lista_reservas.append(nueva_reserva)
            vehiculo.estado = "Alquilado"  # Actualiza el estado del vehículo a Alquilado
            print(f"✅ [ÉXITO] Reserva #{id_reserva} creada para {cliente}.")
            return nueva_reserva
        else:
            print(f"❌ [RECHAZADO] Reserva #{id_reserva}: {mensaje}")
            return None

    def listar_reservas_activas(self):
        print("\n=== LISTADO DE RESERVAS ACTIVAS ===")
        activas = [r for r in self.lista_reservas if r.activa]
        if not activas:
            print("No se encontraron reservas activas.")
        for r in activas:
            # Soporta tanto si el cliente es un objeto con atributo nombre o una cadena de texto
            nombre_cliente = r.cliente.nombre if hasattr(r.cliente, 'nombre') else r.cliente
            print(f"Reserva ID: {r.id_reserva} | Cliente: {nombre_cliente} | Vehículo Placa: {r.vehiculo.id_vehiculo} | Desde: {r.fecha_inicio.strftime('%Y-%m-%d')} Hasta: {r.fecha_fin.strftime('%Y-%m-%d')}")
        print("===================================\n")

    def cancelar_reserva(self, id_reserva):
        for r in self.lista_reservas:
            if r.id_reserva == id_reserva and r.activa:
                r.activa = False
                r.vehiculo.estado = "Disponible"  # Restablece el estado del vehículo a Disponible
                print(f"⚠️ [CANCELADA] Reserva #{id_reserva} cancelada. Vehículo {r.vehiculo.id_vehiculo} ahora está Disponible.")
                return True
        print(f"❌ [ERROR] No se pudo cancelar. No existe reserva activa con ID {id_reserva}.")
        return False