# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    # constructor
    def __init__(self, room, character):
        # attributes (room, name character)
        self.room = room
        self.character = character
    def __str__(self):
        output = ''
        output = f'our hero is in the {self.room} room.'
        return output

# move method
    def move(self, direction):
        # move player in direction specified
        if direction in ['n', 's', 'e', 'w']:
        # move to the current rooms room to at direction
            next_room = self.current_room.get_next_room(direction)
            ## if there is a direction to move. move there
            if next_room is not None:
                self.current_room = next_room
            else:
                print('You can not move in that direction!')


p = Player("Outside Cave Entrance", "Lorenzo")

# print(p)
    