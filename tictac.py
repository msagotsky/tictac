# Tic Tac Toe game

import random

#make function to display board
def display(L):
	print '\n'
	print L[0], L[1], L[2]
	print L[3], L[4], L[5]
	print L[6], L[7], L[8]
	print '\n'

#who goes first?
def whoIsFirst():
	x = random.choice([0, 1])
	if x == 1:
		return 'user'
	else:
		return 'computer'

#function to make move
def makeMove(L, x, y):
	L[y] = x

#check if space is free board x, input y
def spaceCheck(x, y):
	return x[y] == '_'

#get move from user. user is always 'X' for now...
#boolean 'or' hack short-circuits problems with invalid list indices
def userMove():
	n = raw_input('Enter 0 thru 8 to move\n')
	while n not in ['0', '1', '2', '3', '4', '5', '6', '7', '8'] or not spaceCheck(L,int(n)):
		n = raw_input('Seriously! Enter 0 thru 8 to move:\n')
	makeMove(L, 'X', int(n))

#makes copy of the board useful for AI
def boardCopy(L):
	boardCopy = [ ]

	for x in L:
		boardCopy.append(x)
	return boardCopy

#computer moves
def computerMove():
	for x in range(0,9): #checks board copy for winning move and wins
		altL = boardCopy(L)
		if spaceCheck(altL, x):
			makeMove(altL, 'O', x)
			if isGameOver(altL, 'O'):
				return makeMove(L, 'O', x)
	for x in range(0,9): #checks board copy for losing move and blocks
		altL = boardCopy(L)
		if spaceCheck(altL, x):
			makeMove(altL, 'X', x)
			if isGameOver(altL, 'X'):
				return makeMove(L, 'O', x)
	moves = [ ] #makes random move if one is available 
	for x in range(0,9):
		if spaceCheck(L, x):
			moves.append(x)
	if len(moves) != 0:
		return makeMove(L, 'O', random.choice(moves))
	else:
		return None

#End game scenario 1: checks if there are any moves left
def isTie():
	moves = [ ]
	for x in range(0,9):
		if spaceCheck(L,x):
			moves.append(x)
	if len(moves) == 0:
		return True
	else:
		return False

#End game scenario 2: someone wins.  Is there a prettier way to write this block?
def isGameOver(x,y):
	return ((x[0] == y and x[1] == y and x[2] == y) or 
	(x[3] == y and x[4] == y and x[5] == y) or
	(x[6] == y and x[7] == y and x[8] == y) or
	(x[0] == y and x[3] == y and x[6] == y) or
	(x[1] == y and x[4] == y and x[7] == y) or
	(x[2] == y and x[5] == y and x[8] == y) or
	(x[0] == y and x[4] == y and x[8] == y) or
	(x[6] == y and x[4] == y and x[2] == y))

print '\n\n\nWelcome to tic-tac-toe!!!\n\n0 1 2\n3 4 5\n6 7 8\nEnter 0-8 to place your tic or tac as shown below!\n'

#yes the game is set to run indefinitely until you force quit.  But who would do that anyway :P  
while True:
	L = ['_'] * 10
	turn = whoIsFirst()
	gameOn = True
	while gameOn == True:
		if turn == 'user':
			print 'Your move :)'
			userMove()
			display(L)
			if isGameOver(L,'X'):
				print 'you WIN! hurray! :D'
				print "let's play again!\n\n"
				gameOn = False
			elif isTie():
				print 'GAME IS A TIE'
				print "let's play again!\n\n"
				gameOn = False
			else:
				turn = 'computer'
		if turn == 'computer':
			print 'Computer moves:'
			computerMove()
			display(L)
			if isGameOver(L, 'O'):
				print 'you LOSE, suckah!'
				print "let's play again!\n\n"
				gameOn = False
			elif isTie():
				print 'GAME IS A TIE'
				print "let's play again!\n\n"
				gameOn = False
			else:
				turn = 'user'