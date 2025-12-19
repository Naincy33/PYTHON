class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_func(key)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash_func(key)
        return key in self.table[index]


ht = HashTable()
ht.insert(5)
ht.insert(10)  # collision

print(ht.search(10))
print(ht.search(15))  # False
print(ht.table)