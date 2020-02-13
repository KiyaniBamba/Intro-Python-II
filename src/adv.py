from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""), 

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
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

# Make a new player object that is currently in the 'outside' room.


from player import Player

#initialize user
user_initialize = input ("Welcome on Adventure Game! \nTo start, enter the name of your character: ")
player_position = Player (room['outside'], user_initialize)
current_position = player_position.room

print("\nAwesome! Your hero,", user_initialize, "is in the", current_position)

print("Your mission is to find the king's treasure.")

print("- - - - - - - - - - - - - - - - - - - - - - \n")

print("Please, choose your direction to continue")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

direction = 0
while direction == 0:
    direction = input("[1] North  [2] South   [3] Est   [4] West    [9] Quit\n")
    try:
    # user chooses North
        if direction == "1":
            if player_position == Player (room['outside'], user_initialize):
                player_position = Player (room['outside'].n_to, user_initialize)
                print("You are in the", player_position.room)
                direction = 0
            elif player_position == Player (room['foyer'], user_initialize):
                player_position = Player (room['foyer'].n_to, user_initialize)
                print("You are in the", player_position.room)
                direction = 0
            elif player_position == Player (room['narrow'], user_initialize):
                player_position = Player (room['narrow'].n_to, user_initialize)
                print("You are in the", player_position.room)
                direction = 0
        # user chooses South
        elif direction == "2":
            if player_position == Player (room['foyer'], user_initialize):
                player_position = Player (room['foyer'].s_to, user_initialize)
                print("You are in the", player_position.room)
                direction = 0
            elif player_position == Player (room['overlook'], user_initialize):
                player_position = Player (room['overlook'].s_to, user_initialize)
                print("You are in the", player_position.room)
                direction = 0
            elif player_position == Player (room['treasure'], user_initialize):
                player_position = Player (room['treasure'].s_to, user_initialize)
                print("You are in the", player_position.room)
                direction = 0

        # user chooses Est
        elif direction == "3" and player_position == Player (room['foyer'], user_initialize):
            player_position = Player (room['foyer'].e_to, user_initialize)
            print("You are in the", player_position.room)
            direction = 0
        # user chooses West
        elif direction == "4" and player_position == Player (room['narrow'], user_initialize):
            player_position = Player (room['narrow'].w_to, user_initialize)
            print("You are in the", player_position.room)
            direction = 0
        elif direction == "9":
            print("Thank you for playing with me! Take care.")
        else:
            print("Oh dear, you have hit a wall! Invalid selection. Please try again.")
            direction = 0
            
        print("Please choose to continue...")