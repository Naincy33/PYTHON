import tkinter as tk

class PartyAnimal:
    total_parties = 0

    def __init__(self, nam):
        self.name = nam
        self.x = 0

    def party(self):
        self.x += 1
        PartyAnimal.total_parties += 1

class FootballFan(PartyAnimal):
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points += 7
        self.party()

class CricketFan(PartyAnimal):
    def __init__(self, nam):
        super().__init__(nam)
        self.runs = 0

    def sixer(self):
        self.runs += 6
        self.party()

# GUI Setup
app = tk.Tk()
app.title("Sports Fan Scoreboard")
app.geometry("400x300")

# Create players
jim = FootballFan("Jim")
virat = CricketFan("Virat")

# Labels
jim_label = tk.Label(app, text="Jim - Points: 0 | Parties: 0")
jim_label.pack()

virat_label = tk.Label(app, text="Virat - Runs: 0 | Parties: 0")
virat_label.pack()

total_label = tk.Label(app, text="Total Parties: 0")
total_label.pack()

# Button functions
def jim_scores():
    jim.touchdown()
    update_labels()

def virat_scores():
    virat.sixer()
    update_labels()

def update_labels():
    jim_label.config(text=f"Jim - Points: {jim.points} | Parties: {jim.x}")
    virat_label.config(text=f"Virat - Runs: {virat.runs} | Parties: {virat.x}")
    total_label.config(text=f"Total Parties: {PartyAnimal.total_parties}")

# Buttons
tk.Button(app, text="Jim Touchdown", command=jim_scores).pack(pady=5)
tk.Button(app, text="Virat Sixer", command=virat_scores).pack(pady=5)

app.mainloop()
