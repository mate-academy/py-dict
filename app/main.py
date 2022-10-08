class Dictionary:

    def __init__(self):
        self.capacity = 8
        self.threshold = int(self.capacity * 2 / 3)
        self.length = 0
        self.hash_table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        key_hash = hash(key)
        index = key_hash % self.capacity
        while True:
            if len(self.hash_table[index]) == 0:
                self.hash_table[index] = [key, value, key_hash]
                self.length += 1
                break
            if self.hash_table[index][0] == key and \
                    self.hash_table[index][2] == key_hash:
                self.hash_table[index][1] = value
                break
            index = (index + 1) % self.capacity
        if self.length == self.threshold:
            self.resize()

    def resize(self):
        temp_table = self.hash_table
        self.capacity *= 2
        self.length = 0
        self.threshold = int(self.capacity * 2 / 3)
        self.hash_table = [[] for _ in range(self.capacity)]
        for item in temp_table:
            if len(item) != 0:
                self.__setitem__(item[0], item[1])

    def __getitem__(self, input_key):
        key_hash = hash(input_key)
        index = key_hash % self.capacity
        item = self.hash_table[index]
        while True:
            try:
                if item[0] == input_key and item[2] == hash(input_key):
                    return item[1]
            except IndexError:
                raise KeyError
            index = (index + 1) % self.capacity
            item = self.hash_table[index]

    def __len__(self):
        return self.length

    def clear(self):
        self.hash_table.clear()

    def __delitem__(self, key):
        index = hash(key) % self.capacity
        self.hash_table[index] = []

    def get(self, key):
        return self.__getitem__(key)

    def pop(self, key):
        element = self.__getitem__(key)
        self.__delitem__(key)
        return element
