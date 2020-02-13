# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
     # constructor
    def __init__(self, name, description):
        # attributes (room, name character)
        self.name = name
        self.description = description
    def __str__(self):
        output = ''
        output += self.name + '. \nDescription: ' + self.description
        return output

r = Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.")

# print(r)

