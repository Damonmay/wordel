# wordle game

import random


def split(word):
    return list(word)
 
# prints a random value from the list
print("start of wordle")
real_word = random.choice(open('words.txt').read().split()).strip().lower()
print("-you have ten guesses")
print("-all guesses should be lower case letters")
print("-there can be double letters")


real_word_split = split(real_word) 
guess_word = "nope"
guessed_letters = ["z"]
real_word_progress = ["_","_","_","_","_"]
found_letters = []


trials = 0
while((guess_word != real_word) and (trials < 10)):
	guess_word = raw_input("Guess word: ")
	guess_word_split = split(guess_word)
	
	if(len(guess_word_split) != 5):
		print("this has to be a 5 letter word")
	else:
		i = 0
		for x in guess_word:
			if(x == real_word_split[i]): #correct spot
				real_word_progress[i] = x
			elif(x in real_word_split): #is in the word, but wrong spot
				if(x not in found_letters):
					found_letters.append(x)
			else: #letter is not in the word
				if(x not in guessed_letters):
					guessed_letters.append(x)
			i = i+1
	print("Letters not in the word", guessed_letters)
	print(real_word_progress)
	print("Letters in the word", found_letters)

	trials = trials+1;
	print("there are ", 10-trials, " trials remaining")

if(trials > 9):
	print("Game Over")
	print("The correct word is ", real_word)
else:
	print("the word is correct")
	print("You Win")



     
