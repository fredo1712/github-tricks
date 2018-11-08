lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
players = [
	{'name':'Robert',
	'numbers':{21,17,5,8,1}
	},
	{'name':'Fred',
	'numbers':{11,10,22,13,8,34,56,21}
	}
]

print(players[0]['name'])

number_correct_player1 = len(lottery_numbers.intersection(players[0]['numbers']))
number_correct_player2 = len(lottery_numbers.intersection(players[1]['numbers']))

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers. We still cannot use f-strings in this exercise.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

print ('Player ' + players[0]['name'] + ' got ' + str(number_correct_player1) + ' numbers right.')
print ('Player ' + players[1]['name'] + ' got ' + str(number_correct_player2) + ' numbers right.')
