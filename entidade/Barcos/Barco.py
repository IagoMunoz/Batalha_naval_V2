from abc import abstractmethod, ABC


class Barco(ABC):
    @abstractmethod
    def __init__(self, tipo_barco, comprimento_barco):
        self.__bar_pos = []
        self.__bar_tipo = tipo_barco
        self.__bar_len = comprimento_barco
        self.__bar_vivo = True

########################### getters e setters ###########################

    @property
    def bar_pos(self):
        return self.__bar_pos

    @bar_pos.setter
    def bar_pos(self, bar_pos):
        self.__bar_pos = bar_pos

    @property
    def tipo_bar(self):
        return self.__bar_tipo

    @tipo_bar.setter
    def tipo_bar(self, tipo_bar):
        self.__bar_tipo = tipo_bar

    @property
    def len_bar(self) -> int:
        return self.__bar_len

    @len_bar.setter
    def len_bar(self, len_bar):
        self.__bar_len = len_bar

    @property
    def vivo_bar(self):
        return self.__bar_vivo

    @vivo_bar.setter
    def vivo_bar(self, vivo_bar):
        self.__bar_vivo = vivo_bar

###################### Funçoes especificas ###################

    def add_bar_pos(self, posicao_para_barco):
        self.__bar_pos.append(posicao_para_barco)