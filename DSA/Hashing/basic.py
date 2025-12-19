class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_func(key)
        self.table[index] = key

    def search(self, key):
        index = self.hash_func(key)
        return self.table[index] == key


ht = HashTable()
ht.insert(12)
ht.insert(24)

print(ht.search(12))  # True
print(ht.search(5))   # False
