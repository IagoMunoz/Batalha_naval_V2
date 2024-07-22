from Jogador import Jogador


class Usuario(Jogador):
    def __init__(self, id_do_usuario, nome_do_usuario, data_nascimento):
        super().__init__(nome_do_usuario)
        self.__user_id = id_do_usuario
        self.__user_birth = data_nascimento

####################### getters e setters ###########################

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def user_birth(self):
        return self.__user_birth

    @user_birth.setter
    def user_birth(self, user_birth):
        self.__user_birth = user_birth
