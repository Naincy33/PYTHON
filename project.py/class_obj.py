class PartyAnimal:
    def __init__(self, name):
        self.name = name
        self.x = 0
        print(f"{self.name} joins the party!")

    def party(self):
        self.x = self.x + 1
        print(f"{self.name} party count: {self.x}")

    def __del__(self):
        print(f"Party's over for {self.name}. Final count: {self.x}")

# Objects
an1 = PartyAnimal("Bunty")
an2 = PartyAnimal("Chintu")

an1.party()
an2.party()
an1.party()
an2.party()
an2.party()

# Optional: delete explicitly (to trigger __del__ early)
del an1
del an2
