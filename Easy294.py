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

	# at each letter in the word, see if our dictionary even has that letter
	# --- if it does, check the how many of that letter we have
	# --- --- if we have more than 0, decrement there and move on
	# --- --- otherwise, we don't have enough letters for this word in our tiles
	# --- otherwise, we don't have enough letters for this word in our tiles
	for letter in word:
		if (letter in letter_counts):
			if (letter_counts[letter] > 0):
				letter_counts[letter] -= 1
			else:
				return False
		else:
			return False

	# if we've made it here, we must have enough letters -- True dat
	return True

print scrabble("ladilmy", "daily") #-> true
print scrabble("eerriin", "eerie") #-> false
print scrabble("orrpgma", "program") #-> true
print scrabble("orppgma", "program") #-> false
