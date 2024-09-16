import tkinter as tk

class DraggableWindow:
    def __init__(self, root):
        self.root = root
        self.x = 0
        self.y = 0
        
        # 创建窗口
        self.window = tk.Toplevel(root)
        self.window.geometry("200x200")
        
        # 绑定鼠标事件
        self.window.bind("<Button-1>", self.start_drag)
        self.window.bind("<B1-Motion>", self.drag)
    
    def start_drag(self, event):
        self.x = event.x
        self.y = event.y
    
    def drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        self.window.geometry(f"+{self.window.winfo_x() + deltax}+{self.window.winfo_y() + deltay}")

# 创建主窗口
root = tk.Tk()
root.geometry("300x300")

# 创建可移动窗口
draggable_window = DraggableWindow(root)

root.mainloop()