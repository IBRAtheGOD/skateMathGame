import random

#defining some functions
def askQuestion():
	#this will ask a random question according to the current trick they're learning
	pass

def evaluateLevel():
	#this will tell what trick they're on
	pass


#welcome message

print('This is a game of skate! Well sorta...Answer the questions in time or you get a letter!')

class Player:
	def __init__(self, name, favoriteTrick1, favoriteTrick2, favoriteTrick3):
		super(Player, self).__init__()
		self.name = name
		self.favoriteTrick1 = favoriteTrick1
		self.favoriteTrick2 = favoriteTrick2
		self.favoriteTrick3 = favoriteTrick3

#creates instance of the class player. player1 is an object
player1 = Player
#takes input to assign a name to the player
player1.name = input("Please enter your name: ")
#now we ask the user their favorite tricks
player1.favoriteTrick1 = input("\nGreat! Now please enter your top 3 favorite skateboard tricks => ")
player1.favoriteTrick2 = input("\n=>")
player1.favoriteTrick3 = input("\n=>")
# test print
# print(f'your name is {player1.name} and your top 3 favorite skateboard tricks are the {player1.favoriteTrick1}\n, the {player1.favoriteTrick2}, and the {player1.favoriteTrick3}')
print("\n##########################################")
print("\n#  ------  |  /   ----   -----  -----    #")
print("\n#  |       | /   |    |    |    |        #")
print("\n#  ------  |/    ------    |    -----    #")
print("\n#       |  |\\   |    |    |    |        #")
print("\n#  ------  | \\  |    |    |    -----    #")
print("\n##########################################")















