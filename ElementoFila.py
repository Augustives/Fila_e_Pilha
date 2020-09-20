class ElementoFila:

    def __init__(self, valor=0, prox=None):
        self.__valor = valor
        self.__proximo = prox

    def valor(self):
        return self.__valor

    def proximo(self):
        return self.__proximo

    def proximo_setter(self, proximo):
        self.__proximo = proximo

    def __str__(self):
        return str(self.__valor)