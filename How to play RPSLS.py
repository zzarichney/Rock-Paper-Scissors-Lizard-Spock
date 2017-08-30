
if answer == myanswer:
	print "DRAW"
elif answer == "rock":
	if myanswer == "paper":
		print "WIN!"
	elif myanswer == "scissor":
		print "LOST!"
elif answer == "paper":
	if myanswer == "scissor":
		print "WIN!"
	elif myanswer == "rock":
		print "LOST!"
elif answer == "scissor":
	if myanswer == "rock":
		print "WIN!"
	elif myanswer == "paper":
		print "LOST!"

"rock", "paper", "scissor", "lizzard", "spock"
print "WIN"
0: 2, 3		2,3
1: 0, 4		1,5
2: 1, 3		3,5
3: 1, 4		4,7
4: 0, 2		4,6

LOST
0: 1, 4		1,4	
1: 2, 3		3,4	
2: 0, 4		2,6
3: 0, 2		3,2
4: 1, 3		5,7


