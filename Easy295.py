# Easy #295 Letter By Letter

def change_letters(from_string, to_string):
	print from_string
	letters = list(from_string)

	for i in range(0, len(letters)):
		if (letters[i] != to_string[i]):
			letters[i] = to_string[i]
			print "".join(letters)

change_letters('floor', 'brake')
print '-----------------'
change_letters('wood', 'book')
print '-----------------'
change_letters('a fall to the floor', 'braking the door in')
