from rspl import *
player['name']=input("Give you nickname: ")
def main():
	rounds=0
	while int(input("Enter 0 to stop: ")):
		player['hand']=input('Choose a hand r,s,p: ')
		dot = machine_chose(history(player['hand']))
		print(hands[dot])
		player['wins']+=check_win(player['hand'],dot)
		rounds+=1
main()	
		
	
