from ElementoPilha import ElementoPilha


class Pilha:
    def __init__(self):
        self.__topo = None

    def add(self, valor):
        novo_elemento = ElementoPilha(valor)
        novo_elemento.anterior_setter(self.__topo)
        self.__topo = novo_elemento

    def remove(self):
        print("Valor: " + str(self.__topo))
        self.__topo = self.__topo.anterior()

    def vazia(self):
        return self.__topo == None
