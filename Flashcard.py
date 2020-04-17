from random import randint, shuffle
class Flashcard:
	def __init__(self,front,size=1):
		self.size = size
		self.front = front
		self.backs = []
		self.curBack = -1

	def addBack(self, backVal):
		self.size+=1
		self.backs.append(backVal)

	def updateFront(self, frontVal):
		self.front = frontVal

	def getFront(self):
		return self.front

	def getBacks(self):
		return self.backs

	def getRandomBack(self):
		if not self.backs:
			return "This flashcard has no backs"
		self.curBack = randint(0,len(self.backs)-1)
		return self.backs[self.curBack]

	def shuffleFlashcard(self):
		shuffle(self.backs)
		self.curBacks=-1

	def getSize(self):
		return self.size

	def getNextBack(self):
		if not self.backs:
			return "This flashcard has no backs"
		self.curBack+=1
		self.curBack%=len(self.backs)
		return self.backs[self.curBack]


