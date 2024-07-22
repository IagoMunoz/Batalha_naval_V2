from Barco import Barco


class Bote(Barco):
    def __init__(self):
        super().__init__("Bote", 1)

##############################################


class Sub(Barco):
    def __init__(self):
        super().__init__("Submarino", 2)

##############################################


class Frag(Barco):
    def __init__(self):
        super().__init__("Fragata", 3)

##############################################


class Porta(Barco):
    def __init__(self):
        super().__init__("Porta-aviões", 4)