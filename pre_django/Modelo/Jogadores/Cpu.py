'''No começo significava Allied Mastercomputer [Computador-mestre
   Aliado], depois passou a significar Adaptative Manipulator 
   [Manipulador Adaptativo], mas mais tarde ele se tornou consciente
   e passaram a chamá-lo de Agressive Menace [Ameaça Agressiva], só 
   que aí já era tarde demais e, por fim, ele mesmo, com sua 
   inteligência emergente, passou a se chamar de AM, dizendo que isso
   significa “I am”, ou seja, “eu sou”... I think, therefore I am... 
   Penso, logo existo.'''
from random import randint

class Cpu():
    def __init__(self):
        self.__cpu_nome = "Computador"

 ################ getters e setters ###########################
 
    @property
    def cpu_nome(self):
        return self.__cpu_nome

    @cpu_nome.setter
    def cpu_nome(self, cpu_nome):
        self.__cpu_nome = cpu_nome

################  funçoes especificas #########################

    def tiro_rand_cpu(self, oceano_medidas, jatirou):
        linha = randint(1,oceano_medidas[0])
        coluna = randint(1, oceano_medidas[1])
        
        while [coluna, linha] in jatirou:
            linha = randint(1,oceano_medidas[0])
            coluna = randint(1, oceano_medidas[1])

        return [coluna, linha]

          
        