#--------------------------------------------\\
#Dustin Mamer
#Text Based Game
#CS 30 May 20, 2024
#--------------------------------------------//
import random as r
import json
#-------------------------------------------->>
# Functions/Classes
#-------------------------------------------->>
global pickup
pickup = ["C_4", "B_4", "D_3", "C_3", "A_3", "C_2", "B_2","A_2", "C_1"]

global existence
existence = ["C_4", "B_4", "A_4", "D_3", "C_3", "B_3", "A_3", "C_2", "B+2", "A_2", "C_1", "B_1", "A_1"]

global inventory
inventory = {"food": 0, "knife": 0, "med": 0, "health": 3, "key": 0}

class Room():
  '''A class to model a room in the Bunker'''

  def __init__(self, name, description, *doors):
    self.name = name
    self.description = description
    self.doors = doors

  def describe_room(self):
    '''Describes the room that you are currently in.'''
    description = f'{self.description}'
    return description

  def available_doors(self):
    '''Returns the availaible doors in the room'''
    available = f'The availaible doors are: {self.doors}'
    return available


C_4 = Room(
    '\nC_4',
    '\nThere is rust creeping along the sides of the steel bars holding the roof up. Destroyed medical equipment is scattered across the ground and the concrete floors have begun cracking from wear. Cracked cryo pods cover one side of the room, as signs of battle cover the walls. \
Cold air, from the cryo pods, drifts along the hard concrete floor.  On the wall, the letters C_4 are painted blue paint. On one side of the room there is an old door that looks to have been closed for a long time.',
    'B_4')

B_4 = Room(
    '\nB_4',
    '\nThe room seems to be an old office room full of cubicles. The floors are covered with old computers.',
    'C_4', 'A_4')

A_4 = Room(
    '\nA_4',
    '\nThe room is empty, but a set of stairs leads upwards to another floor. ',
    'B_4', 'D_3')

D_3 = Room(
    '\nD_3',
    '\nThe room seems to have been a living room before it was destroyed. A coffee table sits in the middle of the room and a couch is flipped over right on top of it.',
    'A_4', 'B_3')

B_3 = Room(
    '\nB_3',
    '\nThe room is in the shape of an Octagon, and parallel to you, a big screen is mounted on the wall. The big screen is bright red and the word warning is hastily sliding across the screen. To both your left and your right, there is a door leading to another room.',
    'D_3', 'C_3', 'A_3')

C_3 = Room(
    '\nC_3',
    '\nThe room is dimly lit and the walls are covered with computer servers. Three lines of servers sit in the middle of the room and all power still seems functionally.',
    'B_3')

A_3 = Room(
    '\nA_3',
    '\nThe room is well lit with fluorescent lights llining the roof. The room looks to have been used as a security check in for people coming into the control room in B_3. A metal detector is standing in the middle of the room and right beside it is a xray machine for bags that are brought in. The room looks eerily similar to a TSA check in at the airport.',
    'B_3', 'B_2')

B_2 = Room(
    '\nB_2',
    '\nOn one side of the room is a desk where a secretary would usually be seated. A long couch covers another side of the room and on the adjacent wall there is a door with a nameplate that is covered with a sticky black goo. On the final wall of the room, there is another door leading to another room.',
    'C_2', 'A_2')

C_2 = Room(
    '\nC_2',
    '\nYour in an office. Paper covers the floors as filing cabinets are turned over. The desk is still standing and a name plate is shown saying, "MR GUTTERMAN".',
    'B_2')

A_2 = Room(
    '\nA_2',
    '\nAround you is a small room with two elevators on one side of the room. One another side of the room a vending machine is standing there beckoning you to come over.',
    'B_2', 'C_1')

C_1 = Room(
    'C_1',
    '\nAround you is a small room with two elevators on one side of the room. On the opposite side of the room, is a hallway that looks to lead to a lobby of sorts.',
    'A_2', 'B_1')

B_1 = Room(
    'B_1',
    '\nThe room looks similar to a waiting room with a couple of couches and chairs spread out around the room.',
    'C_1', 'A_1')

A_1 = Room(
    'A_1',
    '\nA big vault door blocks your path on one side of the room. A desk covered with papers and computers is facing the vault door. Taking a closer look at the gigantic vault door you notice a small keyhole in the middle of the door.',
    'B_1')

room_list = {
    'C_4': C_4,
    'B_4': B_4,
    'A_4': A_4,
    'D_3': D_3,
    'B_3': B_3,
    'C_3': C_3,
    'A_3': A_3,
    'B_2': B_2,
    'C_2': C_2,
    'A_2': A_2,
    'C_1': C_1,
    'B_1': B_1,
    'A_1': A_1
}


class Supplies():
  '''defines the supplies that you have in your inventory'''

  def __init__(self, inventory):
    self.inventory = inventory

  def check_supplies(self, inventory):
    '''Checks how much food, knives and med packs you have.'''
    print(" ")
    print(inventory)

  def use_food(self, inventory):
    '''Subtracts the food when you move between rooms.'''
    if inventory["food"] > 0:
      print("\nYou have consumed one food. -1 food\n")
      inventory['food'] = inventory['food'] - 1
    else:
      if inventory["health"] > 1:
        print("You have no food left, and as a result have lost 1 health")
        inventory['health'] = inventory['health'] - 1
      else:
        print("You have died! :(")
        exit()

  def use_med(self, inventory):
    '''Removes a Med-pack to restore one health.'''
    if inventory['health'] > 2:
      print("\nYou are at full health")
    else:
      if inventory['med'] > 0:
        inventory['med'] = inventory['med'] - 1
        inventory['health'] = inventory['health'] + 1
        print(f'You are at ', inventory['health'], ' Hp')
      else:
        print("You have no med packs left!\n")

  def search(self):
    '''Searches the room for items.'''
    if player_room == C_4:
      '''Checks what room the player is in.'''
      if "C_4" in pickup:
        '''Checks if player has already searched this room'''
        print("You have found five cans of soup")
        inventory['food'] = inventory['food'] + 5
        print("You have found five knives")
        inventory['knife'] = inventory['knife'] + 5
        print("You have found One Med-pack")
        inventory['med'] = inventory['med'] + 1
        pickup.remove("C_4")

      else:
        print("This room has nothing left ot be salvaged")

    elif player_room == B_4:
      if "B_4" in pickup:
        print("You have found a knife")
        inventory['knife'] = inventory["knife"] + 1
        print("You have found a Med-pack")
        inventory['med'] = inventory['med'] + 1
        pickup.remove("B_4")

      else:
        print("This room has nothing left to be salvaged")

    elif player_room == A_4:
      print(
          "The room is empty, but a set of stairs leads upwards to another floor. "
      )

    elif player_room == D_3:
      if "D_3" in pickup:
        print("You have found three cans of soup")
        inventory['food'] = inventory['food'] + 3
        print("You have found two knives")
        inventory['knife'] = inventory['knife'] + 2
        pickup.remove("D_3")

      else:
        print("This room has nothing left to be salvage.")

    elif player_room == B_3:
      print("The room has nothing that you can salvage.")

    elif player_room == C_3:
      if "C_3" in pickup:
        print("You have found three cans of soup")
        inventory["food"] = inventory["food"] + 3
        print("You have found Five knives")
        inventory["knife"] = inventory["knife"] + 5
        print("You have found One Med-pack")
        inventory["med"] = inventory["med"] + 1
        pickup.remove("C_3")

      else:
        print("This room has nothing left to be salvaged.")

    elif player_room == A_3:
      if "A_3" in pickup:
        print("You have found three cans of soup")
        inventory["food"] = inventory["food"] + 3
        print("You have found a knife")
        inventory["knife"] = inventory["knife"] + 1
        pickup.remove("A_3")

      else:
        print("This room has nothing left to be salvaged.")

    elif player_room == B_2:
      if "B_2" in pickup:
        print("You have found three cans of soup")
        inventory["food"] = inventory["food"] + 3
        pickup.remove("B_2")

    elif player_room == C_2:
      if "C_2" in pickup:
        print("You have found a knife.")
        inventory["knife"] = inventory["knife"] + 1
        print("You have found a Med-pack")
        inventory["med"] = inventory["med"] + 1
        print(" ")
        print("You have found a key.")
        print("This key will be useful later on.")
        inventory["key"] = inventory["key"] + 1
        pickup.remove("C_2")

      else:
        print("This room has nothing left to be salvaged.")

    elif player_room == A_2:
      if "A_2" in pickup:
        print("You have found two cans of soup")
        inventory["food"] = inventory["food"] + 2
        print("You have found a knife")
        inventory["knife"] = inventory["knife"] + 1
        pickup.remove("A_2")

      else:
        print("This room has nothing left to be salvaged.")
        
    elif player_room == C_1:
      if "C_1" in pickup:
        print("You have found two cans of soup")
        inventory["food"] = inventory["food"] + 2
        print("You have found a knife")
        inventory["knife"] = inventory["knife"] + 1
        print("You have found two Med-pack")
        inventory["med"] = inventory["med"] + 2
        pickup.remove("C_1")
      else:
        print("This room has nothing left to be salvaged.")
        
    elif player_room == B_1:
      if "B_1" in pickup:
        print("You have found three cans of soup")
        inventory["food"] = inventory["food"] + 3
        pickup.remove("B_1")
      else:
        print("This room has nothing left to be salvaged.")
        
    elif player_room == A_1:
      print("This room has nothing for you to salvage.")


#---------------------------------------------------------------------------------|

class Events():
  '''Defines the Events that will occur during your adventure.'''

  def __init__(self, inventory):
    self.inventory = inventory

  def low_level_attack(self, inventory):
    '''An easy attack that has a great chance to occur when going into a room for the first time.'''
    if r.randint(1, 10) == 1:
      if inventory['health'] > 1:
        print("You have been attacked by a small radioactive rat and have incurred a minor injury. -1 Hp")
        inventory['health'] = inventory['health'] - 1

      else:
        print("You have been attacked by a small radioactive rat and have incurred a minor injury. -1 Hp")
        print("\nYou have died! :(\n")
        exit()

    if r.randint(1, 100) == 1:
      if inventory['health'] > 2:
        print("You have been attacked by a small radioactive rat and have incurred a major injury. -2 Hp")
        inventory['health'] = inventory['health'] - 2

      else:
        print("You have been attacked by a small radioactive rat and have incurred a major injury. -2 Hp")
        print("\nYou have died! :(\n")
        exit()

    if r.randint(1, 1000) == 1:
      print("You have been attacked by a small radioactive rat and have incurred a deathly injury. -3 Hp. You have died!")
      exit()

    if inventory['knife'] > 0:
      print("You were attacked by a small radioactive rat and were able to kill the rat with a knife. -1 knife")
      inventory['knife'] = inventory['knife'] - 1

    else:
      if inventory['health'] > 1:
        print("You were attacked by a small radioactive rat and were able to kill the rat with your bare hands. -1 Hp")
        inventory['health'] = inventory['health'] - 1

      else:
        print("You were attacked by a small radioactive rat and were able to kill the rat with your bare hands. But you later succumbed to your injuries.")
        print("You have died! :(")
        exit()

  def mid_level_attack(self, inventory):
    '''A medium attack that has a medium chance to occur when going into a room for the first time.'''
    if r.randint(1, 4) == 1:
      if inventory['health'] > 1:
        print("You have been attacked by a Big radioactive rat and have incurred a minor injury. -1 Hp")
        inventory['health'] = inventory['health'] - 1

      else:
        print("You have been attacked by a Big radioactive rat and have incurred a minor injury. -1 Hp")
        print("You have died! :(")
        exit()

    if r.randint(1, 20) == 1:
      if inventory['health'] > 2:
        print("You have been attacked by a Big radioactive rat and have incurred a major injury. -2 Hp")
        inventory['health'] = inventory['health'] - 2

      else:
        print("You have been attacked by a Big radioactive rat and have incurred a major injury. -2 Hp")
        print("You have died! :(")
        exit()

    if r.randint(1, 100) == 1:
      print("You have been attacked by a Big radioactive rat and have incurred a deathly injury. -3 Hp. You have died!")
      exit()

    if inventory['knife'] > 1:
      print("You were attacked by a Big radioactive rat and were able to kill the rat with two knives. -2 knife")
      inventory['knife'] = inventory['knife'] - 2

    elif inventory['knife'] == 1:
      if inventory['health'] > 1:
        print("You were attacked by a Big radioactive rat and were able to kill the rat with a knife and your bare hands. -1 knife, -1 Hp")
        inventory['knife'] = inventory['knife'] - 1
        inventory['health'] = inventory['health'] - 1
      else:
        print("You were attacked by a Big radioactive rat and were able to kill the rat with a knife and your bare hands. But you later succumbed to your injuries.")
        print("You have died! :(")
        exit()

    else:
      if inventory['health'] == 3:
        print("You were attacked by a Big radioactive rat and were able to kill the rat with your bare hands. -2 Hp")
        inventory['health'] = inventory['health'] - 2

      else:
        print("You were attacked by a Big radioactive rat and were able to kill the rat with your bare hands. But you later succumbed to your injuries.")
        print("You have died! :(")
        exit()

  def high_level_attack(self, inventory):
    '''A hard attack that has a low chance to occur when going into a room for the first time.'''
    if r.randint(1, 2) == 1:
      if inventory['health'] > 1:
        print("You have been attacked by a Big Radioactive Feral Raccoon and have incurred a minor injury. -1 Hp")
        inventory['health'] = inventory['health'] - 1

      else:
        print("You have been attacked by a Big Radioactive Feral Raccoon and have incurred a minor injury. -1 Hp")
        print("You have died! :(")
        exit()

    if r.randint(1, 5) == 1:
      if inventory['health'] > 2:
        print("You have been attacked by a Big Radioactive Feral Raccoon and have incurred a major injury. -2 Hp")
        inventory['health'] = inventory['health'] - 2

      else:
        print("You have been attacked by a Big Radioactive Feral Raccoon and have incurred a major injury. -2 Hp")
        print("You have died! :(")
        exit()

    if r.randint(1, 20) == 1:
      print("You have been attacked by a Big Radioactive Feral Raccoon and have incurred a deathly injury. -3 Hp. You have died!")
      exit()
      
    if inventory['knife'] > 2:
      print("You were attacked by a Big Radioactive Feral Raccoon and were able to kill the raccoon with three knives. -3 knife")
      inventory['knife'] = inventory['knife'] - 3

    elif inventory['knife'] == 2:
      if inventory['health'] > 1:
        print("You were attacked by a Big Radioactive Feral Raccoon and were able to kill the raccoon with two knives and your bare hands. -2 knife, -1 Hp")
        inventory['knife'] = inventory['knife'] - 2
        inventory['health'] = inventory['health'] - 1
      else:
        print("You were attacked by a Big Radioactive Feral Raccoon and were able to kill the raccoon with two knives and your bare hands. But you later succumbed to your injuries.")
        print("You have died! :(")
        exit()

    elif inventory['knife'] == 1:
      if inventory['health'] > 2:
        print("You were attacked by a Big Radioactive Feral Raccoon and were able to kill the raccoon with one knife and your injured bare hands. -1 knife, -2 Hp")
        inventory['knife'] = inventory['knife'] - 1
        inventory['health'] = inventory['health'] - 2
      else:
        print("You were attacked by a Big Radioactive Feral Raccoon and were able to kill the raccoon with one knife and your injured bare hands. But you later succumbed to your injuries.")
        print("You have died! :(")
        exit()
    else:
      print("You were attacked by a Big Radioactive Feral Raccoon and were sadly killed by the Big Radioactive Feral Raccoon.")
      print("You have died! :(")
      exit()

  def encounter_percentage(self):
    '''Randomly chooses an event that will occur during your adventure.'''
    blag = r.randint(1, 5)
    loot = r.randint(1, 7)
    event = r.randint(1, 10)
    if blag == 1:
      pass
    elif blag == 2 or blag == 3 or blag == 4:
      if event == 1 or event == 3 or event == 5 or event == 7 or event == 9:
        self.low_level_attack(inventory)
      elif event == 2 or event == 4 or event == 6 or event == 8:
        self.mid_level_attack(inventory)
      elif event == 10:
        self.high_level_attack(inventory)
    elif blag == 5:
      if loot == 1:
        print("You were lucky and have found a can of soup.")
        inventory["food"] = inventory["food"] + 1
      elif loot == 2:
        print("You were lucky and have found a knife")
        inventory['knife'] = inventory['knife'] + 1
      elif loot == 3:
        print("You were lucky and have found a Med-pack")
        inventory['med'] = inventory['med'] + 1
      else:
        pass
      

  def vending_machine(self, inventory):
    '''Allows you to exchange food and med packs from the vending machine.'''
    buy = input("What would you like to buy? \n1. Food \n2. knife \n3. Med-pack \n4. Exit \n")
    if buy == "1":
      confirm = input("\nAre you sure you want to buy +1 food for -2 knife? (y/n)")
      if confirm == "y":
        print("\norder has been confirmed!\n")
        print("You deposited two knives")
        inventory["knife"] = inventory["knife"] - 2
        print("You obtained one can of soup")
        inventory["food"] = inventory["food"] + 1
      elif confirm == "n":
        print("Order has been cancelled.")
        pass
      else:
        print("Invalid input")
        pass

    elif buy == "2":
      confirm = input("\nAre you sure you want to buy +2 knife for -1 food? (y/n)")
      if confirm == "y":
        print("\norder has been confirmed!\n")
        print("You deposited one food")
        inventory["food"] = inventory["food"] - 1
        print("You obtained two knives")
        inventory["knife"] = inventory["knife"] + 2
      elif confirm == "n":
        print("Order has been cancelled.")
        pass
      else:
        print("Invalid input")
        pass

    elif buy == "3":
      confirm = input("\nAre you sure you want to buy +1 Med-pack for -1 food & -1 knife? (y/n)")
      if confirm == "y":
        print("\norder has been confirmed!\n")
        print("You deposited one food")
        inventory["food"] = inventory["food"] - 1
        print("You deposited one knife")
        inventory['knife'] = inventory['knife'] - 1
        print("You obtained one Med-pack")
        inventory['med'] = inventory['med'] + 1

    elif buy == '4':
      print("You have exited the vending machine")
      pass

    else:
      print("Invalid input")
      pass

  def end_event(self, inventory):
    '''An event at the end where the player finds the exit to the Bunker.'''
    if inventory["key"] > 0:
      print(" \n")
      print("You insert the key into the keyhole on the bunker door and turn it. \n \nThe door begins to creek as it slowly opens. Dust and dirt falls from the ceiling and onto the floor. \nAs the doors open you see the sun emerging from the horizon.")
      print("\nYou have successfully escaped the bunker!")
      exit()
    else:
      print("\nYou do not have the key to the bunker door.")
      print("\nYou'll probably find the key someplace in the bunker.\n")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

global player_room
player_room = C_4
supplies = Supplies(inventory)
print(" ______     ______     ______     ______     ______   ______  ")
print("/\  ___\   /\  ___\   /\  ___\   /\  __ \   /\  == \ /\  ___\     ")
print("\ \  __\   \ \___  \  \ \ \____  \ \  __ \  \ \  _-/ \ \  __\     ")
print(" \ \_____\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_\    \ \_____\   ")
print("  \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/     \/_____/   ")
print(" ______   ______     ______     __    __                          ")
print('/\  ___\ /\  == \   /\  __ \   /\ "-./  \                         ')
print("\ \  __\ \ \  __<   \ \ \/\ \  \ \ \-./\ \                        ")
print(" \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \ \_\                       ")
print("  \/_/     \/_/ /_/   \/_____/   \/_/  \/_/                       ")
print(" ______     __  __     __   __     __  __     ______     ______   ")
print('/\  == \   /\ \/\ \   /\ "-.\ \   /\ \/ /    /\  ___\   /\  == \  ')
print('\ \  __<   \ \ \_\ \  \ \ \-.  \  \ \  _"-.  \ \  __\   \ \  __<  ')
print(' \ \_____\  \ \_____\  \ \_\\"\ _\  \ \_\ \_\  \ \_____\  \ \_\ \_\ ')
print("  \/_____/   \/_____/   \/_/ \/_/   \/_/\/_/   \/_____/   \/_/ /_/")
print(" ")

print("You wake up out of a cryo pod and find yourself someplace underground. You have no idea where you are or how you got here.")
print(" ")
global events
events = Events(inventory)

while True:
  if player_room == C_4:
    if "C_4" in existence:
      existence.remove("C_4")
    else:
      print("You have previously visited room C_4")
    print("\nYou are in room C_4.")
  elif player_room == B_4:
    if "B_4" in existence:
      existence.remove("B_4")
    else:
      print("You have previously visited room B_4")
    print("\nYou are in room B_4.")
  elif player_room == A_4:
    if "A_4" in existence:
      existence.remove("A_4")
    else:
      print("You have previously visited room A_4")
    print("\nYou are in room A_4.")
  elif player_room == D_3:
    if "D_3" in existence:
      existence.remove("D_3")
    else:
      print("You have previously visited room D_3")
    print("\nYou are in room D_3.")
  elif player_room == B_3:
    if "B_3" in existence:
      existence.remove("B_3")
    else:
      print("You have previously visited room B_3")
    print("\nYou are in room B_3.")
  elif player_room == C_3:
    if "C_3" in existence:
      existence.remove("C_3")
    else:
      print("You have previously visited room C_3")
    print("\nYou are in room C_3.")
  elif player_room == A_3:
    if "A_3" in existence:
      existence.remove("A_3")
    else:
      print("You have previously visited room A_3")
    print("\nYou are in room A_3.")
  elif player_room == B_2:
    if "B_2" in existence:
      existence.remove("B_2")
    else:
      print("You have previously visited room B_2")
    print("\nYou are in room B_2.")
  elif player_room == C_2:
    if "C_2" in existence:
      existence.remove("C_2")
    else:
      print("You have previously visited room C_2")
    print("\nYou are in room C_2.")
  elif player_room == A_2:
    if "A_2" in existence:
      existence.remove("A_2")
    else:
      print("You have previously visited room A_2")
    print("\nYou are in room A_2.")
  elif player_room == C_1:
    if "C_1" in existence:
      existence.remove("C_1")
    else:
      print("You have previously visited room C_1")
    print("\nYou are in room C_1.")
  elif player_room == B_1:
    if "B_1" in existence:
      existence.remove("B_1")
    else:
      print("You have previously visited room B_1")
    print("\nYou are in room B_1.")
  elif player_room == A_1:
    print("\nYou are in room A_1.")
    if "A_1" in existence:
      existence.remove("A_1")
    else:
      print("You have previously visited room A_1")

  print(player_room.describe_room())
  print(" ")
  
  if player_room == A_2:
    command = input("What would you like to do:  \n(m) move room, \n(s) search room, \n(u) use Med-pack, \n(i) inventory, \n(v) vending machine, \n(q) quit game, \n(h) help\n\n")

  elif player_room == A_1:
    command = input("What would you like to do:  \n(m) move room, \n(s) search room, \n(u) use Med-pack, \n(i) inventory, \n(k) insert key, \n(q) quit game, \n(h) help\n\n")

  else:
    command = input(
        "What would you like to do:  \n(m) move room, \n(s) search room, \n(u) use Med-pack, \n(i) inventory, \n(q) quit game, \n(h) help\n\n"
    )
  command = command.lower()
  if command == 'm':
    print(player_room.available_doors())
    room_sel = input(f'Where would you like to go? You are going to ')
    room_sel = room_sel.upper()
    # Check if the input is valid
    if room_sel in player_room.doors:
      supplies.use_food(inventory)
      player_room = room_list[room_sel]
      events.encounter_percentage()
    else:
      print("\nInvalid input. Please choose a valid direction.\n")

  elif command == 's':
    print(" ")
    supplies.search()
    print(" ")

  elif command == 'v':
    if player_room == A_2:
      print("\nYou have entered the vending machine\n")
      events.vending_machine(inventory)
      print(" ")
    else:
      print("\nStop cheating by looking at the code!!!\n")

  elif command == 'u':
    supplies.use_med(inventory)
    print(" ")

  elif command == 'i':
    supplies.check_supplies(inventory)
    print(" ")

  elif command == 'k':
    if player_room == A_1:
      events.end_event(inventory)
    else:
      pass

  elif command == 'q':
    print("\nYou have quit the game\n")
    exit()

  elif command == 'h':
    '''Prints the json file that contains the instructions for the game.'''
    with open('instructions.json', 'r') as f_ins:
      instruction = json.load(f_ins)
      print(instruction)
  else:
    print("\nInvalid input. Please choose a valid option.\n")
  print("|----------------------------------------------------------------------|\n")