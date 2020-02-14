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
        output += self.name + '. \nDescription: ' + self.description + '\n Choose your next move.'
        return output

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def get_next_room(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        else:
            return None


r = Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.")

# print(r)

