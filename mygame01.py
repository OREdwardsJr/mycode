#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import random

class Player():
    def __init__(self, name, xp=100, max_xp=100, location=0, has_key=False):
        self.name = name
        self.xp = xp
        self.max_xp = max_xp
        self.location = location #Stores which room Player currently is in - Player starts in rooms_map[0]
        self.has_key = has_key

    def heal(self, potion):
        self.xp += potion.strength
        
        self.xp = self.xp if (self.xp <= self.max_xp) else self.max_xp

    def receive_damage(self, monster):
        self.xp -= monster.strength


class Monster():
    def __init__(self, strength):
        self.strength = strength


class Room():
    def __init__(self, name, has_key=False, is_garden=False, can_transport=False, monster=None, potion=None, _id=-1):
        self.name = name
        self.has_key = has_key
        self.is_garden = is_garden
        self.can_transport = can_transport
        self.monster = monster
        self.potion = potion
        self.id = _id

    def __repr__(self):
        return self.name


class Potion():
    def __init__(self, strength):
        self.strength = strength


class Game():
    def __init__(self, rooms_map={}, rooms=[], monsters=[], potions=[], player=None):
        self.rooms_map = rooms_map
        self.rooms = rooms
        self.monsters = monsters
        self.potions = potions
        self.player = player

    def setup_game(self):
        # create rooms, potions, and monsters
        self.rooms = [
            Room("Kitchen"),
            Room("Bathroom 1"),
            Room("Bathroom 2"),
            Room("Master Bedroom"),
            Room("Study Room"),
            Room("Entertainment Room"),
            Room("Attic"),
            Room("Basement"),
            Room("Spare Bedroom"),
            Room("Garden")
        ]
        self.potions = [Potion(10), Potion(35), Potion(10)]
        self.monsters = [Monster(25), Monster(50)]

        # create user
        username = input('Enter player name')
        self.player = Player(username)

        self.showInstructions()

    def setup_rooms(self):
        '''
        Room objects are randomly stored in the nodes of an undirected graph. 
        Items (potions, monsters, key, etc...) are randomly assigned to rooms
            - Rooms may have multiple items of different categories
            - Rooms hold <= 1 of the same item type
            - EG: The kitchen may hold a key and monster but may not hold a a key and two monsters given the two monsters
                    are the same item type.
        '''
        # shuffle rooms into random nodes 
        random.shuffle(self.rooms)

        # assign room IDs
        for i in range(len(self.rooms)):
            self.rooms[i].id = i

        # -----------------------------------------------
        # Randomly place content into rooms

        # set key
        i = random.randrange(0, len(self.rooms))
        self.rooms[i].has_key = True

        # set garden
        i = random.randrange(0, len(self.rooms))
        self.rooms[i].is_garden = True

        # set transport
        i = random.randrange(0, len(self.rooms))
        self.rooms[i].can_transport = True

        # set monsters (while loop ensures rooms occupy <= 1 monster)
        i = j = random.randrange(0, len(self.rooms))
        self.rooms[i].monster = self.monsters[0]

        while (j == i):
            j = random.randrange(0, len(self.rooms))
            
        self.rooms[j].monster = self.monsters[1]

        # set potions (while loop ensures rooms occupy <= 1 potion)
        i = j = k = random.randrange(0, len(self.rooms))
        self.rooms[i].potion = self.potions[0]

        while (j == i):
            j = random.randrange(0, len(self.rooms))

        self.rooms[j].potion = self.potions[1]

        while (k == i):
            k = random.randrange(0, len(self.rooms))

        self.rooms[k].potion = self.potions[2]
        # -----------------------------------------------

        # fill graph (rooms mapping)
        self.rooms_map = {
            0: {
                'room' : self.rooms[0],
                'South' : self.rooms[3],
                'East' : self.rooms[1],
                'West' : self.rooms[6],
                'doors' : ['South', 'East', 'West']
                },
            1: {
                'room': self.rooms[1],
                'West': self.rooms[0],
                'doors' : ['West']
                },
            2: {
                'room' : self.rooms[2],
                'South' : self.rooms[7],
                'East' : self.rooms[3],
                'doors' : ['South', 'East']
                },
            3: {
                'room' : self.rooms[3],
                'West' : self.rooms[2],
                'East' : self.rooms[4],
                'North' : self.rooms[0],
                'doors' : ['West', 'East']
                },
            4: {
                'room' : self.rooms[4],
                'West' : self.rooms[3],
                'East' : self.rooms[5],
                'South' : self.rooms[8],
                'doors' : ['West', 'East', 'South']
                },
            5: {
                'room' : self.rooms[5],
                'West' : self.rooms[4],
                'South' : self.rooms[9],
                'doors' : ['West', 'South']
                },
            6: {
                'room' : self.rooms[6],
                'East' : self.rooms[7],
                'North' : self.rooms[0],
                'doors' : ['East', 'North']
                },
            7: {
                'room' : self.rooms[7],
                'West' : self.rooms[6],
                'North' : self.rooms[2],
                'doors' : ['West', 'North']
                },
            8: {
                'room' : self.rooms[8],
                'North' : self.rooms[4],
                'East' : self.rooms[9],
                'doors' : ['North', 'East']
                },
            9: {
                'room' : self.rooms[9],
                'West' : self.rooms[8],
                'North' : self.rooms[5],
                'doors' : ['West', 'North']
                }
            }

    def enter_room(self, choice):
        location = self.player.location

        self.player.location = self.rooms_map[location][choice]

    def visit_mystery_room(self):
        num = random.randint(0, 10)

        if num < 3:
            print('You have a super strong potion!! Your XP has been reset to the maximum level')

            self.player.xp = self.player.max_xp
        elif 3 <= num < 6:
            print('Oh no! You ran into the strongest monster there is!!')

            self.player.xp -= 65
        else:
            print('You have been transported to the garden! I hope you have the key with you!')

            for room in self.rooms:
                if (room.name == "Garden"):
                    self.player.location = room.id

        print(f'{self.player.name}, your health is {self.player.xp}. You are being returned to {self.rooms_map[self.player.location]["room"]}')

    def showInstructions(self):
        """"Get to the Garden with a key and a potion to win! Avoid the monsters! Commands include go direction and get item."""
        #print a main menu and the commands
        print(f'''
        Welcome, {self.player}! Your goal is to acquire the key and bring it to the Garden where fortune awaits you!

        You must wander through the castle in search of the key. Be wary! Monsters are hidden in some of these rooms.

        Good luck!

        RPG Game
        ========
        Commands:
        go [direction]
        ''')
    
    def play_game(self):        
        active_game = True
        choice = ""

        self.showInstructions()

        while active_game:
            rooms_map_key = self.rooms_map[self.player.location] 
            room = rooms_map_key['room']
            doors = rooms_map_key['doors']

            #If room has key
            if (self.player.has_key == False) and (room.has_key):
                print('Congrats, you have found the key! You can achieve victory by reaching the Garden')

                self.player.has_key = True

            #If room has potion
            if (room.potion):
                print('You have found potion!')

                self.player.heal()

                print(f'Your health is now: {self.player.xp}')

            #If room has monster
            if (room.monster != None):
                print(f'''Oh no you ran into a monster!!!
                          It has a strength of {room.monster.strength} and has attacked you!
                          Beware, the monster has jumped to a random room. Its still out there!!''')

                self.player.receive_damage(room.monster)
                self.place_monster_in_new_room(room.monster)

                print(f'Your remaining xp is: {self.player.xp}')

            #If xp <= 0
            if (self.player.xp <= 0):
                print('Sorry! You have been defeated! Game over :(')
                exit()

            #If room can transport to mystery room
            if (room.can_transport):
                print(f'''This room has magical powers and can transport to a mystery room!
                          The mystery room consists of healing potion, a monster, or direct access
                          to the garden.''')

                visit_mystery_room = input('Would you like to visit mystery room?!? (y/n)').lower()

                if (visit_mystery_room == 'y'):
                    room = self.visit_mystery_room(room) # Updates room to garden or leaves as is

            #If room is garden
            if (room.is_garden):
                if (self.player.has_key):
                    print('Congrats!!! You have obtained the fortune and won the game!')
                    exit()

                print('Here is the fortune!! Unfortunately, you need the key to access it.')

            while choice not in doors:
                print(f'''{self.player}, you are located in {room}.
                        You can go through the following doors: {doors}.
                        Your health is {self.player.xp}
                ''')

                choice = input('Which door would you like to enter? (Enter "quit" to end game)').title()

                if (choice.lower() == "quit"):
                    print('Goodbye!')
                    exit()

            self.enter_room(choice)
        

def main():
    game = Game()

    game.setup_game()
    game.setup_rooms()
    game.play_game()

# Run Script
if __name__ == "__main__":
    main()

# LEFT OFF HERE #
'''
TODO: 
    - Build game logic.
        - if rooms[i].can_transport then handle_transport()
        - build logic to check player health and end accordingly
        - check whether user has delivered key to garden
'''
# Start Game
play_game()


showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    elif move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    else:
        print('Invalid command.'

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

