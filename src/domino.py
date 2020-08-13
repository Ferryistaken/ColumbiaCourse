class Domino:
	def __init__(self, topString, bottomString):
		self.topString = topString
		self.bottomString = bottomString

	def describe(self):
		return "Top String: " + self.topString + "  Bottom String: " + self.bottomString

	def simplify(self):
		# returns a domino with an empty string
		if self.topString.startswith(self.bottomString) or self.bottomString.startswith(self.topString):
			if len(self.topString) >= len(self.bottomString):
				smallestString = self.bottomString
				biggestString = self.topString
				return Domino(biggestString[len(smallestString):], "")
			else:
				smallestString = self.topString
				biggestString = self.bottomString
				return Domino("", biggestString[len(smallestString):])
		else:
			return self



	def isASolution(self):
		# returns true if the domino is a solution(top and bottom string are the same)
		if self.topString == self.bottomString:
			return True
		else:
			return False


class Node:
	def __init__(self, parentNode=None, addedDomino=None, addedDominoList=None):
		self.parentNode = parentNode
		self.addedDomino = addedDomino
		self.addedDominoList = addedDominoList
		if parentNode is None:
			self.state = Domino("", "")
		else:
			self.state = Domino(self.parentNode.state.topString + self.addedDomino.topString, self.parentNode.state.bottomString + self.addedDomino.bottomString).simplify()


	def describe(self):
		if self.parentNode is None:
			return "Root Node    "
		else:
			return "Parent node: " + self.parentNode.describe() +  "Domino: " + self.addedDomino.describe() + "   State: " + self.state.describe()
