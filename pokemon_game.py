import random
import requests


def pokemon_details():
    pokemon_id = random.randint(1, 151)

    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    response = requests.get(url)
    pokemon = response.json()

    pokemon_name = pokemon['name'].title()
    pokemon_height = pokemon['height']
    pokemon_weight = pokemon['weight']
    pokemon_hp = pokemon['stats'][0]['base_stat']
    pokemon_attack = pokemon['stats'][1]['base_stat']
    pokemon_defense = pokemon['stats'][2]['base_stat']
    pokemon_spattack = pokemon['stats'][3]['base_stat']
    pokemon_spdefense = pokemon['stats'][4]['base_stat']
    pokemon_speed = pokemon['stats'][5]['base_stat']
    return {'ID': pokemon_id, 'Name': pokemon_name, 'Height': pokemon_height,
            'Weight': pokemon_weight, 'HP': pokemon_hp, 'Attack': pokemon_attack,
            'Defense': pokemon_defense, 'Special Attack': pokemon_spattack,
            'Special Defense': pokemon_spdefense, 'Speed': pokemon_speed}


def present_pokemon_options():
    print('\nYour choices are...')
    for option in pokemon_options:
        print(f'{option} : {pokemon_options[option]["Name"]}')
    return input('You pick: ')


def present_stat_options():
    print('Which stat would you like to compare?')
    for option_no, stat in enumerate(stats):
        if stat != 'Name' and stat != 'ID':
            print(f'{option_no}: {stat}')
    return input('You choose: ')


def present_keep_going_options():
    return input('\nWould you like to keep going Y/N? ').upper()


# Start of programme run

tournament_ongoing = True
player_score = 0
opponent_score = 0
stats = ['Height', 'Weight', 'HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed']


while tournament_ongoing:
    pokemon_options = {'1': pokemon_details(), '2': pokemon_details(), '3': pokemon_details()}
    player_pick = present_pokemon_options()
    while player_pick not in pokemon_options and \
            not any(pokemon['Name'].title() == player_pick.title() for pokemon in pokemon_options.values()):
        print('\nYou have not chosen a valid pokemon. Please try again.')
        player_pick = present_pokemon_options()

    try:
        player_pokemon = pokemon_options[str(player_pick)]
    except:
        for choice in range(1,4):
            if str(pokemon_options[str(choice)]['Name']).lower() == str(player_pick).lower():
                player_pokemon = pokemon_options[str(choice)]
    opponent_pokemon = pokemon_details()

    print(f'\n{player_pokemon["Name"]}, I choose you!')
    print(f'Your opponent sends out {opponent_pokemon["Name"]}!\n')

    chosen_stat = present_stat_options()
    valid_stat = False
    while not valid_stat:
        try:
            if int(chosen_stat) in range(0, len(stats)):
                valid_stat = True
                chosen_stat = stats[int(chosen_stat)]
            else:
                print('\nThe stat you have chosen is not valid. Please try again.\n')
                chosen_stat = present_stat_options()
        except:
            if chosen_stat.lower() in map(str.lower, player_pokemon.keys()):
                valid_stat = True
                chosen_stat = stats[[stat.lower() for stat in stats].index(chosen_stat.lower())]
            else:
                print('\nThe stat you have chosen is not valid. Please try again.\n')
                chosen_stat = present_stat_options()

    print(f'\nThe {chosen_stat.lower()} of your {player_pokemon["Name"]} is {player_pokemon[chosen_stat]}.')
    print(f'The {chosen_stat.lower()} of the opponent\'s {opponent_pokemon["Name"]} is {opponent_pokemon[chosen_stat]}.\n')

    if player_pokemon[chosen_stat] > opponent_pokemon[chosen_stat]:
        print('You win the match! You score a point.')
        player_score += 1
    elif player_pokemon[chosen_stat] == opponent_pokemon[chosen_stat]:
        print('Amazing! It\'s a draw! No one gets a point.')
    else:
        print('Your opponent wins! They score a point.')
        opponent_score += 1

    keep_going = present_keep_going_options()
    while keep_going != 'Y' and keep_going != 'N':
        print('Please pick Y or N.')
        keep_going = present_keep_going_options()
        print(keep_going)
    if keep_going == 'N':
        tournament_ongoing = False
    elif keep_going == 'Y':
        tournament_ongoing = True

badges = {0: 'Yellow',
          1: 'Crystal',
          2: 'Emerald',
          3: 'Platinum',
          4: 'Greyscale',
          5: 'Singularity',
          6: 'Cosmic',
          7: 'Battle',
          8: 'Chrono',
          9: 'Chrono'}
print(f'\nYour final score is {player_score} and your opponent\'s score is {opponent_score}.')
if player_score > opponent_score:
    if (player_score - opponent_score)//10 > 9:
        print(f'\n☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆\n'
              f'Holy moly! We\'ve got a Pokemon Master over here! Pssst... '
              f'When was the last time you wandered into the tall grass?'
              f'\n☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆')
    else:
        print(f'☆ You defeated your opponent! '
              f'Congratulations, here is your {badges[(player_score-opponent_score)//10]} badge! ☆')
else:
    print('☹ You weren\'t able to defeat your opponent. You dropped some prize money! ☹')
print('\nThe tournament has concluded. Thanks for participating!')