
from Nave import nave
class nave_lanzadera(nave):

    def __init__(self, nombre, peso,altura,comustible,potencia,estado,capacidad_carga):
        super().__init__(nombre,peso,altura,comustible,potencia,estado)
        self.capacidad_carga = capacidad_carga

    def crear_nave(self):
        pass

    def encender_nave(self):
        pass

    def apagar_nave(self):
        pass


