#%%
def is_possible_game(cubes, game):
    for subset in game:
        colors = subset.split()
        color = colors[1]  # Extraer el color (red, green o blue)
        count = int(colors[0])  # Extraer la cantidad de cubos en el conjunto

        if cubes[color] < count:
            return False

    return True

def sum_possible_game_ids(cube_configuration, games_text):
    total_sum = 0

    # Dividir el texto de los juegos en juegos individuales
    games = games_text.split('\n')

    for game in games:
        if not game:
            continue

        game_info = game.split(":")[1].strip()
        subsets = game_info.split(";")

        if is_possible_game(cube_configuration, subsets):
            game_id = int(game.split(":")[0].split()[1])
            total_sum += game_id

    return total_sum

# Ejemplo de uso
cube_configuration = {
    'red': 12,
    'green': 13,
    'blue': 14
}

games_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

result = sum_possible_game_ids(cube_configuration, games_input)
print(result)
# %%
