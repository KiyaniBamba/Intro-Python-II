# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    # constructor
    def __init__(self, name, current_room):
        # attributes (room, name character)
        self.name = name
        self.current_room = current_room 

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