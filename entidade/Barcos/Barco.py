from abc import abstractmethod, ABC


class Barco(ABC):
    @abstractmethod
    def __init__(self, tipo_barco, comprimento_barco):
        self.__pos_bar = []
        self.__vivo_bar = True
        self.__tipo_bar = tipo_barco
        self.__len_bar = comprimento_barco

########################### getters e setters ###########################

    @property
    def pos_bar(self):
        return self.__pos_bar

    @pos_bar.setter
    def pos_bar(self, pos_bar):
        self.__pos_bar = pos_bar
 
    @property
    def vivo_bar(self):
        return self.__vivo_bar

    @vivo_bar.setter
    def vivo_bar(self, vivo_bar):
        self.__vivo_bar = vivo_bar

    @property
    def tipo_bar(self):
        return self.__tipo_bar

    @tipo_bar.setter
    def tipo_bar(self, tipo_bar):
        self.__tipo_bar = tipo_bar

    @property
    def len_bar(self) -> int:
        return self.__len_bar

    @len_bar.setter
    def len_bar(self, len_bar):
        self.__len_bar = len_bar