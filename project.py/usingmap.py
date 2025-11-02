# Take input from the user (numbers separated by spaces)
numbers = input("Enter some numbers separated by spaces: ")  # Example: 1 2 3 4

# Step 1: Convert input strings to integers using map
num_list = list(map(int, numbers.split()))

# Step 2: Find the square of each number using map and lambda
squares = list(map(lambda x: x**2, num_list))

# Display results
print("Your numbers:", num_list)
print("Their squares:", squares)

