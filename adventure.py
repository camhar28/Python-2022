#Import all the functions from adventurelib
from adventurelib import *

#Rooms
Room.items = Bag()

space = Room("You are drifting in space. You see a spaceship")
airlock = Room("You are in an airlock")
cargo = Room("You have entered the cargo bay")
docking = Room("You have entered the docking bay, you see a small shuttle")
hallway = Room("You are in the connector, you can go four ways")
bridge = Room("You are in the Bridge. Flashing lights are everywhere. There is a dead body.")
quarters = Room("You are in the Barracks. There is no-one here. There is a locker in the corner")
mess_hall = Room("You are in the Eating Hall. You see food over the counter")
escape_pods = Room("There are rows of escape pods infront of you. You need a key to access it")

#Room Connections
docking.west = cargo
hallway.north = cargo
hallway.east = bridge
hallway.south = mess_hall
hallway.west = airlock
bridge.south = escape_pods
mess_hall.west = quarters
quarters.north = airlock

#Items
Item.description = ""
Keycard = Item("A red keycard","keycard","card","key","red keycard")
Keycard.description = "You look at the keycard and see that it is labelled escape pod"

note = Item("A scribbled note", "note","paper","code")
note.description = "You look at the note. The numbers 2,3,5,4 are scribbled on it"

#Add items to room
quarters.items.add(note)

#Variables
current_room = space
inventory = Bag()
body_searched = False
used_keycard = False

#Binds
@when("jump")
def jump():
	print("You Jump")

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_airlock():
	global current_room
	if current_room == space:
		print("You haul yourself into the airlock")
		current_room = airlock
	else:
		print("There is no airlock here")


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

@when("look")
def look():
	print(current_room)
	print("There are rooms to the",current_room.exits())
	if len(current_room) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)

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

@when("search body")
@when("look at body")
@when("search man")
def search_body():
	if current_room == bridge:
		print("You search the body and a red keycard falls to the floor")
		current_room.items.add(keycard)
		body_searched = True
	elif current_room == bridge and body_searched == True:
		print("You already searched the body")
	else:
		print("There is no body here")

@when ("use ITEM")
def use(item):
	if item == keycard and current_room == bridge:
		print("You use the keycard and the escape pods open")
		print("The escape pods are to the south")
		used_keycard = True
		bridge.south = escape
	elif used_keycard == True and current_room == bridge:
		print("You have already used the card")
	else:
		print("You can't use that here")

@when("2354")
@when("type 2354")
def escape_pod_win():
	if note in inventory:
		if current_room == escape:
			print("You enter the code and escape. You win")
		else:
			print("There is nowhere to enter the code")
	else:
		print("You don't have the code. You can't just guess it.")

#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE
#ANYTHING BELOW THIS LONEs
#The main function
def main():
	start()
	#Start the main loop
	print(current_room)

main()