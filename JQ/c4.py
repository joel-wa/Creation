def count_types(pokemon_data, pokemon_names):
    #initializing dict to store counted types
    type_count = {}

    for name in pokemon_names:
        if name in pokemon_data:
            pokemon_type = pokemon_data[name].get('type')

            #making sure that the pokemon_type exists in the database
            if pokemon_type:

                #Here, we are checking the current count of the given pokemon type in the type_count dict
                #If none already exists in the type_count dict, we are giving it a default value of 0
                #If it exists, we will just increase its count
                type_count[pokemon_type] = type_count.get(pokemon_type, 0) + 1

    return type_count
