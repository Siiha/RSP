from RSPl import *
from tkinter import *
people = people("you")
ai = ai("ai")
def r():
    ai.selection()
    people.selection("r")
    base.destroy()
    base2 = Tk()
    l = Label(base2, text="Ai selection is " + ai.hand)
    l.pack()
    base2.mainloop()
def s():
    ai.selection()
    people.selection("s")
    base.destroy()
    base2 = Tk()
    l = Label(base2, text="Ai selection is " + ai.hand)
    l.pack()
    base2.mainloop()
def p():
    ai.selection()
    people.selection("p")
    base.destroy()
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

