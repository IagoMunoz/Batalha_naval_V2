from abc import abstractmethod, ABC
#jogador, aquele que joga
#podendo ser o computador ou um usuario


class Jogador(ABC):
    @abstractmethod
    def __init__(self, nome_do_jogador):
        self.__jog_nome = nome_do_jogador
        self.__jog_pts = 0
        self.__jog_jogos = []

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
    def jog_jogos(self):
        return self.__jog_jogos

    @jog_jogos.setter
    def jog_jogos(self, jog_jogos):
        self.__jog_jogos = jog_jogos

##################### funçoes especificas ##################

    def add_partida(self, jogo_recem_jogado):
        self.__jog_jogos.append(jogo_recem_jogado)