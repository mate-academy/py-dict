from typing import Hashable, Any


class Dictionary:
    LOAD_FACTOR = 2 / 3

    def __init__(self) -> None:
        self.capacity = 8
        self.length = 0
        self.threshold = int(self.capacity * self.LOAD_FACTOR)
        self.hash_table = self.make_hash_table()

    def make_hash_table(self) -> list:
        return [[] for _ in range(self.capacity)]

    def resize(self) -> None:
        old_hash_table = self.hash_table
        self.length = 0
        self.capacity *= 2
        self.threshold = int(self.capacity * self.LOAD_FACTOR)
        self.hash_table = self.make_hash_table()
        for element in old_hash_table:
            if element:
                self.__setitem__(element[0], element[2])

    def __getitem__(self, key: Hashable) -> Any:
        key_hash = hash(key)
        hash_index = key_hash % self.capacity
        while True:
            try:
                if self.hash_table[hash_index][0] == key\
                   and self.hash_table[hash_index][1] == key_hash:
                    return self.hash_table[hash_index][2]
            except IndexError:
                raise KeyError
            hash_index = (hash_index + 1) % self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.length == self.threshold:
            self.resize()
        key_hash = (hash(key))
        hash_index = key_hash % self.capacity
        while True:
            if not self.hash_table[hash_index]:
                self.hash_table[hash_index] = [key, key_hash, value]
                self.length += 1
                break
            if self.hash_table[hash_index][0] == key and\
                    self.hash_table[hash_index][1] == key_hash:
                self.hash_table[hash_index][2] = value
                break
            hash_index = (hash_index + 1) % self.capacity

    def __len__(self) -> int:
        return self.length
