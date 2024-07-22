from Jogador import Jogador

'''No começo significava Allied Mastercomputer [Computador-mestre
   Aliado], depois passou a significar Adaptative Manipulator 
   [Manipulador Adaptativo], mas mais tarde ele se tornou consciente
   e passaram a chamá-lo de Agressive Menace [Ameaça Agressiva], só 
   que aí já era tarde demais e, por fim, ele mesmo, com sua 
   inteligência emergente, passou a se chamar de AM, dizendo que isso
   significa “I am”, ou seja, “eu sou”... I think, therefore I am... 
   Penso, logo existo.'''

class Computador(Jogador):
    def __init__(self):
        super().__init__("Computador")
        #aqui vai ter o pc inteligente