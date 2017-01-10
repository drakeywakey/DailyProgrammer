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


def scrabble(tiles, word):
	letter_counts = {}

	# get counts of how many letters we have in our tiles
	for letter in tiles:
		print letter
		if (letter in letter_counts):
			letter_counts[letter] += 1
			print 'new count for %r' % letter_counts[letter]
		else:
			letter_counts[letter] = 1
			print 'letter_counts[%r] now 1' % letter

	print letter_counts

scrabble("ladilmy", 'daily')
