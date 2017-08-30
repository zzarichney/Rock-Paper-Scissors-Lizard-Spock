import random
import sys
import os

def menu():
	os.system('cls')
	while True:
		print "Want to play Rock Paper Scissor Lizzard Spock?"
		corridor = raw_input("Yes\nno\nhelp\n:")
		if corridor == "yes":
			print "Lets us play"
			os.system('cls')
			game()
			
		elif corridor == "no":
			print "No? then why did you open me?"
			raw_input()
			os.system('cls')
			sys.exit()
		elif corridor == "help":
			os.system('cls')
			print "heres how to play! \n" 
			raw_input()
			os.system('cls')
			continue
		else:
			raw_input("was that any of the options?")	
			os.system('cls')

def game():
	playerP = 0
	computerP = 0
	os.system('cls')
	possibility = ["Rock", "Paper", "Scissor", "Lizzard", "Spock"]
	while True:
		#os.system('cls')
		print "Score Board\nplayer 1: {0}\nComputer : {1}".format(playerP, computerP)
		computer = random.choice(possibility)
		#print computer
		player1 = raw_input("rock, paper, scissor, lizzard or spock? ").title()

		#print player1
		if player1 == "Exit":
			break

		if not player1 in possibility + "Bomb":
			os.system('cls')
			print "please try again you noob"
			continue

		player_won = False
		if player1 == computer:
				os.system('cls')
				print "It's a draw"
				continue
		elif player1 == "Rock":
			if computer == "Scissor" or computer == "Lizzard":
				player_won = True
		elif player1 == "Paper":
			if computer == "Rock" or computer == "Spock":
				player_won = True
		elif player1 == "Scissor":
			if computer == "Paper" or computer == "Lizzard":
				player_won = True
		elif player1 == "Lizzard":
			if computer == "Paper" or computer == "Spock":
				player_won = True
		elif player1 == "Spock":
			if computer == "Rock" or computer == "Scissor":
				player_won = True
		elif player1 == "Bomb":
			player_won = True

		if player_won:
			os.system('cls')
			print "win"
			playerP += 1
		else:
			os.system('cls')
			print "Lost"
			computerP += 1
			continue	
	menu()
menu()