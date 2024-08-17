from typing import Any, Hashable


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table: list = [None] * self.capacity

    def _calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity
        while (self.hash_table[index] is not None
               and self.hash_table[index][1] != key):
            index = (index + 1) % self.capacity
        return index

    def resize(self) -> None:
        old_hash_table = self.hash_table
        self.__init__(self.capacity * 2)
        for item in old_hash_table:
            if item is not None:
                self.__setitem__(item[1], item[-1])

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            if self.size + 1 >= self.capacity * 2 / 3:
                self.resize()
                return self.__setitem__(key, value)
            self.size += 1

        self.hash_table[index] = (hash(key), key, value)

    def __getitem__(self, key: Hashable) -> Any:
        index = self._calculate_index(key)
        if self.hash_table[index] is None:
            raise KeyError(f"Key {key} is not in this dict")
        return self.hash_table[index][-1]

    def __len__(self) -> int:
        return self.size
