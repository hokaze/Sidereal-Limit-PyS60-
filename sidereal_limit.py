#!/usr/bin/env python2
# Sidereal Limit "Hubristic Destiny" generator #

import random, sys, os

def FileRead(filename):
	# Cross-platform way of finding the absolute path of this script,
	# used to ensure odd platforms like symbian open files correctly
	path = os.path.abspath(os.path.dirname(sys.argv[0]))
	# Actual file reading
	f = open(os.path.join(path, filename), "r")
	lines = [line.rstrip('\n') for line in f]
	f.close()
	return lines

def RollOptions(choices):
	option = random.choice(choices).split()
	
	# Re-roll options which append
	if option[0] == "reroll+":
		append = option[1:]
		# re-roll, but ignoring the re-roll options for sake of sanity
		option = choices[random.randint(0,11)].split() + append
		
	# Re-roll options which alter segments
	elif option[0] == "reroll-":
		alter = option[1:]
		option = choices[random.randint(0,11)].split()
		if alter[0] == "start":
			option[0] = str(alter[1])
		elif alter[0] == "end":
			option[1] = str(alter[1])
			option[2] = str(alter[2])
			
	return option

options = FileRead("options.txt")
place = FileRead("places.txt")
person = FileRead("people.txt")
item = FileRead("items.txt")
group = FileRead("groups.txt")
date = FileRead("dates.txt")
action = FileRead("actions.txt")
fatelist = ["place", "person", "item", "group", "date", "action"]

destiny = RollOptions(options)
fateform = ""

for word in destiny:
	fateform += word + " "
print "Your destiny has took the format of:", fateform

i = 0
flawedfate = ""

for word in destiny:
	if word in fatelist:
		destiny[i] = random.choice(eval(word))
	flawedfate += destiny[i] + " "
	i += 1
		
print "For the good of Creation: ", flawedfate