

class Usuario():
    def __init__(self, id_do_usuario, nome_do_usuario, data_nascimento):

        self.__user_id = id_do_usuario
        self.__user_nome = nome_do_usuario
        self.__user_birth = data_nascimento
        self.__user_pts = 0
        self.__user_jogos = []

####################### getters e setters ###########################

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def user_nome(self):
        return self.__user_nome

    @user_nome.setter
    def user_nome(self, user_nome):
        self.__user_nome = user_nome

    @property
    def user_birth(self):
        return self.__user_birth

    @user_birth.setter
    def user_birth(self, user_birth):
        self.__user_birth = user_birth

    @property
    def user_pts(self):
        return self.__user_pts

    @user_pts.setter
    def user_pts(self, user_pts):
        self.__user_pts = user_pts

    @property
    def user_jogos(self):
        return self.__user_jogos

    @user_jogos.setter
    def user_jogos(self, user_jogos):
        self.__user_jogos = user_jogos

##################### funçoes especificas ##################

    def user_jogos_add(self, jogo_recem_jogado):
        self.__user_jogos.append(jogo_recem_jogado)
