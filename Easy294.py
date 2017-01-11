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
			elif ('?' in letter_counts and letter_counts['?'] > 0):
				letter_counts['?'] -= 1
			else:
				return False
		else:
			# Bonus:1 allow for the wildcard character '?'
			# Check if we have any wildcards left for use
			# if we do, use one and continue, word is still a valid possibility
			# otherwise, the letter we need wasn't available, and we didn't have any wildcards left
			if ('?' in letter_counts and letter_counts['?'] > 0):
				letter_counts['?'] -= 1
			else:
				return False

	# if we've made it here, we must have enough letters -- True dat
	return True

# original examples
#print scrabble("ladilmy", "daily") #-> true
#print scrabble("eerriin", "eerie") #-> false
#print scrabble("orrpgma", "program") #-> true
#print scrabble("orppgma", "program") #-> false

# Bonus 1 examples
#print scrabble("pizza??", "pizzazz") #-> true
#print scrabble("piizza?", "pizzazz") #-> false
#print scrabble("a??????", "program") #-> true
#print scrabble("b??????", "program") #-> false

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

enable1 = open('./enable1.txt')
words = enable1.read().split()

# finds the longest word in the dictionary that can be made with the given letter tiles
def longest(tiles):
	longest = ''

	for word in words:
		if (scrabble(tiles, word) and len(word) > len(longest)):
			longest = word

	return longest

print longest("dcthoyueorza")# ->  "coauthored"
print longest("uruqrnytrois")# -> "turquois"
print longest("rryqeiaegicgeo??")# -> "greengrocery"
print longest("udosjanyuiuebr??")# -> "subordinately"
print longest("vaakojeaietg????????")# -> "ovolactovegetarian"

enable1.close()
