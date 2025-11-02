import tkinter as tk
from tkinter import messagebox
import random
import os

DATA_FILE = "party_data.txt"

def get_emoji(name):
    emojis = ['🧑‍🎤', '🧒', '👧', '🧑‍🦱', '👨‍🎨', '👩‍🚀', '👨‍🏫', '🧑‍💻', '👸', '🤴', '🎭', '🤹']
    random.seed(hash(name))  # Always same emoji for same name
    return random.choice(emojis)


class PartyAnimal:
    def __init__(self, name, label):
        self.name = name
        self.count = 0
        self.label = label
        self.emoji = get_emoji(name)

    def party(self):
        self.count += 1
        self.label.config(text=f"{self.emoji} {self.name} count: {self.count}")

    def goodbye(self):
        return f"{self.emoji} {self.name}: {self.count} parties 🎉"

    def get_data(self):
        return f"{self.name}:{self.count}"

    def set_count(self, count):
        self.count = count
        self.label.config(text=f"{self.emoji} {self.name} count: {self.count}")


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
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan', 'lime', 'magenta', 'gold']
        shapes = ['circle', 'square', 'triangle']

        for _ in range(20):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(10, 25)
            color = random.choice(colors)
            shape = random.choice(shapes)

            if shape == 'circle':
                self.create_oval(x - size, y - size, x + size, y + size, fill=color, outline="")
            elif shape == 'square':
                self.create_rectangle(x - size, y - size, x + size, y + size, fill=color, outline="")
            elif shape == 'triangle':
                self.create_polygon(
                    x, y - size,
                    x - size, y + size,
                    x + size, y + size,
                    fill=color, outline=""
                )

        self.after_id = self.after(300, self.firework)

    def stop_fireworks(self):
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
            self.delete("all")

def load_data():
    data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                if ':' in line:
                    name, count = line.strip().split(':')
                    data[name] = int(count)
    return data

def save_data(players):
    with open(DATA_FILE, "w") as f:
        for player in players:
            f.write(player.get_data() + "\n")

def main():
    root = tk.Tk()
    root.title("Party Animal App 🎉")

    saved_counts = load_data()
    players = []
    player_widgets = {}

    fw_canvas = FireworksCanvas(root, width=400, height=200, bg="black")
    fw_canvas.pack(pady=10)

    # Frame for dynamic players
    players_frame = tk.Frame(root)
    players_frame.pack(pady=10)

    def add_player(name):
        if name in player_widgets:
            messagebox.showwarning("Oops!", f"{name} already exists.")
            return
        if not name.isalpha():
            messagebox.showerror("Invalid Name", "Please enter a valid name (letters only).")
            return

        label = tk.Label(players_frame, font=("Arial", 14))
        label.pack()
        animal = PartyAnimal(name, label)
        animal.set_count(saved_counts.get(name, 0))
        players.append(animal)
        player_widgets[name] = animal
        btn = tk.Button(players_frame, text=f"Party with {name}", command=lambda: [animal.party(), fw_canvas.start_fireworks()])
        btn.pack(pady=3)

    # Add default players
    for name in saved_counts:
        add_player(name)

    # Add new player controls
    add_frame = tk.Frame(root)
    add_frame.pack(pady=10)

    entry = tk.Entry(add_frame)
    entry.pack(side=tk.LEFT)

    def on_add():
        new_name = entry.get().strip().capitalize()
        if new_name:
            add_player(new_name)
            entry.delete(0, tk.END)

    tk.Button(add_frame, text="Add Player", command=on_add).pack(side=tk.LEFT, padx=5)

    def on_close():
        fw_canvas.stop_fireworks()
        save_data(players)
        msg = "\n".join([p.goodbye() for p in players])
        messagebox.showinfo("Party Over", msg)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

main()



