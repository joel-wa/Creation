import unittest
from c2 import find_continents
from c3 import pokemon_in_continent
from c4 import count_types

class TestPokemonFunctions(unittest.TestCase):
    def setUp(self):
        # Example data
        self.pokemon_data = {
            'bulbasaur': {'type': 'grass', 'locations': ['South America']},
            'ivysaur': {'type': 'grass', 'locations': ['Asia', 'Antarctica']},
            'charmander': {'type': 'fire', 'locations': ['North America']},
            # Add more Pokemon data as needed
        }

    def test_find_continents(self):
        continents_list = find_continents(self.pokemon_data)
        self.assertCountEqual(continents_list, ['South America', 'Asia', 'Antarctica', 'North America'])

    def test_pokemon_in_continent(self):
        target_continent = 'Asia'
        pokemon_on_continent_list = pokemon_in_continent(self.pokemon_data, target_continent)
        self.assertEqual(pokemon_on_continent_list, ['ivysaur'])

    def test_count_types(self):
        pokemon_names_list = ['bulbasaur', 'ivysaur', 'charmander', 'squirtle']
        type_count_result = count_types(self.pokemon_data, pokemon_names_list)
        self.assertEqual(type_count_result, {'grass': 2, 'fire': 1})

if __name__ == '__main__':
    unittest.main()


#in your c3.py file, change "continents" to "locations"