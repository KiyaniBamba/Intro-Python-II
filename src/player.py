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


p = Player("Outside Cave Entrance", "Lorenzo")

# print(p)
    