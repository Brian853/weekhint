import tkinter,threading
from datetime import datetime
import tkinter.font as tkFont
top='1800'
left='960'
ww='50'
hh='20'
root = tkinter.Tk()
root.overrideredirect(True)
root.attributes('-alpha', 0.6)
root.attributes('-topmost',1)
root.geometry(ww+'x'+hh+'+'+top+'+'+left)
ftlbl = tkFont.Font(family='fixedsys', size= 18)
tmlbl = tkinter.Label(root,width=200,fg = '#FFFAFA',bg = 'black',text = 'Hello',anchor='center',font=ftlbl)
tmlbl.pack()
x, y = 0, 0
def fun_move(event):
    global x,y
    new_x = (event.x-x)+root.winfo_x()
    new_y = (event.y-y)+root.winfo_y()
    root.geometry(ww+'x'+hh +'+'+ str(new_x)+'+' + str(new_y))
def fun_button_1(event):
    global x,y
    x,y = event.x,event.y
def fun_timer():
    global timer
    fun_applyweek()      
    timer = threading.Timer(5555, fun_timer)
    timer.start()
def fun_getweek():
    return datetime.date(datetime.now()).isocalendar()[1]
def fun_applyweek():
    tmlbl.configure(text = str(datetime.now().year)[-2:] +'W'+str(fun_getweek()))
tmlbl.bind('<B1-Motion>',fun_move)
tmlbl.bind('<Button-1>',fun_button_1)
fun_applyweek() 
root.mainloop()
timer = threading.Timer(1, fun_timer)
timer.start()
