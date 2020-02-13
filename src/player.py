# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    # constructor
    def __init__(self, room, character, attributes):
        # attributes (room, name character)
        self.room = room
        self.character = character
        self.attributes = attributes
    def __str__(self):
        output = ''
        output += self.character + ' is in the ' +  self.room + ' room.'
        return output


p = Player("Outside Cave Entrance", "Lorenzo", ["Man", "Black hair", "19 years old"])

# print(p)
    