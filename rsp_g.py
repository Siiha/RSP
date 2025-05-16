from rspl import *
from tkinter import *
player['name']="AAA"
def r():
    player['hand']='r'
    dot = machine_chose(history(player['hand']))
    base.destroy()
    base2 = Tk()
    l = Label(base2, text="The opponent's choice is  " + dot)
    l.pack()
    base2.mainloop()
def s():
    player['hand']='s'
    dot = machine_chose(history(player['hand']))
    base.destroy()
    base2 = Tk()
    l = Label(base2, text="The opponent's choice is  " + dot)
    l.pack()
    base2.mainloop()
def p():
    player['hand']='p'
    dot = machine_chose(history(player['hand']))
    base.destroy()
    base2 = Tk()
    l = Label(base2, text="The opponent's choice is  " + dot)
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
