import tkinter as tk
from tkinter import messagebox

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


# GUI Setup
def main():
    root = tk.Tk()
    root.title("Party Animal App 🎉")

    # Bunty
    bunty_label = tk.Label(root, text="Bunty count: 0", font=("Arial", 14))
    bunty_label.pack()
    bunty = PartyAnimal("Bunty", bunty_label)
    tk.Button(root, text="Party with Bunty", command=bunty.party).pack(pady=5)

    # Chintu
    chintu_label = tk.Label(root, text="Chintu count: 0", font=("Arial", 14))
    chintu_label.pack()
    chintu = PartyAnimal("Chintu", chintu_label)
    tk.Button(root, text="Party with Chintu", command=chintu.party).pack(pady=5)

    # On Close
    def on_close():
        msg = bunty.goodbye() + "\n" + chintu.goodbye()
        messagebox.showinfo("Party Over", msg)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

main()
