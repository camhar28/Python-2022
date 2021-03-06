########################
#IMPORTS
########################
from adventurelib import *

########################
#DEFINE ROOMS
########################
Room.items = Bag()

escape = Room("You have won. Congratulations")
hall1 = Room("There is a long hallway stretching in front of you")
hall2 = Room("There is a long hallway stretching in front of you")
hall3 = Room("There is a long hallway stretching in front of you")
hall4 = Room("There is a long hallway stretching in front of you")
hall5 = Room("There is a long hallway stretching in front of you")
master_Bedroom = Room("There is a large bed in the middle of the room")
ensuite = Room("There is a bathroom here. there is a shower and a clogged toilet")
hidden_Room = Room("")
final_Room = Room("There is a locked case and a locked safe in here. There is a computer in the corner, there is a keyslot in the side of it")


########################
#DEFINE CONNECTIONS
########################
hall1.north = hall5
hall1.east = hall2
hall2.east = hall3
hall3.north = hall4
master_Bedroom.east = hall4
master_Bedroom.west = hall5
master_Bedroom.south = ensuite

########################
#DEFINE ITEMS
########################
Item.description = ""
keycard = Item("A red keycard","keycard","card","key","red keycard")
keycard.description = "You look at the keycard and see that it is labelled hidden_Room"

moneyBag = Item("Moneybag", "bag", "money", "moneybag")
moneyBag.description = "A bag containing a large quantity of money"

plunger = Item("A plunger", "plunger")
plunger.description = "A wooden handle with a black plunger on the end"


########################
#DEFINE BAGS
########################
inventory = Bag()


########################
#ADD ITEMS TO BAGS
########################

ensuite.items.add(plunger)

########################
#DEFINE ANY VARIABLES
########################
current_room = hall1
toilet_unclogged = False 

########################
#BINDS (eg"@when(look)")
########################
@when("look")
def look():
	print(current_room)
	print("There are rooms to the",current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)

@when ("use ITEM")
def use(item):
	if item == "plunger" and current_room == ensuite:
		print("You unclogged the toilet. It was blocked because of a keycard.")
		ensuite.items.add(keycard)
		toilet_unclogged = True
	elif item == "keycard" and current_room == hidden_Room:
		print("you use the card and a door opens to the east")
		hidden_Room.east = final_Room
	elif item == "keycard" and current_room == final_Room:
		print("You use the keycard on the computer and it opens a safe in the wall. A moneybag falls out.")
		print("New objective: Take the moneybag out of the house")
		hall1.south = escape
		final_Room.items.add(moneyBag)
	else:
		print("You can't use that here")

@when("get ITEM")
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
	if item == "keycard" and current_room == final_Room:
		print("you turn the keycard over and it says main computer")
	elif item == "keycard":
		hall4.east = hidden_Room
		t = inventory.find(item)
		print(t.description)
	elif item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying a {item}")

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




########################
#MAIN FUNCTION
########################


def main():
	start()
	#Start the main loop
	print(current_room)

main()