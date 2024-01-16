class RandomizedSet:

    def __init__(self):
        self._s = {}
        self._m = {}
        self._c = 0

    def insert(self, val: int) -> bool:
        b = val in self._s
        if not b:
            self._s[val] = self._c
            self._m[self._c] = val
            self._c += 1
        return not b

    def remove(self, val: int) -> bool:
        b = val in self._s
        if b:
            index = self._s[val]
            del self._s[val]
            self._c -= 1

            x = self._m[self._c]
            del self._m[self._c]
            if val != x:
                self._m[index] = x
                self._s[x] = index
        return b

    def getRandom(self) -> int:
        return self._m[random.randint(0, self._c - 1)]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
