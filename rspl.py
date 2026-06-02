from collections import Counter
t = "rsp"
player = {'name':"AAA",'wins':0,'hand':''}
with open('history.txt','r+') as f:
          history = f.read().replace('\n','')
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
def update_history(player_chose):
    global history
    history += str(t.index(player_chose))
    return history
def write_history():
    with open('history.txt','w') as f:
        f.write(history)
        f.close()
def machine_chose(history):
    if len(history)<5: return t[0]
    else:
        c = Counter(history)
        return t[int(c.most_common(1)[0][0])-1]