class MyHashMap:
    keys = []
    values = []

    def put(self, key, value):
        if key in self.keys:
            self.remove(key)
        self.keys.append(key)
        self.values.append(value)
    
    def get(self, key):
        if not key in self.keys:
            return -1
        return self.values[self.keys.index(key)]

    def remove(self, key):
        del self.values[self.keys.index(key)]
        del self.keys[self.keys.index(key)]
