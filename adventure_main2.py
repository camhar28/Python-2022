########################
#IMPORTS
########################
from adventurelib import *

########################
#DEFINE ROOMS
########################
Room.items = Bag()

Hall1 = Room("There is a long hallway stretching in front of you")
Hall2 = Room("There is a long hallway stretching in front of you")
Hall3 = Room("There is a long hallway stretching in front of you")
Hall4 = Room("There is a long hallway stretching in front of you")
Hall5 = Room("There is a long hallway stretching in front of you")
Master_Bedroom = Room("There is a large bed in the middle of the room")
Ensuite = Room("There is a bathroom here. there is a shower and a clogged toilet, there is a plunger on the floor")
Hidden_Room = Room("There is a vault, it requires a passcode")
Final_Room = Room("There is a locked case and a locked safe in here. There is a computer in the corner, there is a keyslot in the side of it")


########################
#DEFINE CONNECTIONS
########################
Hall1.north = Hall5
Hall1.east = Hall2
Hall2.east = Hall3
Hall3.north = Hall4
Master_Bedroom.east = Hall4
Master_Bedroom.west = Hall5
Master_Bedroom.south = Ensuite




########################
#DEFINE ITEMS
########################
Item.description = ""
Keycard = Item("A red keycard","keycard","card","key","red keycard")
Keycard.description = "You look at the keycard and see that it is labelled Main Computer"

MoneyBag = Item("Moneybag, bag, money")
MoneyBag.description = "A bag containing a large quantity of money"

Plunger = Item("A plunger", "plunger")
Plunger.description = "A wooden handle with a black plunger on the end"


########################
#DEFINE BAGS
########################
inventory = Bag()


########################
#ADD ITEMS TO BAGS
########################

Ensuite.items.add(Plunger)

########################
#DEFINE ANY VARIABLES
########################
current_room = Hall1
toilet_unclogged = False 

########################
#BINDS (ed"@when(look)")
########################
@when("look")
def look():
	print(current_room)
	print("There are rooms to the",current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)

@when("jump")
def jump():
	print("You Jump")

@when("DIRECTION")
@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#Checks if the current room list of exits has
		#The direction the player wants to go
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You can't go that way")


@when("get Item")
@when("take ITEM")
@when("pick up ITEM")
def get_item(item):
	#check if item is in room
	#take it out of room
	#put into inventory
	#otherwise tell user there is no item
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You picked up the {item}")
	else:
		print(f"You don't see a {item}")


@when("inventory")
def check_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying a {item}")




########################
#MAIN FUNCTION
########################


def main():
	start()
	#Start the main loop
	print(current_room)

main()