from collections import Counter
t = "rsp"
player = {'name':"AAA",'wins':0,'hand':''}
hands = {"r":"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","s":"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""","p":"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""} 
def check_win(player_chose,machine_chose):
    if player_chose==t[t.index(machine_chose)-1]: print("You win!"); x=1
    elif player_chose==machine_chose: print("spare!"); x=0
    else: print("You lose!"); x=0
    return x
def history(player_chose):
	with open('history.txt','r+') as f:
          r = f.read().replace('\n','')
          f.write(str(t.index(player_chose)))
          return Counter(r)
def save(player,rounds):
    with open('games.txt','r+') as f:
        f.write(f"{player['name']} wins:{player['wins']}/{rounds}\n")  
machine_chose = lambda d: t[int(d.most_common()[0][0])-1]
