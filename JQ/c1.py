import json

def read_pokedata(file_name):
    try:
        with open(file_name, 'r') as file:
            #initializing dictionary
            pokemon_data = {}
            for line in file:
                data = line.strip().split(',')

                #extracting values
                name = data[0]
                pokemon_type = data[1]
                continents = data[2:]

                # Store the data in a dictionary
                pokemon_data[name] = {'name':name,'type': pokemon_type, 'locations': continents}

            #returning the dictionary
            return pokemon_data
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return None
