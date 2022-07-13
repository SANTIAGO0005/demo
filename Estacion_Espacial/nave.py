from abc import ABC,abstractmethod

class Nave:


    def __init__(self,nombre,peso,altura,comustible,potencia,estado):
            self.nombre = nombre
            self.peso = peso
            self.altura = altura
            self.combustible = comustible
            self.potencia = potencia
            self.estado = estado

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor