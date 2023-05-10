# desviacion estandar
# mediano
# manejo exepciones
import math


class Statistics:

    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        self.lista_datos = []

    def meter_datos(self):
        for dato in range(self.inicio, self.final + 1):
            self.lista_datos.append(dato)
        return self.lista_datos

    def size(self):
        return len(self.lista_datos)

    def is_empty(self):
        if not self.size():
            return True

    def ordenar_datos(self):
        return sorted(self.lista_datos)

    def calcular_valor_mediano(self):
        if self.is_empty():
            raise Exception("no given data")

        else:
            if self.size() % 2 == 2:
                indice = (self.size()/2)
                valores = self.lista_datos.index(indice) + (self.lista_datos.index(indice)+1)
                valores = valores/2
                return valores
            else:
                indice = math.ceil(self.size()/2)
                return self.lista_datos.index(indice)


