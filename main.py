from pokemon import Pokemon

def read_file():
    #funktion som läser in txt filen och returnerar en lista med objekt
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

def create_object(nr, name, type1, type2, total, HP, Atk, Def, Sp_Atk, Sp_Def, Spd, Gen, Legendary):
    newpokemon = Pokemon(nr, name, type1, type2, total, HP, Atk, Def, Sp_Atk, Sp_Def, Spd, Gen, Legendary)
    print(str(newpokemon))
    return newpokemon

def search_pokemon(pokemon_list):
    pokemon_search = input("what pokemon do you want to find?")
    found_pokemon = ""
    for i in range(len(pokemon_list)):
        if pokemon_list[i].get_name() == pokemon_search:
            found_pokemon = pokemon_list[i]
    if found_pokemon == "":
        print("We could not find your pokemon!")
    else:
        print("Vi hittade din pokemon: \n" + found_pokemon)

def main():
    pokemon_list = read_file()

    create_object("1111", "boll", "Water", "Flying", "600", "200", "100", "100", "100", "100", "100", "10", "True")

    search_pokemon(pokemon_list)

main()
