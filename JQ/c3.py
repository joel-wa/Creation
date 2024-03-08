def pokemon_in_continent(pokemon_data, target_continent):
    pokemon_on_continent = []

    for pokemon_name, pokemon_info in pokemon_data.items():
        continents = pokemon_info.get('continents', [])

        #adding condition to add only matching pokemons
        if target_continent in continents:
            pokemon_on_continent.append(pokemon_name)

    return pokemon_on_continent

