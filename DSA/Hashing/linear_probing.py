class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [None]*size

    def hash_func(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_func(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = key

    def search(self, key):
        index = self.hash_func(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size
        return False
ht = HashTable()
ht.insert(5)
ht.insert(10) 
ht.insert(40)  # collision
print(ht.search(10))  # True
print(ht.search(15))  # False
print(ht.search(40))  # True
print(ht.table)