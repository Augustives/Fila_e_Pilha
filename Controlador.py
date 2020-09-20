from Pilha import Pilha
from Fila import Fila


class ControladorPrincipal:
    def __init__(self):
        self.__pilha = Pilha()
        self.__fila = Fila()
        self.__limitepilha = 5
        self.__limitefila = 5
        self.__contadorpilha = 0
        self.__contadorfila = 0

    def inicia(self):
        print("Escolha uma das opcoes:")
        print("----------  OPCOES  ----------")
        print("1 - Add na Pilha")
        print("2 - Excluir na Pilha")
        print("3 - Add na Fila")
        print("4 - Excluir na Fila")
        print("5 - Para escolher o limite de valores.")
        escolha = int(input("Digite o numero de uma das opcoes:"))

        if escolha == 1:
            self.add_pilha(float(input("Digite um valor para adicionar na pilha:")))
            self.inicia()
        if escolha == 2:
            self.remove_pilha()
            self.inicia()
        if escolha == 3:
            self.add_fila(float(input("Digite um valor para adicionar na fila:")))
            self.inicia()
        if escolha == 4:
            self.remove_fila()
            self.inicia()
        if escolha == 5:
            self.definir_limite()
            self.inicia()

    def add_pilha(self, valor):
        if int(self.__contadorpilha) >= int(self.__limitepilha):
            print("Impossivel adicionar um valor, pilha cheia. Por favor remova um valor antes de adicionar outro.")
        else:
            self.__pilha.add(valor)
            self.__contadorpilha += 1
            print("Valor " + str(valor) + " adicionado a pilha.")

    def remove_pilha(self):
        if self.__pilha.vazia():
            print("Impossivel remover um valor, pilha vazia.")
        else:
            self.__pilha.remove()
            self.__contadorpilha -= 1
            print("Valor no topo da Pilha removido.")

    def add_fila(self, valor):
        if int(self.__contadorfila) >= int(self.__limitefila):
            print("Impossivel adicionar um valor, fila cheia. Por favor remova um valor antes de adicionar outro.")
        else:
            self.__fila.add(valor)
            self.__contadorfila += 1
            print("Valor " + str(valor) + " adicionado a fila.")

    def remove_fila(self):
        if self.__fila.vazia():
            print("Impossivel remover um valor, fila vazia.")
        else:
            self.__fila.remove()
            self.__contadorfila -= 1
            print("Primeiro da fila removido.")

    def definir_limite(self):
        escolha = input("Para definir o limite da pilha ou da fila digite: 1 para Pilha ou 2 para Fila")
        if int(escolha) == 1:
            self.__limitepilha = input("Digite um inteiro para ser o limite de valores da pilha.")
        if int(escolha) == 2:
            self.__limitefila = input("Digite um inteiro para ser o limite de valores da fila.")
