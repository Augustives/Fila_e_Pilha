from ElementoFila import ElementoFila

class Fila:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None

    def add(self, valor):
        novo_elemento = ElementoFila(valor)

        if self.__primeiro == None:
            self.__primeiro = novo_elemento
            self.__ultimo = novo_elemento
        else:
            self.__ultimo.proximo_setter(novo_elemento)
            self.__ultimo = novo_elemento

    def remove(self):
        print("Valor: " + str(self.__primeiro))
        self.__primeiro = self.__primeiro.proximo()

        if self.__primeiro == None:
            self.__ultimo = None

    def vazia(self):
        return self.__primeiro == None