def find_continents(pokemon_data):

    #Using a set for idempotency
    unique_continents = set()

    #iterating over each pokemon's data in the dictionary
    for pokemon_info in pokemon_data.values():
        continents = pokemon_info.get('locations', [])
        unique_continents.update(continents)

    return list(unique_continents)

