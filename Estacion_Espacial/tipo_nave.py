from abc import ABC,abstractmethod

class Tipo_nave(ABC):

    @abstractmethod
    def crear_nave(self):
            pass

    @abstractmethod
    def encender_nave(self):
            pass

    @abstractmethod
    def apagar_nave(self):
            pass




