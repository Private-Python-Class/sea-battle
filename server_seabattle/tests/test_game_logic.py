from server_seabattle.game_logic import Field, empty, Ship1


def test_generate_gield():
    f = Field()
    expected_result = {'1A': 'empty', '1B': 'empty', '1C': 'empty', '1D': 'empty', '1E': 'empty', '1F': 'empty', '1G': 'empty', '1H': 'empty', '1I': 'empty', '1J': 'empty', '1K': 'empty', '2A': 'empty', '2B': 'empty', '2C': 'empty', '2D': 'empty', '2E': 'empty', '2F': 'empty', '2G': 'empty', '2H': 'empty', '2I': 'empty', '2J': 'empty', '2K': 'empty', '3A': 'empty', '3B': 'empty', '3C': 'empty', '3D': 'empty', '3E': 'empty', '3F': 'empty', '3G': 'empty', '3H': 'empty', '3I': 'empty', '3J': 'empty', '3K': 'empty', '4A': 'empty', '4B': 'empty', '4C': 'empty', '4D': 'empty', '4E': 'empty', '4F': 'empty', '4G': 'empty', '4H': 'empty', '4I': 'empty', '4J': 'empty', '4K': 'empty', '5A': 'empty', '5B': 'empty', '5C': 'empty', '5D': 'empty', '5E': 'empty', '5F': 'empty', '5G': 'empty', '5H': 'empty', '5I': 'empty', '5J': 'empty', '5K': 'empty', '6A': 'empty', '6B': 'empty', '6C': 'empty', '6D': 'empty', '6E': 'empty', '6F': 'empty', '6G': 'empty', '6H': 'empty', '6I': 'empty', '6J': 'empty', '6K': 'empty', '7A': 'empty', '7B': 'empty', '7C': 'empty', '7D': 'empty', '7E': 'empty', '7F': 'empty', '7G': 'empty', '7H': 'empty', '7I': 'empty', '7J': 'empty', '7K': 'empty', '8A': 'empty', '8B': 'empty', '8C': 'empty', '8D': 'empty', '8E': 'empty', '8F': 'empty', '8G': 'empty', '8H': 'empty', '8I': 'empty', '8J': 'empty', '8K': 'empty', '9A': 'empty', '9B': 'empty', '9C': 'empty', '9D': 'empty', '9E': 'empty', '9F': 'empty', '9G': 'empty', '9H': 'empty', '9I': 'empty', '9J': 'empty', '9K': 'empty', '10A': 'empty', '10B': 'empty', '10C': 'empty', '10D': 'empty', '10E': 'empty', '10F': 'empty', '10G': 'empty', '10H': 'empty', '10I': 'empty', '10J': 'empty', '10K': 'empty'}
    result = f.generate_field()
    print(result)
    assert expected_result == result


def test_create_field_and_set_ship_on_it():
    target_ceil = 'A1'
    f = Field()
    assert f.field[target_ceil] == empty
    s1 = Ship1([target_ceil])
    f.set_ship(s1)
    assert f.field[target_ceil] == s1