from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room('outside', "outside the Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room('foyer', "in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room('overlook', "at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room('narrow', "in a Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room('treasure', "in the Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

valid_inputs = ['N', 'E', 'S', 'W', 'NORTH', 'EAST', 'SOUTH', 'WEST']


def find_room(a_dict, key):
    output = 'Not found'
    for room in a_dict:
        if room == key:
            output = 'Found'
    return output

def check_input(user_input):
    output = 'Not found'
    user_input = user_input.upper()
    for word in valid_inputs:
        if user_input == word:
            output = 'Found'
    return output

# Make a new player object that is currently in the 'outside' room.

player_start = input('Welcome player. What is your name? ')

player = Player('outside', str(player_start))

print(f'Welcome {player.name}. You can quit at any time by typing "Q".')

first_step = str(input(f'You are currently {player.cur_room}. You can move North, West, South or East throughout the game. Where would you like to go? '))

search_input = check_input(first_step)

# while selection != 'Q'

if search_input == 'Found':
    print('good answer', first_step.upper())
else:
    print("Please enter a valid move, like 'n' or 'North' ")

search_room = find_room(room, player.cur_room)

if search_room == 'Found':
    print(room[player.cur_room]['location'])
else:
    print("OH NO")

# Should movement between rooms be based on a series of methods on the player or room class, or should the possible moves be presented to the user (1. north, 2. south) for improved UI. Could store possible movements on each room and render via a loop.

# move = str(input(f'{player.name}, you are currently {room[player.cur_room]['location']}. You can move North, West, South or East throughout the game. Where would you like to go? '))

# if valid, then go into loop to move and check if valid for that room type


# instead of referencing the string, reference the room stored on Player (but if the rooms change during the game, you'd only want to reference the key, in case the room value itself changes)

# Write a loop that:
# * Prints the current room name
# ---> look up room in dictionary...?

# * Prints the current description (the textwrap module might be useful here).
# Text wrap Python docs: https://docs.python.org/2/library/textwrap.html
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
