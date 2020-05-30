import tkinter,threading
from datetime import datetime
import tkinter.font as tkFont
import time
from win10toast import ToastNotifier

def wh_move(event):
    global x,y
    new_x = (event.x-x)+root.winfo_x()
    new_y = (event.y-y)+root.winfo_y()
    root.geometry(ww+'x'+hh +'+'+ str(new_x)+'+' + str(new_y))
def wh_button_1(event):
    global x,y
    x,y = event.x,event.y
def wh_button_3(event):
    global timer
    timer.cancel()
    quit()
def wh_tips_3(event):
    toaster.show_toast(u'WeeHint', u'本程序用于显示年份周数。\n可以拖动标签改变位置。\n在标签上三击右键退出。',threaded=True)
def wh_timer():
    global timer
    #fun_applyweek()      
    tmlbl.configure(text = str(datetime.now().year)[-2:] +'W'+str(datetime.date(datetime.now()).isocalendar()[1]))
    timer = threading.Timer(60, wh_timer)
    timer.start()

top='1705'
left='155'
ww='50'
hh='20'
root = tkinter.Tk()
root.overrideredirect(True)
root.attributes('-alpha', 0.6)
root.attributes('-topmost',1)
root.geometry(ww+'x'+hh+'+'+left+'+'+top)
ftlbl = tkFont.Font(family='fixedsys', size= 18)
tmlbl = tkinter.Label(root,width=200,fg = '#FFFAFA',bg = 'black',text = 'Hello',anchor='center',font=ftlbl)
tmlbl.pack()
x, y = 0, 0 
tmlbl.bind('<B1-Motion>',wh_move)
tmlbl.bind('<Button-1>',wh_button_1)
tmlbl.bind('<Button-3>',wh_tips_3)
tmlbl.bind('<Triple-Button-3>',wh_button_3)
toaster = ToastNotifier()
toaster.show_toast(u'WeeHint', u'本程序用于显示年份周数。\n可以拖动标签改变位置。\n在标签上三击右键退出。',threaded=True)
#fun_applyweek() 

timer = threading.Timer(1, wh_timer)
timer.start()
root.mainloop()
