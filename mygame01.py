#!/usr/bin/python3

# import random
import random

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom] and rooms[currentRoom]['item'] != "monster":
    print('You see a ' + rooms[currentRoom]['item'])
  
  print("---------------------------")

def combatMode():
  # Display to show inventory and location
  showStatus()
  # print the current mode play has entered
  print("Welcome to Combat mode, You have encountered a monster and now have a chance to fight for your life")
  print('''
  Combat Mode
  ========
  Commands:
    punch 
    kick 
    use [item from inventory]
  ''')

  # Create health for both the monster and player
  phealth = 100 
  mhealth = 100

    

  while phealth > 0 and mhealth > 0:
    # Prompt player to perform first fight move
    move = input("Which attack move would you like to do now, think smart\n>").lower().split()

    #get random number between 0 and 100
    rand = random.randrange(0,100)

    # fight conditions :
    if move[0] == "punch" and rand%2 == 0:
      mhealth -= 20 
      print(f"Monster took 20% damage, monster health now is {mhealth}%")
      print(f"Your health is now {phealth}%")
    elif move[0] == "punch" and rand%2 == 1:
      phealth -= 30
      print(f"The monster dodged your punch and hit you with a harder one, you took 30% damage")
      print(f"Your health is now {phealth}%")
      print(f"Monster health is now {mhealth}%")
    elif move[0] == "kick" and rand%2==0:
      mhealth -= 25
      print(f"Monster took 25% damage, monster health now is {mhealth}")
      print(f"Your health is now {phealth}%")
    elif move[0] == "kick" and rand%2 == 1:
      phealth -= 35
      print(f"The monster grabbed your leg and slammed you on the ground pretty hard, you took 50% damage")
      print(f"Your health is now {phealth}%")
      print(f"Monster health is now {mhealth}%")
    elif move[1] == "shotgun" and move[0] == "use":
      if "shotgun" in inventory:
        mhealth -= 60 
        print(f"You shot the monster with a shotgun, leaving him with -60% damage, and monster health is {mhealth}")
        print(f"Your health is now {phealth}%")
        # deletes shotgun from inventory
      else:
        print("You do not have a shotgun in your inventory ")
    elif move[1] == "sword" and move[0] == "use":
      if "sword" in inventory:
        mhealth -= 45 
        print(f"You sliced the monster with a sharp sword, leaving him with -45% damage, and monster health is {mhealth}")
        print(f"Your health is now {phealth}%")
      else:
        print("You do not have a sword in your inventory")
    elif move[1] == "grenade" and move[0] == "use":
      if "grenade" in inventory:
        mhealth -= 80 
        print(f"You threw a grenade and injured the monster pretty bad, leaving him with -80% damage, and monster health is {mhealth}")
        print(f"Your health is now {phealth}%")
      else:
        print("You do not have a grenade in your inventory")
    elif move[0] == "use" and move[1] == "first-aid kit":
      if "first-aid kit" in inventory:
        phealth = 100
        print(f"You have used the first-aid kit and now your health is {phealth}")
        print(f"Monster Health: {mhealth}")
      else:
        print("You do not have a first-aid kit in your inventory")
    else:
      print("Not an attack method")

    # Condition if either health level is below 0
    if mhealth <= 0:
      print("You have defeated the monster, go north to return to hall after your victory")
    elif phealth <=0:
      return False
    print("--------------------------------------------------")
  
  


#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {
            'Bedroom' : {
                  'south' : 'Hall',
                  'east' : 'Closet',
                  'item' : 'sword'
                },

            'Closet' : {
                  'west' : 'Bedroom',
                  'item' : 'grenade'
                },

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'north' : 'Bedroom',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },

            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },

            'Attic' : {
                  'west' : 'Dining Room',
                  'south': 'Garage',
                  'item' : ['shotgun','first-aid kit']
               },

            "Garage" : {
                  'North' : 'Attic',
                  'item' : 'monster'
               },

            'Garden' : {
                  'north' : 'Dining Room'
               },

            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    x = combatMode()
    if x == 0:
      print('A monster has FINISHED you... GAME OVER!')
      break

  
      
      