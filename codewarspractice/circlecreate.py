import math

def circle(radius):
    result = []
    for y in range(-radius, radius + 1):
        row = ''
        for x in range(-radius, radius + 1):
            # Distance from center
            distance = math.sqrt(x**2 + y**2)
            # Adjust threshold for appearance
            if radius - 0.5 < distance < radius + 0.5:
                row += '#'
            else:
                row += ' '
        result.append(row)
    return '\n'.join(result)

# Example usage
print(circle(10))