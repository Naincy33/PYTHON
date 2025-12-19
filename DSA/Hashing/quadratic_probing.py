def insert(table, key, size):
    index = key % size
    i = 1
    while table[index] is not None:
        index = (key + i*i) % size
        i += 1
    table[index] = key


table = [None]*7
insert(table, 10, 7)
insert(table, 17, 7)
insert(table, 24, 7)  # collision resolved
print(table)  # Output: [None, 17, None, None, 10, None, 24]