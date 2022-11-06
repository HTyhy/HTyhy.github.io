import tkinter, sys
from tkinter import *
root = tkinter.Tk()
root.overrideredirect(True)
root.attributes("-alpha", 0.15)
root.wm_attributes('-topmost', 0.7)
root.geometry("160x200+1100+200")
all_y = root.winfo_screenheight()
all_x = root.winfo_screenwidth()
text = Text(root, width=22, height=20, undo=True, autoseparators=False,font=('微软雅黑',10))
text.grid()
rootalpha = 0.1
is_hide = 'right'
def close(event):
    root.destroy()
    sys.exit()

def MouseDown(event): # 不要忘记写参数event
    global mousX  # 全局变量，鼠标在窗体内的x坐标
    global mousY  # 全局变量，鼠标在窗体内的y坐标
 
    mousX=event.x  # 获取鼠标相对于窗体左上角的X坐标
    mousY=event.y  # 获取鼠标相对于窗左上角体的Y坐标
    
def MouseMove(event):
    root.geometry(f'+{event.x_root - mousX}+{event.y_root - mousY}') # 窗体移动代码
    # event.x_root 为窗体相对于屏幕左上角的X坐标
    # event.y_root 为窗体相对于屏幕左上角的Y坐标
def exit(event):
    root.destroy()
root.bind("<Button-1>",MouseDown)  # 按下鼠标左键绑定MouseDown函数
root.bind("<B1-Motion>",MouseMove)  # 鼠标左键按住拖曳事件,3个函数都不要忘记函数写参数
root.bind("<Double-Button-1>",exit) 
root.bind("<Double-Button-3>", close)
root.mainloop()