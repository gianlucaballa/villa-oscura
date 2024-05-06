# To interact with the interpreter (e.g.: exit game).
import sys

# Instructions that players can access throughout the game.
instructions = '''
-----------------------------------------------
INSTRUCTIONS:
Solve the mystery in the villa!
There is no saving. Complete the adventure in one go.
Close the terminal to exit the game.

Traits (max 3 points each)
- Body: it measures your resistance and strength.
- Spirit: it measures your willpower and wisdom.
- Luck: it measures how easily you escape dangers.
- Health: start with 3. If 0, the game is over.

Actions
In order to perform an action, an invisible die is rolled.
The result of this roll + your specific Trait for that action
must beat an established difficulty.

Example: Breaking a window is based on Body. 
Let's imagine that the die roll is 3. 
The difficulty for this action is 5.
If you have at least 2 in Body, you succeed in the action 
(3 + 2 >= 5).

The game does not allow re-rolls so be careful!
Almost all actions are irreversible.

Available actions 
(associate these with environments and objects:
for example, WALK FOREST to walk into the forest) 

WALK: to approach objects and places.
USE: to use objects.
FORCE: to force a physical action.
EXAMINE: to investigate. Add AROUND for surroundings.
ITEM: to check what you carry in your backpack.
INS: for game instructions.
TRAIT: to check your current Traits.
DESC: to re-read descriptions of where the player is.
(cap is not necessary)
-----------------------------------------------
'''

# Traits and inventory system.
traits_dic = {'Body': 0, 'Spirit': 0, 'Luck': 0, 'Health': 3}
inventory_set = {'flashlight'}

# Conditions for the Traits.

# No Health (Game Over).
if traits_dic['Health'] == 0:
	print('''
	The adventure has worn you out. Time to go home.
	   
	GAME OVER
	   
	PS: Why don't you try again later?
	   
	''')
	sys.exit()

# Limit value for Traits. Set the minimum in between 2 values.
max_value = 3
for trait, value in traits_dic.items():
	traits_dic[trait] = min(value, max_value)

# Introduction text.
print('''
-----------------------------------------------
Welcome to Villa Oscura! A game made in Python.

Type INS to learn how to play.
Type TRAIT to see your Traits.
Type ITEM to check your inventory.
(cap is not necessary)
-----------------------------------------------
''')

# Introduction loop.
while True:
	introduction_input = input('Ready to start? ').upper()
	if introduction_input == 'INS':
		print(instructions)
	elif introduction_input == 'TRAIT':
		print()
		# Print dictionary in the same order as it was defined.
		for trait, value in traits_dic.items():
			print(trait + ':', value)
		print()
	elif introduction_input == 'ITEM':
		print()
		print('Inventory:')
		for item in inventory_set:
			print('-', item)
		print()
	elif introduction_input != 'YES' and introduction_input != 'Y' and introduction_input != 'YEAH':
		print('Invalid input.')
		print()
		continue
	else:
		break

# Spending points for Traits.
print('''
-----------------------------------------------
Good! You're passionate about mysteries.
There is an old house in town known as "Villa Oscura".
Legends tell of a murder happened in the house before you were born.
It has been abandoned since then and you have decided to explore it.
	  
It's a spring evening. A soft wind caresses you as you approach the house.
No sound comes from it. You're alone.
	  
But, before you start exploring it...
	  
Spend 3 points in between Body, Spirit and Luck!
Remember: you cannot go higher than 3 for each Trait.
-----------------------------------------------
''')

while True:
	try:
		Body_starting = int(input('Body: type a number '))
		print('Body:', Body_starting)
	except:
		print('Invalid input.')
		print()
		continue
	try:
		Spirit_starting = int(input('Spirit: type a number '))
		print('Spirit:', Spirit_starting)
	except:
		print('Invalid input.')
		print()
		continue
	try:
		Luck_starting = int(input('Luck: type a number '))
		print('Luck:', Luck_starting)
	except:
		print('Invalid input.')
		print()
		continue
	if Body_starting + Spirit_starting + Luck_starting != 3:
		print()
		print(Body_starting + Spirit_starting + Luck_starting, 'points spent.')
		print('You must spend 3 points.')
		print()
		continue
	print()
	while True:
		instructions_traits_points = input('Success! Type INS for help or press a button. ').upper()
		if instructions_traits_points == 'INS':
			print(instructions)
			break
		else:
			print()
			break
	question_traits_points = input('Confirm points? ').upper()
	if question_traits_points == 'YES' or question_traits_points == 'Y' or question_traits_points == 'YEAH':
		break
	elif question_traits_points == 'NO' or question_traits_points == 'N':
		print()
		continue
	else:
		print('Invalid input. Please, re-spend 3 points and confirm.')
		print()
		continue

# Updated Traits.
traits_dic['Body'] = Body_starting
traits_dic['Spirit'] = Spirit_starting
traits_dic['Luck'] = Luck_starting

print()
print('''
-----------------------------------------------
Congratulations! 
These are your Traits:
''')
for trait, value in traits_dic.items():
	print(trait + '->', value)
print()
print('Check them with TRAIT.')

# Block 1: entering the house.
description_entrance = ('''
-----------------------------------------------
	   
You are in front of the entrance door: 
dark rotten wood, sturdy. No signs on it.
	  
It's locked, as you imagined.
	  
No one is around. 
The sun has disappeared behind the house's sharp roof.
There is still light though.

Your turn...
''')

print(description_entrance)

while True:
	entrance_input = input('> ').upper()
	# Actions to examine the situation (they do not move the story forward).
	if entrance_input == 'INS':
		print(instructions)
	elif entrance_input == 'DESC':
		print(description_entrance)
	elif entrance_input == 'TRAIT':
		print()
		for trait, value in traits_dic.items():
			print(trait + ':', value)
		print()
	elif entrance_input == 'ITEM':
		print()
		print('Inventory:')
		for item in inventory_set:
			print('-', item)
		print()
	elif 'EXAMINE' in entrance_input and 'DOOR' in entrance_input:
		print('''The door's hinges are rusty and worn out...''')
		print()
	elif entrance_input == 'EXAMINE':
		print('''What to examine? Remember, type action + object/environment''')
		print()
	elif 'EXAMINE' in entrance_input and 'FLASHLIGHT' in entrance_input:
		print('''It's a common flashlight. No use here.''')
		print()
	elif 'EXAMINE' in entrance_input and 'HINGES' in entrance_input or 'HINGE' in entrance_input:
		print('''With a good push they might fall off...''')
		print()
	elif 'EXAMINE' in entrance_input and 'AROUND' in entrance_input:
		print('''On your left, there is a small square window with cracked glass.''')
		print()
	elif entrance_input == 'USE':
		print('''Use what? Remember, type action + object/environment''')
		print()
	elif 'USE' in entrance_input and 'FLASHLIGHT' in entrance_input:
		print('''No point in doing that.''')
		print()
	elif 'USE' in entrance_input and 'DOOR' in entrance_input:
		print('''You try to push the door open but it's locked.''')
		print()
	elif entrance_input == 'FORCE':
		print('''Force what? Remember, type action + object/environment''')
		print()
	
	# Actions that move the story forward.
	elif 'WALK' in entrance_input and 'WINDOW' in entrance_input:	
		print(
'''The window's shattered glass has the shape of sharp teeth anchored to the wooden frame. 
You might try to pass through it, if those pointy teeth do not bother you!''')
		print()	
	elif 'FORCE' in entrance_input and 'DOOR' in entrance_input:
		qst_force_entrance = input('''Have you considered all? Are you sure about this? ''')	
		if qst_force_entrance == 'YES' or qst_force_entrance == 'Y' or qst_force_entrance == 'YEAH':
			break
		else:
			continue
	
	
	else:
		print('''Invalid input.''')
		continue

	
	


