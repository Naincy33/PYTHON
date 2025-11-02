class Actor:
    def __init__(self, actorid, actorname, no_movies, earnings):
        self.actorid = actorid
        self.actorname = actorname
        self.no_movies = no_movies
        self.earnings = earnings

    def average_earning(self):
        if self.no_movies == 0:
            return 0
        return self.earnings / self.no_movies

    def display(self):
        print("Actor ID:", self.actorid)
        print("Name:", self.actorname)
        print("Number of Movies:", self.no_movies)
        print("Total Earnings:", self.earnings)
        print("Average Earning per Movie:", self.average_earning())
        print("-" * 30)


# Create 3 Actor objects
actor1 = Actor(101, "Shah Rukh Khan", 80, 800)
actor2 = Actor(102, "Salman Khan", 90, 700)
actor3 = Actor(103, "Aamir Khan", 60, 600)

# Store them in a list
actors = [actor1, actor2, actor3]

# Find actor with minimum average earnings
min_avg_actor = actors[0]
for actor in actors[1:]:
    if actor.average_earning() < min_avg_actor.average_earning():
        min_avg_actor = actor

print("Actor with Minimum Average Earning:")
min_avg_actor.display()
