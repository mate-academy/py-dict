class Dictionary:
    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.hash = self.capacity * [None]

    def resize_dict(self):
        self.capacity *= 2
        self.length = 0
        old_dict = self.hash
        self.hash = self.capacity * [None]
        for value in old_dict:
            if value:
                self.__setitem__(value[0], value[2])

    def __setitem__(self, key, value):
        if self.length >= (self.capacity * 2 / 3):
            self.resize_dict()
        hash_key = hash(key)
        index = hash_key % self.capacity

        while True:
            if not self.hash[index]:
                self.hash[index] = [key, hash_key, value]
                self.length += 1
                break
            if self.hash[index][0] == key and \
                    self.hash[index][1] == hash_key:
                self.hash[index][2] = value
                break
            index = (index + 1) % self.capacity

    def __getitem__(self, key):
        hash_key = hash(key)
        index = hash_key % self.capacity
        while self.hash[index]:
            if self.hash[index][1] == hash_key and\
                    self.hash[index][0] == key:
                return self.hash[index][2]
            index = (index + 1) % self.capacity
        raise KeyError

    def __len__(self):
        return self.length
