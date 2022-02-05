# wordle game


#link to a list of 5 letter words

import random


def split(word):
    return list(word)
 
# prints a random value from the list
print("start of wordle")
real_word = random.choice(open('words.txt').read().split()).strip().lower()
print("-you have ten guesses")
print("-all guesses should be lower case letters")
print("-there can be double letters")





# words = ["apple", "pears", "goose", "floor"]
# real_word = random.choice(words)
real_word_split = split(real_word) 
guess_word = "nope"
guessed_letters = "z"

print("real word", real_word)
# print(real_word_split)

trials = 0
while((guess_word != real_word) and (trials < 10)):
	guess_word = raw_input("Guess word: ")
	guess_word_split = split(guess_word)
	
	if(len(guess_word_split) != 5):
		print("too long try again")
	else:
		i = 0
		for x in guess_word:
			if(x == real_word_split[i]):
				print(x, "is in the correct spot")
			elif(x in real_word_split):
				print(x, "is in the word, wrong spot")
			else:
				print(x," is not in the word")
			i = i+1
	# guessed_letters.append(guess_word_split)
	# top_line = ["Q", "W", "E", "R", "T", "Y"]
	# print(top_line)

	trials = trials+1;
	print("there are ", 10-trials, " trials remaining")

if(trials > 9):
	print("Game Over")
	print("The correct word is ", real_word)
else:
	print("the word is correct")
	print("You Win")



     
