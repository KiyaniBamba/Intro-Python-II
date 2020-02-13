# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
     # constructor
    def __init__(self, name, description):
        # attributes (room, name character)
        self.name = name
        self.description = description
        self.n_to = {}
        self.s_to = {}
        self.e_to = {}
        self.w_to = {}

    def __str__(self):
        output = ''
        output += self.name + '. \nDescription: ' + self.description + '\n Choose your next move.'
        return output

r = Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.")

# print(r)

