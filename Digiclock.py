import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        
        self.label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
        self.label.pack(anchor='center')
        
        self.update_clock()
        
    def update_clock(self):
        current_time = strftime('%H:%M:%S %p')
        self.label.config(text=current_time)
        self.root.after(1000, self.update_clock)
        
if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop() 
