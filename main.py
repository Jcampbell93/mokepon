from mokepon import Mokepon
from pyapi import create_mokepon_from_api


def setup_player(player_name: str):
    mokepon_choices = ['charmander', 'squirtle', 'bulbasaur', 'pikachu', 'eevee', 'geodude']

    while True:
        print('Choose from:', mokepon_choices)
        mokepon_choice = input("Which mokepon would you like to choose " + player_name + "? ")
        if mokepon_choice in mokepon_choices:
            return create_mokepon_from_api(mokepon_choice)


def run_game():
    player_one = setup_player("Player 1")
    player_two = setup_player("Player 2")

    active_player = player_one
    inactive_player = player_two

    while player_one.is_alive and player_two.is_alive:
        while True:
            for option in player_options:
                print(option + ") " + player_options[option]["name"])
            choice = input("What Move would " + active_player.name + " like to do: ").upper()
            if choice == 'A' or choice == 'B':
                break
        player_turn(active_player, inactive_player, choice)

        current_player = active_player
        active_player = inactive_player
        inactive_player = current_player

    if player_one.is_alive:
        print(player_one.name, 'Wins!')

    if player_two.is_alive:
        print(player_two.name, 'Wins!')


def attack(active_player: Mokepon, inactive_player: Mokepon):
    inactive_player.take_damage(active_player.damage, active_player.elemental_type.name)


def other_function(player_one: Mokepon, player_two: Mokepon):
    print(player_one.name, 'other')


player_options = {
    "A": {"name": "Attack", "function": attack},
    "B": {"name": "Other", "function": other_function}
}


def player_turn(active_player, inactive_player, player_choice):

    print(active_player.name, 'chose', player_options[player_choice]["name"])
    player_options[player_choice]["function"](active_player, inactive_player)
    print(inactive_player.health)
    if inactive_player.health > 0:
        print(inactive_player.name, 'Health is', inactive_player.health)
    else:
        print(inactive_player.name, 'fainted!')


run_game()


# Things to add;
# different monsters,
# choice of action
#   different abilities (can have a type), heals,

# https://pokeapi.co/
# https://pokeapi.co/api/v2/pokemon/ditto