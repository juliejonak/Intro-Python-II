# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, cur_room, name):
        self.cur_room = cur_room
        self.name = name

    
    def __repr__(self):
        return(self.name, self.cur_room)
