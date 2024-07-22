from abc import abstractmethod, ABC
#jogador, aquele que joga
#podendo ser o computador ou um usuario


class Jogador(ABC):
    @abstractmethod
    def __init__(self, nome_do_jogador):
        self.__jog_nome = nome_do_jogador
        self.__jog_pts = 0
        self.__jog_partidas = []

####################### getters e setters #################

    @property
    def jog_nome(self):
        return self.__jog_nome

    @jog_nome.setter
    def jog_nome(self, jog_nome):
        self.__jog_nome = jog_nome

    @property
    def jog_pts(self):
        return self.__jog_pts

    @jog_pts.setter
    def jog_pts(self, jog_pts):
        self.__jog_pts = jog_pts

    @property
    def jog_partidas(self):
        return self.__jog_partidas

    @jog_partidas.setter
    def jog_partidas(self, jog_partidas):
        self.__jog_partidas = jog_partidas