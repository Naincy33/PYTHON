def hash1(key, size):
    return key % size

def hash2(key):
    return 1 + (key % 5)

def insert(table, key, size):
    index = hash1(key, size)
    step = hash2(key)

    while table[index] is not None:
        index = (index + step) % size
    table[index] = key


table = [None]*7
insert(table, 10, 7)
insert(table, 17, 7)
insert(table, 24, 7)  # collision resolved
print(table)  # Output: [None, 17, None, 10, None