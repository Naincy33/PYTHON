import math

class Circle:
    def __init__(self):
        self.radius = 0.0

    def accept_radius(self):
        self.radius = float(input("Enter the radius of the circle: "))

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def display_details(self):
        print("\n--- Circle Details ---")
        print("Radius:", self.radius)
        print("Area:", round(self.calculate_area(), 2))
        print("Perimeter:", round(self.calculate_perimeter(), 2))


# Create Circle object and use its methods
circle1 = Circle()
circle1.accept_radius()
circle1.display_details()
