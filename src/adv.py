from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room('outside', "outside the Cave Entrance", "North of you, the cave mouth beckons"),

    'foyer':    Room('foyer', "in the Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room('overlook', "at the Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room('narrow', "in a Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room('treasure', "in the Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

def find_room(a_dict, key):
    output = 'Not found'
    for room in a_dict:
        if room == key:
            output = 'Found'
    return output

# Make a new player object that is currently in the 'outside' room.

player_start = input('Welcome player. What is your name? ')

player = Player('outside', str(player_start))

newline = '\n'

print(f'Welcome {player.name}. You can quit at any time by typing "Q". {newline} You can move throughout the game by typing North, West, South or East (N, W, S, E).')

direction = ''
while direction != 'Q':

    direction = str(input(f'{newline} ** You are currently {room[player.cur_room].location}. ** {newline} {newline} {room[player.cur_room].description} {newline} {newline} Where would you like to go? ')).upper()

    if direction in ('N', 'NORTH'):
        if hasattr(room[player.cur_room], f'n_to'):
            player.cur_room = room[player.cur_room].n_to.name
        else:
            print('You cannot move North from this room.')
    elif direction in ('S', 'SOUTH'):
        if hasattr(room[player.cur_room], f's_to'):
            player.cur_room = room[player.cur_room].s_to.name
        else:
            print('You cannot move South from this room.')
    elif direction in ('E', 'EAST'):
        if hasattr(room[player.cur_room], f'e_to'):
            player.cur_room = room[player.cur_room].e_to.name
        else:
            print('You cannot move East from this room.')
    elif direction in ('W', 'WEST'):
        if hasattr(room[player.cur_room], f'w_to'):
            player.cur_room = room[player.cur_room].w_to.name
        else:
            print('You cannot move West from this room.')

    elif direction != 'Q':
        print("Please enter a valid move, like 'n' or 'North' ")

print(f'{newline} Thanks for playing! {newline}')

# * Prints the current description (the textwrap module might be useful here).
# Text wrap Python docs: https://docs.python.org/2/library/textwrap.html
