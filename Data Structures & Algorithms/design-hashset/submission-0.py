class MyHashSet:

    def __init__(self):
        self.capacity = 1000
        self.table = [[] for _ in range(self.capacity)]
    
    def _hash(self, key: int) -> int:
        return key % self.capacity
    
    def add(self, key: int) -> None:
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)
    
    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.table[index]
    
    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)