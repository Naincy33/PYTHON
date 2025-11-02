# Create the dictionary
ODD = {
    1: "one",
    3: "three",
    5: "five",
    7: "seven",
    9: "nine"
}

# Display the keys
print("Keys:", ODD.keys())

# Display the values
print("Values:", ODD.values())

# Display the items (key-value pairs)
print("Items:", ODD.items())

# Find the length of the dictionary
print("Length:", len(ODD))

# Check if 7 is present as a key
print("Is 7 present?", 7 in ODD)

# Check if 2 is present as a key
print("Is 2 present?", 2 in ODD)

# Retrieve the value corresponding to the key 9
print("Value for key 9:", ODD.get(9))

# Delete the item with key 9
ODD.pop(9, None)  # safely removes key 9 if present

# Display the dictionary after deletion
print("Dictionary after deleting key 9:", ODD)
