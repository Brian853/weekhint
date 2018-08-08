# -*- coding: UTF-8 -*-
import tkinter,threading
from datetime import datetime
import tkinter.font as tkFont
ww='60'
hh='30'
root = tkinter.Tk()
root.overrideredirect(True)
root.attributes('-alpha', 0.5)
root.geometry(ww+'x'+hh+'+400+400')
root.attributes('-topmost',1)
canvas = tkinter.Canvas(root)
canvas.configure(width = ww,height = hh,bg = 'black')
ftlbl = tkFont.Font(family='fixedsys', size= 18)
tmlbl = tkinter.Label(root,fg = '#FFFAFA',bg = 'black',text = 'Hello',anchor='center',font=ftlbl)
tmlbl.pack()
canvas.configure(highlightthickness = 0)
canvas.pack()
x, y = 0, 0
def move(event):
    global x,y
    new_x = (event.x-x)+root.winfo_x()
    new_y = (event.y-y)+root.winfo_y()
    s = ww+'x'+hh +'+'+ str(new_x)+'+' + str(new_y)
    root.geometry(s)
def button_1(event):
    global x,y
    x,y = event.x,event.y
def fun_timer():
    global timer
    tmlbl.configure(text = fun_getweek())
    timer = threading.Timer(5555, fun_timer)
    timer.start()
def fun_getweek():
    weeks = datetime.date(datetime.now()).isocalendar()[1]
    return weeks
canvas.bind('<B1-Motion>',move)
canvas.bind('<Button-1>',button_1)
year = str(datetime.now().year)[-2:]
tmlbl.configure(text = year +'W'+str(fun_getweek()))
root.mainloop()
timer = threading.Timer(1, fun_timer)
timer.start()
