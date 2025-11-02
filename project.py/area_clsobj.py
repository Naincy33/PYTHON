import math

class Circle:
    def __init__(self):
        self.radius = 0.0

    def accept_radius(self):
        self.radius = float(input("Enter the radius of the circle: "))

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display(self):
        print("\n--- Circle Details ---")
        print("Radius       :", self.radius)
        print("Area         :", round(self.area(), 2))
        print("Perimeter    :", round(self.perimeter(), 2))

# Main program
c = Circle()
c.accept_radius()
c.display()
