class Pokemon:
    def __init__(self, nr, name, type1, type2, total, HP, Atk, Def, Sp_Atk, Sp_Def, Spd, Gen, Legendary):
        self.__nr = nr
        self.__name = name
        self.__type1 = type1
        self.__type2 = type2
        self.__total = total
        self.__HP = HP
        self.__Atk = Atk
        self.__Def = Def
        self.__Sp_Atk = Sp_Atk
        self.__Sp_Def = Sp_Def
        self.__Spd = Spd
        self.__Gen = Gen
        self.__Legendary = Legendary

    def __str__(self):
        return "#" + self.__nr + " " + self.__name + ", type: " + self.__type1 + ", "  +  self.__type2 + ", hp: " + self.__HP + ", Atk: " + self.__Atk + ", Def: " + self.__Def + ", Sp.Atk " + self.__Sp_Atk + ", Sp.Def " + self.__Sp_Def + ", Spd: " + self.__Spd + ", Gen: " + self.__Gen + ", Legendary " + self.__Legendary

    def __lt__(self, other):
        return int(self.__total)<int(other.get_total)

    def get_name(self):
        return self.__name

    def get_total(self):
        return self.__total

    def faint():
        self.__hp = 0
