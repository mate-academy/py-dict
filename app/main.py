from typing import Any, Hashable


class Dictionary:
    INITIAL_CAPACITY = 8
    LOAD_FACTOR = 2 / 3

    def __init__(self) -> None:
        self.capacity = self.INITIAL_CAPACITY
        self.length = 0
        self.hash_table = [[] for _ in range(self.INITIAL_CAPACITY)]

    def hash_table_index(self, key: Hashable) -> int:
        hashed_key = hash(key)
        index = hashed_key % self.capacity

        return index

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        threshold = self.capacity * self.LOAD_FACTOR

        if self.length > threshold:
            self.capacity *= 2
            old_hash_table = self.hash_table

            self.hash_table = [[] for _ in range(self.capacity)]

            for item in old_hash_table:
                if item:
                    key, value = item
                    self.__setitem__(key, value)
                    self.length -= 1

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.hash_table_index(key)

        while self.hash_table[index]:
            key_, value_ = self.hash_table[index]
            if key == key_:
                self.hash_table[index] = (key, value)
                return
            index = (index + 1) % self.capacity

        self.length += 1
        self.hash_table[index] = (key, value)
        self.resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = self.hash_table_index(key)

        while self.hash_table[index]:
            key_, value = self.hash_table[index]
            if key == key_:
                return value
            index = (index + 1) % self.capacity

        raise KeyError

    def pop(self, key: Hashable) -> Any:
        item = self[key]
        del self[key]

        return item

    def clear(self) -> None:
        self.hash_table = [[] for _ in range(self.capacity)]
        self.length = 0

    def get(self, key: Hashable, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default
