# 561_le14_smyth.py
#
# Smyth, Ravela
# NIM Game 2 player



def main():
	li = []
	playGame(li)
 
	
def initBoard(li):	    
	for i in range(1,5):
		li.append(i*2-1)
	getBoard(li)

def playGame(li):
	player = "Player 1"

	initBoard(li)

	while True:
		getInput(li, player)
		
		#check winner (li all 0s)
		if li == [0] * len(li):
			print("Congrats {}, you WON!\n".format(player))
			break
		
		#switch players
		if player == "Player 1":
			player = "Player 2"
		else:
			player = "Player 1"
		
def getInput(li, player):
	while True:
		sticks = input('{} please input # of sticks to remove: '.format(player))
		rows = input("Pick a row to remove from: ")
		
		#check validity
		if (sticks and rows) and (int(sticks) > 0) and (int(rows) <= len(li)) and (int(rows) > 0):
				if (int(sticks) <= li[int(rows)-1]):
					break
	
		print("Your input is not valid, try again {}".format(player))

	#update board
	li[int(rows)-1] -= int(sticks)

	getBoard(li)
		
def getBoard(li):
	print("Current board:\n"+"-" * 25)
	for i in range(1,5):
		print('Row #{} : {}'.format(i, 'O' * li[i-1]))		
	print("-" * 25)

main()








