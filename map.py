class HashTable:
    def __init__(self) -> None:
        self.size = 11
        self.data = [None] * self.size
        self.slots = [None] * self.size

    def put(self, key, value):
        hashvalue = self._hash_function(key, self.size)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = value
            else:
                nextslot = self._rehash(hashvalue, self.size)
                while self.slots[nextslot] not in (None, key):
                    nextslot = self._rehash(nextslot, self.size)
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = value
                else:
                    self.data[nextslot] = value

    def get(self, key):
        startslot = self._hash_function(key, self.size)
        found = False
        stop = False
        data = None
        currentslot = startslot
        while self.slots[currentslot] != None and not found and not stop:
            if self.slots[currentslot] == key:
                found = True
                data = self.data[currentslot]
            else:
                currentslot = self._rehash(currentslot, self.size)
                if currentslot == startslot:
                    stop = True
        return data

    def __len__(self):
        return sum(1 for x in self.slots if x != None)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, key):
        return key in self.slots

    def _hash_function(self, key, size):
        return key % size

    def _rehash(self, oldhash, size):
        return (oldhash+1) % size


if __name__ == '__main__':
    map = HashTable()
    map[12] = 'cat'
    map[22] = 'dog'
    map[42] = 'human'
    map[23] = 'zz'
    assert map[12] == 'cat'
    assert map[22] == 'dog'
    assert map[42] == 'human'
    assert map[23] == 'zz'
    map[23] = 'xx'
    assert map[23] == 'xx'
    import random
    map2 = HashTable()
    i = 0
    while i < 11:
        x = random.randint(1, 100)
        if x not in map2:
            map2[x] = x
            i += 1

    print(len(map2))
