y= list("rsp")
class player:
    def __init__(self,name):
        self.name = name
        self.hand = "r"
        self.cores = 0
class people(player):
    def selection(self):
        self.hand = input("Choose a hand r,s,p: ")
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
    def hands(self):
        if self.hand=="r":
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        if self.hand=="s":
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        if self.hand=="p":
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
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
                f2.write(f"{p1.name} won! \n")
                
people=people(input("your name is: "))
ai=ai("ai")
people.selection()
ai.selection()
ai.hands()
re = referee()
re.check(people,ai)
