class Player:
    def __init__(self, name, matches_played):
        self.name = name
        self.matches_played = matches_played

class Batsman(Player):
    def __init__(self, name, matches_played, runs_scored):
        # Call base class constructor
        super().__init__(name, matches_played)
        self.runs_scored = runs_scored

    def calculate_average(self):
        if self.matches_played == 0:
            return 0
        return self.runs_scored / self.matches_played

    def display_details(self):
        print("\n--- Batsman Details ---")
        print("Name:", self.name)
        print("Matches Played:", self.matches_played)
        print("Runs Scored:", self.runs_scored)
        print("Average Runs per Match:", round(self.calculate_average(), 2))


# Main part of the program
# Taking input from user
name = input("Enter Batsman's Name: ")
matches = int(input("Enter Number of Matches Played: "))
runs = int(input("Enter Total Runs Scored: "))

# Create a Batsman object
batsman1 = Batsman(name, matches, runs)

# Display details
batsman1.display_details()
