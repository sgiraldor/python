from typing import Any


class Analizadoreventos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_eventos(self,) -> [str, Any]:
        eventos_por_tipo = {}
        eventos_por_servidor = {}
        evntos_registrados = {}
        total_eventos = 0
        eventos = {}

        with open(self.nombre_archivo, 'r') as archivo:
            for i in archivo:
                if i.startswith('fecha'):
                    total_eventos += 1
                    fecha = i.strip().split(' ')[1]
                    hora = archivo.readline().strip().split(' ')[1]
                    servidor = archivo.readline().strip().split(' ')[1]
                    tipo_evento = archivo.readline().strip().split(' ')[2]
                    descripcion = archivo.readline().strip().split(' ')[1:]
                    descripcion = ' '.join(descripcion)

                    # Estadisticas actualizadas
                    eventos_por_tipo[tipo_evento] = eventos_por_tipo.get(tipo_evento, 0) + 1
                    eventos_por_servidor[servidor] = eventos_por_servidor.get(servidor, 0) + 1
        eventos['total_eventos'] = total_eventos
        eventos['eventos_por_tipo'] = eventos_por_tipo
        eventos['eventos_por_servidor'] = eventos_por_servidor

        return eventos
