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

    def heal(self, potion=None):
        if potion:
            self.xp += potion.strength
            if self.xp > self.max_xp:
                self.xp = self.max_xp

    def receive_damage(self, monster=None):
        if monster:
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


class Potion():
    def __init__(self, strength):
        self.strength = strength


def setup_rooms(rooms, monsters, potions):
    '''
    If you shuffle rooms before assignment then items will always be in the same index in rooms_map.keys()
        - It isn't ideal but it works given the user will start in a random room and won't have access to the rooms_map

    If you shuffle afterwards then the items will always be in the same room (EG: Kitchen could always have the key)

    TODO: Find a workaround if time permits
    '''
    # shuffle rooms
    random.shuffle(rooms)

    # place content into rooms
    room[0].has_key = True
    room[1].is_garden = True
    room[2].can_transport = True
    room[3].monster = monsters[0]
    room[4].monster = monsters[1]
    room[5].potion = potions[0]
    room[6].potion = potions[1]

    # assign IDs
    for i in range(len(rooms)):
        rooms[i].id = i

    return rooms

def showInstructions():
    """"Get to the Garden with a key and a potion to win! Avoid the monsters! Commands include go direction and get item."""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


def setup_game():
    # create rooms, potions, and monsters
    rooms = [
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

    potions = [Potion(10), Potion(25)]

    monsters = [Monster(25), Monster(50)]

    rooms = setup_rooms(rooms, monsters, potions)
   
    # a dictionary linking a room to other rooms
    rooms_map = {
            0: {
                'room' : rooms[0],
                'South' : rooms[3],
                'East' : rooms[1],
                'West' : rooms[6],
                'doors' : ['South', 'East', 'West']
                },
            1: {
                'room': rooms[1],
                'West': rooms[0],
                'doors' : ['West']
                },
            2: {
                'room' : rooms[2],
                'South' : rooms[7],
                'East' : rooms[3],
                'doors' : ['South', 'East']
                },
            3: {
                'room' : rooms[3],
                'West' : rooms[2],
                'East' : rooms[4],
                'North' : rooms[0],
                'doors' : ['West', 'East']
                },
            4: {
                'room' : rooms[4],
                'West' : rooms[3],
                'East' : rooms[5],
                'South' : rooms[8],
                'doors' : ['West', 'East', 'South']
                },
            5: {
                'room' : rooms[5],
                'West' : rooms[4],
                'South' : rooms[9],
                'doors' : ['West', 'South']
                },
            6: {
                'room' : rooms[6],
                'East' : rooms[7],
                'North' : rooms[0],
                'doors' : ['East', 'North']
                },
            7: {
                'room' : rooms[7],
                'West' : rooms[6],
                'North' : rooms[2],
                'doors' : ['West', 'North']
                },
            8: {
                'room' : rooms[8],
                'North' : rooms[4],
                'East' : rooms[9],
                'doors' : ['North', 'East']
                },
            9: {
                'room' : rooms[9],
                'West' : rooms[8],
                'North' : rooms[5],
                'doors' : ['West', 'North']
                }
            }

    # create user
    username = input('Enter player name')
    player = Player(username)

    return [rooms_map, rooms, monsters, potions, player]

def play_game():


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


