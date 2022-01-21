class Pokemon:
    def __init__(self, nr, name, type1, type2, total, HP, Atk, Def, Sp_Atk, Sp_Def, Spd, Gen, Legendary):
        self.nr = nr
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.HP = HP
        self.Atk = Atk
        self.Def = Def
        self.Sp_Atk = Sp_Atk
        self.Sp_Def = Sp_Def
        self.Spd = Spd
        self.Gen = Gen
        self.Legendary = Legendary

    def __str__(self):
        return "#" + self.nr + " " + self.name + ", type: " + self.type1 + ", "  +  self.type2 + ", hp: " + self.HP + ", Atk: " + self.Atk + ", Def: " + self.Def + ", Sp.Atk " + self.Sp_Atk + ", Sp.Def " + self.Sp_Def + ", Spd: " + self.Spd + ", Gen: " + self.Gen + ", Legendary " + self.Legendary

    def __lt__(self, other):
        return self.total<other.total

    def take_damage(self, damage, sp_damage):
        return 0
