from pokemon import Pokemon

def create_object(nr, name, type1, type2, total, HP, Atk, Def, Sp_Atk, Sp_Def, Spd, Gen, Legendary):
    pass


def registerread():
    #funktion som läser in registerfilen och returnerar en lista med objekt
    objectlst = []
    try:
        file = open("poke.txt", "r")
    except IOError:
        print("Error: File does not exist")
        return
    objectstr = file.read().split("\n")
    for i in range(len(objectstr)):
        templst = objectstr[i].split(",")
        tempobj = Pokemon(templst[0], templst[1], templst[2], templst[3], templst[4], templst[5], templst[6], templst[7], templst[8], templst[9], templst[10], templst[11], templst[12])
        objectlst.append(tempobj)
    return objectlst


lista = registerread()
for i in range(len(lista)):
    print(lista[i])
