class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size        

    def put(self, key: int, value: int) -> None:
        hash_key = self._hash_function(key)
        for i, (k, v) in enumerate(self.map[hash_key]):
            if k == key:
                self.map[hash_key][i] = (key, value)
                return
        self.map[hash_key].append((key, value))

    def get(self, key: int) -> int:
        hash_key = self._hash_function(key)
        for k,v in self.map[hash_key]:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        hash_key = self._hash_function(key)
        for i, (k, v) in enumerate(self.map[hash_key]):
            if k == key:
                del self.map[hash_key][i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
