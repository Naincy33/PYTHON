import tkinter as tk
from tkinter import messagebox
import random

class PartyAnimal:
    def __init__(self, name, label):
        self.name = name
        self.count = 0
        self.label = label

    def party(self):
        self.count += 1
        self.label.config(text=f"{self.name} count: {self.count}")

    def goodbye(self):
        return f"Party's over for {self.name}! Final count: {self.count}"

class FireworksCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.width = int(self['width'])
        self.height = int(self['height'])
        self.after_id = None

    def start_fireworks(self):
        self.firework()
    
    def firework(self):
        self.delete("all")
        for _ in range(15):  # 15 circles per frame
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            r = random.randint(5, 15)
            color = random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink'])
            self.create_oval(x-r, y-r, x+r, y+r, fill=color, outline="")
        self.after_id = self.after(300, self.firework)  # repeat every 300ms

    def stop_fireworks(self):
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
            self.delete("all")

def main():
    root = tk.Tk()
    root.title("Party Animal App 🎉")

    fw_canvas = FireworksCanvas(root, width=400, height=200, bg="black")
    fw_canvas.pack(pady=10)

    bunty_label = tk.Label(root, text="Bunty count: 0", font=("Arial", 14))
    bunty_label.pack()
    bunty = PartyAnimal("Bunty", bunty_label)
    tk.Button(root, text="Party with Bunty", command=lambda: [bunty.party(), fw_canvas.start_fireworks()]).pack(pady=5)

    chintu_label = tk.Label(root, text="Chintu count: 0", font=("Arial", 14))
    chintu_label.pack()
    chintu = PartyAnimal("Chintu", chintu_label)
    tk.Button(root, text="Party with Chintu", command=lambda: [chintu.party(), fw_canvas.start_fireworks()]).pack(pady=5)

    def on_close():
        fw_canvas.stop_fireworks()
        msg = bunty.goodbye() + "\n" + chintu.goodbye()
        messagebox.showinfo("Party Over", msg)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

main()
