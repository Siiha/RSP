y=tuple("rsp")
class player:
    def __init__(self,name):
        self.name = name
        self.hand = "r"
        self.cores = 0
class people(player):
    def selection(self,hand):
        self.hand = hand
        f = open("hands.txt","a")
        f.write(self.hand)
        f.close()
class ai(player):
    def selection(self):
        f=open("hands.txt", "r")
        r=f.read()
        f.close()
        x = {}
        for i in y:
            x[i]=r.count(i)
        v = tuple(x.values())
        k = tuple(x.keys())
        self.hand=k[v.index(max(v)) - 1]
class referee:
    def check(self,p1,p2):
            if p1.hand==y[y.index(p2.hand) - 3 + 1]:
                print(f"{p1.name} lost!")
                p2.cores += 1
                f2 = open("score.txt","a")
                f2.write(f"{p2.name} won!\n")
                f2.close()
            elif p1.hand==p2.hand:
                f2 = open("score.txt","a")
                f2.write("It's a draw!\n")
                f2.close()
                print("It's a draw!")
            else:
                print(f"{p1.name} won!")
                p1.cores += 1
                f2 = open("score.txt","a")
                f2.write(f"{p1.name} won!\n")
def hand(x):
	h = {"r":"""
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
	return h[x]
