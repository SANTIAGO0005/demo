from tipo_nave import Tipo_nave
from nave import Nave

class Nave_Tripulada(Nave,Tipo_nave):

    def __init__(self,capacidad_personas,tipo_tarea):
        self.capacidad_personas = capacidad_personas
        self.tipo_tarea = tipo_tarea


    def crear_nave(self):
        pass


    def encender_nave(self):
        pass


    def apagar_nave(self):
        pass

