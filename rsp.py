from RSPl import *
people=people(input("your name is: "))
ai=ai("ai")
print("r" in y)
while int(input("Enter 0 to stop: ")):
	ai.selection()
	people.selection(input("Choose a hand r,s,p: "))
	re = referee()
	re.check(people,ai)
	print(hand(ai.hand))
	print(hand(people.hand))
