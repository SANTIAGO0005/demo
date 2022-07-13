from tipo_nave import Tipo_nave
from nave import Nave

class nave_robotica(Nave, Tipo_nave):

    def __init__(self, cantidad_motores,objetivo_estudio):
            self.cantidad_motores = cantidad_motores
            self.objetivo_estudio = objetivo_estudio

    def crear_nave(self):
        pass

    def encender_nave(self):
        pass

    def apagar_nave(self):
        pass