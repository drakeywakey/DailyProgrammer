# DAILY PROGRAMMER #294

'''
Today's challenge is inspired by the board game Scrabble. Given a set of 7 letter tiles and a word,
determine whether you can make the given word using the given tiles.
Feel free to format your input and output however you like. You don't need to read from your program's input
 if you don't want to - you can just write a function that does the logic. I'm representing a set of tiles as a
  single string, but you can represent it using whatever data structure you want.


examples:
scrabble("ladilmy", "daily") -> true
scrabble("eerriin", "eerie") -> false
scrabble("orrpgma", "program") -> true
scrabble("orppgma", "program") -> false

'''

# Seems simple enough -- let's make a dictionary out of our available tiles --
# Ex 1. 'ladilmy' -->> {l: 2, a: 1, d: 1, i: 1, m: 1, y: 1}
# Then we can loop through all the letters in the desired word and decrement the dictionary at each point
# if there is nothing at that letter, or if the count is down to zero, then false

import json

def can_make_word(counts, word):
	# at each letter in the word, see if our dictionary even has that letter
	# --- if it does, check the how many of that letter we have
	# --- --- if we have more than 0, decrement there and move on
	# --- --- otherwise, we don't have enough letters for this word in our tiles
	# --- otherwise, we don't have enough letters for this word in our tiles

	# don't want alter the actual counts dictionary, so we'll need to use a copy of it
	count_copy = counts.copy()

	# Bonus 3: want to get a score for each letter used, so let's keep track of how many we use,
	# and return that too if we're able to make the word
	letters_used = { '?' : 0 }

	for letter in word:
		if (letter not in letters_used):
			letters_used[letter] = 0

		if (letter in count_copy):
			if (count_copy[letter] > 0):
				count_copy[letter] -= 1
				letters_used[letter] += 1
			elif ('?' in count_copy and count_copy['?'] > 0):
				count_copy['?'] -= 1
				letters_used['?'] += 1
			else:
				return False, letters_used
		else:
			# Bonus:1 allow for the wildcard character '?'
			# Check if we have any wildcards left for use
			# if we do, use one and continue, word is still a valid possibility
			# otherwise, the letter we need wasn't available, and we didn't have any wildcards left
			if ('?' in count_copy and count_copy['?'] > 0):
				count_copy['?'] -= 1
				letters_used['?'] += 1
			else:
				return False, letters_used

	# if we've made it here, we must have enough letters -- True dat
	return True, letters_used

def get_letter_counts(letters):
	counts = {}

	# get a count of how many tiles we have of each letter
	for letter in letters:
		if (letter in counts):
			counts[letter] += 1
		else:
			counts[letter] = 1

	return counts

def scrabble(tiles, word):
	letter_counts = get_letter_counts(tiles)

	return can_make_word(letter_counts, word)

# original examples
print scrabble("ladilmy", "daily")[0] #-> true
print scrabble("eerriin", "eerie")[0] #-> false
print scrabble("orrpgma", "program")[0] #-> true
print scrabble("orppgma", "program")[0] #-> false

# Bonus 1 examples
print scrabble("pizza??", "pizzazz")[0] #-> true
print scrabble("piizza?", "pizzazz")[0] #-> false
print scrabble("a??????", "program")[0] #-> true
print scrabble("b??????", "program")[0] #-> false

# Bonus 2
'''
	Given a set of up to 20 letter tiles, determine the longest word from the enable1 English word list that can be formed using the tiles.
	longest("dcthoyueorza") ->  "coauthored"
	longest("uruqrnytrois") -> "turquois"
	longest("rryqeiaegicgeo??") -> "greengrocery"
	longest("udosjanyuiuebr??") -> "subordinately"
	longest("vaakojeaietg????????") -> "ovolactovegetarian"
	(For all of these examples, there is a unique longest word from the list.
	 In the case of a tie, any word that's tied for the longest is a valid output.)
'''

# There's likely a better way to do this, but for now I think I'll just do it the ol' fashioned way --
# check each word in the dictionary against the tiles we have, and hold onto whichever is the longest.

with open('enable1.txt') as dictionary:
	words = dictionary.read().split()

# finds the longest word in the dictionary that can be made with the given letter tiles
def longest(tiles):
	letter_counts = get_letter_counts(tiles)
	longest = ''

	for word in words:
		if (can_make_word(letter_counts, word)[0] and len(word) > len(longest)):
			longest = word

	return longest

print longest("dcthoyueorza")# ->  "coauthored"
print longest("uruqrnytrois")# -> "turquois"
print longest("rryqeiaegicgeo??")# -> "greengrocery"
print longest("udosjanyuiuebr??")# -> "subordinately"
print longest("vaakojeaietg????????")# -> "ovolactovegetarian"

with open('scores.json') as scoresList:
	scores = json.load(scoresList)

# #print scores
# #print scores["e"]

def get_word_score(letters_used):
	score = 0

	for key in letters_used:
		times = letters_used[key]
		score += scores[key] * times

	return score

def highest(tiles):
	letter_counts = get_letter_counts(tiles)
	highest = ''
	highest_score = 0

	for word in words:
		outcome = can_make_word(letter_counts, word)
		can_make = outcome[0]
		letters_used = outcome[1]
		#word_score = get_word_score(letters_used)

		if (can_make):
			word_score = get_word_score(letters_used)
			#print letter_counts
			#print letters_used
			if (word_score > highest_score):
				highest_score = word_score
				highest = word

	return highest

print highest("dcthoyueorza") # ->  "zydeco"
print highest("uruqrnytrois") # -> "squinty"
print highest("rryqeiaegicgeo??") # -> "reacquiring"
print highest("udosjanyuiuebr??") # -> "jaybirds"
print highest("vaakojeaietg????????") # -> "straightjacketed"



# Intermediate #294 -- scoring based off of position in the word

def highest_two(tiles):
	letter_counts = get_letter_counts(tiles)
	highest = ''
	highest_score = 0

	for word in words:
		reverse = word
		outcome = can_make_word(letter_counts, word)
		can_make = outcome[0]
		letters_used = outcome[1]

		if (can_make):
			word_score = get_word_score_two(word, letters_used)
			if (word_score > highest_score):
				highest_score = word_score
				highest = word

	return highest


### IMPORTANT: to obtain the highest possible score for this word, we actually try to fill the letters
# in reverse order --- if a letter can be used at the end of the string, and a wildcard replace
# that letter earlier, that letter will get a higher score in the later position for this scoring system.
def get_word_score_two(word, letters_used):
	# this assumes we're only calling this because it is in fact possible to make this work with these letters
	used = letters_used.copy()
	score = 0

	for idx, letter in enumerate(word[::-1]):
		# if this is not the case, we must have used a wildcard character at that position -- adds 0, so we ignore
		if (used[letter] > 0):
			used[letter] -= 1
			score += (len(word) - idx) * scores[letter]

	return score

print highest_two("iogsvooely")# -> 44 ("oology")
print highest_two("seevurtfci")# -> 52 ("service")
print highest_two("vepredequi")# -> 78 ("reequip")
print highest_two("umnyeoumcp")# -> ???
print highest_two("orhvtudmcz")# -> ???
print highest_two("fyilnprtia")# -> ???

print highest_two("yleualaaoitoai??????")# -> 171 ("semiautomatically")
print highest_two("afaimznqxtiaar??????")# -> 239 ("ventriloquize")
print highest_two("yrkavtargoenem??????")# -> ???
print highest_two("gasfreubevuiex??????")# -> ???
