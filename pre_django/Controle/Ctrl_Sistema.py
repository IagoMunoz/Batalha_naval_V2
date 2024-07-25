from Visual.View_Sistema import ViewSys

class CtrlSys():
    def __init__(self):
        self.__view_sys = ViewSys()
    
    #########################33 getters e setters ###########333

    @property
    def view_sys(self):
        return self.__view_sys

    @view_sys.setter
    def view_sys(self, view_sys):
        self.__view_sys = view_sys

    ############## funçoes especificas ##############3

    def sys_exit(self):
        self.__view_sys.exit()
        exit(0)

    ############### funçoes menu ######################

    def view_sys_main(self):
        cases = [self.sys_exit]
        action = self.__view_sys.main()
        cases[action]()

    