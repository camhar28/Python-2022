#Question 1
icecreams = int(input("How many icecreams do you need.\n"))

if icecreams > 20:
	print("There isn't enough icecreams for you")
else:
	print("We can do that")

#Question 2
travel_distance = int(input("How far are you going to travel.\n"))

if travel_distance > 200:
	print("Remeber to get some petrol")
else:
	print("Safe Travels")

#Question 3 
age = int(input("What is your age\n"))

if age >= 18:
	print("You are an adult")
else:
	print("Child, LOL")

#Question 4
fav_movie = input("What is your favorite movie?\n")

if fav_movie == "Lord Of The Rings":
	print("I agree, any other movie is crap")
else:
	print("Lord Of The Rings is clear.")

#Question 5
The_Tragedy = input("Did you ever hear the tragedy of Darth Plagueis The Wise\n")

if The_Tragedy == "no":
	print("I thought not, Its not a story the Jedi would tell you")
else:
	print("Oh, really, I didn't think anyone else did.")

#Question 6
Mel_Gibson = input("Who directed Passion of the Christ\n").lower()

if Mel_Gibson == "mel gibson":
	print("How'd ya know")
else:
	print("WRONG")
