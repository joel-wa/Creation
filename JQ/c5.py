from c1 import read_pokedata
from c2 import find_continents
from c3 import pokemon_in_continent
from c4 import count_types

#change the c1...c4 names to the actual name of your files


pokemon_data_location = ""
 
pokemon_data = read_pokedata(pokemon_data_location)
continentList = find_continents()

def getPokemonInfo():
    for continent in continentList:
        # print(continent)
        pok_in_content =  pokemon_in_continent(pokemon_data,continent)
        number_of_pok_in_content = len(pok_in_content)
        # print(number_of_pok_in_content)
        count = count_types(pokemon_data,pok_in_content)
        # print(count)

        print(f"{continent}:{number_of_pok_in_content} total pokemon")
        print(f"{count}")





if __name__ == '__main__':
    getPokemonInfo()
