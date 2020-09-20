class ElementoPilha:

    def __init__(self, valor=0, ant=None):
        self.__valor = valor
        self.__anterior = ant

    def valor(self):
        return self.__valor

    def anterior(self):
        return self.__anterior

    def anterior_setter(self, anterior):
        self.__anterior = anterior

    def __str__(self):
        return str(self.__valor)