from rspl import *
player['name']=input("Give you nickname: ")
def main():
	global history
	rounds=0
	while int(input("Enter 0 to stop: ")):
		player['hand']=input('Choose a hand r,s,p: ')
		dot = machine_chose(history)
		print(hands[dot])
		player['wins']+=check_win(player['hand'],dot)
		history =update_history(player['hand'])
		
		rounds+=1
	write_history()
main()