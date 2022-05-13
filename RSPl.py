y= list("rsp")
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
        x= []
        
        f=open("hands.txt", "r")
        self.r=f.read()
        
        for i in y:
            x.append(self.r.count(i))
        self.hand=y[x.index(max(x)) - 1]
class referee:
    def check(self,p1,p2):
            if p1.hand==y[y.index(p2.hand) - 3 + 1]:
                print(p1.name + " lost!")
                p2.cores += 1
                f2 = open("score.txt","w")
                f2.write(p2.name+" won!\n")
                f2.close()
            elif p1.hand==p2.hand:
                f2 = open("score.txt","w")
                f2.write("It's a draw!\n")
                f2.close()
                print("It's a draw!")
            else:
                print(p1.name + " won!")
                p1.cores += 1
                f2 = open("score.txt","w")
                f2.write(p1.name+" won!\n")