from RSPl import *
from tkinter import *
people = people("you")
ai = ai("ai")
def r():
    people.hand = "r"
    base.destroy()
    ai.selection()
    base2 = Tk()
    l = Label(base2, text="Ai selection is " + ai.hand)
    l.pack()
    base2.mainloop()
def s():
    people.hand = "s"
    base.destroy()
    ai.selection()
    base2 = Tk()
    l = Label(base2, text="Ai selection is " + ai.hand)
    l.pack()
    base2.mainloop()
def p():
    people.hand = "p"
    base.destroy()
    ai.selection()
    base2 = Tk()
    l = Label(base2, text="Ai selection is " + ai.hand)
    l.pack()
    base2.mainloop()
base = Tk()
sr = Button(base, text="r", command=r)
sr.pack()
ss = Button(base, text="s", command=s)
ss.pack()
sp = Button(base, text="p", command=p)
sp.pack()
base.mainloop()

