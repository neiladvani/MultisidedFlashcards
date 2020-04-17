from Flashcard import Flashcard
from random import shuffle, randint
def runApp():
	commands = {"load", "exit"}
	while True:
		command = input("Please input a command (load or exit): ")
		if command == 'exit':
			return
		elif command == 'load':
			load()
			return
		else:
			print('Command not found.')

def load():
	filename = input("Please input the name of your file, or type the name for a new set of flashcards: ")

	file = open(filename, 'a')
	readFile = open(filename,'r')
	lines = list(readFile)
	readFile.close()

	flashcards = []
	curCard = -1

	for line in lines:
		contents = line.strip().split(',')
		if not contents:
			continue
		front = contents[0]
		flashcard = Flashcard(front)
		for back in contents[1:]:
			if back:
				flashcard.addBack(back)
		flashcards.append(flashcard)

	if len(flashcards)!=0:
		curCard = 0
	print("\n\n")
	while True:
		if curCard>-1:
			print("Current flashcard: " + flashcards[curCard].getFront())
		print("\n")

		command = input("Input a command (add flashcard, add back, quit, view next, view random, flip, flip random, cheat, shuffle card, shuffle deck): ")
		print("\n")
		if command == 'quit':
			file.flush()
			file.close()
			return
		elif command == 'add flashcard':
			front = input("Please input the front of this flashcard: ")
			backs = input("Please input the back(s) of this flashcard separated by commas (1,2,3): ")

			newCard = Flashcard(front)
			for back in backs.split(','):
				newCard.addBack(back)
			flashcards.append(newCard)

			file.write('\n')
			file.write(front+','+backs)
			file.flush()
			print("Flashcard " + front + " has been added to deck: " + filename)
		elif command == 'add back':
			if curCard<0:
				print("No flashcards currently available.")
				continue
			print("Command not supported yet.")
		elif command == 'view next':
			if curCard<0:
				print("No flashcards currently available.")
				continue
			curCard+=1
			curCard%=len(flashcards)
			print("Now viewing flashcard: " + flashcards[curCard].getFront())
		elif command == 'view random':
			if curCard<0:
				print("No flashcards currently available.")
				continue
			curCard = randint(0,len(flashcards)-1)
			print("Now viewing flashcard: " + flashcards[curCard].getFront())
		elif command == 'flip':
			if curCard<0:
				print("No flashcards currently available.")
				continue
			print(flashcards[curCard].getNextBack())
		elif command == 'flip random':
			if curCard<0:
				print("No flashcards currently available.")
				continue
			print(flashcards[curCard].getRandomBack())
		elif command == 'cheat':
			if curCard<0:
				print("No flashcards currently available.")
				continue
			confirm = input("Are you sure you are a dirty cheater? (y/n)")
			if confirm == 'y':
				print(flashcards[curCard].getBacks())
			else:
				print("I thought so.")
		elif command == 'shuffle card':
			flashcards[curCard].shuffleFlashcard()
			print("Current flashcard has been shuffled.")
		elif command == 'shuffle deck':
			shuffle(flashcards)
			print("Deck has been shuffled.")
		else:
			print("Invalid command.")
		print("\n")

if __name__ == '__main__':
	runApp()