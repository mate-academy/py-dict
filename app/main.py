from typing import Any, Hashable


class Node:
    def __init__(self, key, key_hash, value, is_deleted=False) -> None:
        self.key = key
        self.key_hash = key_hash
        self.value = value
        self.is_deleted = is_deleted


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.resize_threshold = self.capacity * (2 / 3)
        self.hash_table = [None] * self.capacity

    def get_index_of_cell(self, key: Hashable) -> int:
        return hash(key) % self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.get_index_of_cell(key)
        node = Node(key, hash(key), value)

        while True:
            if self.hash_table[index] is None:
                self.hash_table[index] = node
                self.length += 1
                break
            if (
                self.hash_table[index].key == key
                or self.hash_table[index].is_deleted is True
            ):
                self.hash_table[index] = node
                break
            index = (index + 1) % self.capacity
        if self.length > self.resize_threshold:
            self.resize_hash_table()

    def __getitem__(self, key: Hashable) -> Any:
        index = self.get_index_of_cell(key)
        for _ in range(self.capacity):
            if self.hash_table[index] is None:
                index = (index + 1) % self.capacity
            elif self.hash_table[index].key == key:
                return self.hash_table[index].value
            else:
                index = (index + 1) % self.capacity
        raise KeyError

    def resize_hash_table(self) -> None:
        self.length = 0
        self.capacity *= 2
        old_hash_table = self.hash_table.copy()
        self.resize_threshold = self.capacity * (2 / 3)
        self.hash_table = [None] * self.capacity
        for node in old_hash_table:
            if node:
                if node.is_deleted is True:
                    continue
                self.__setitem__(node.key, node.value)

    def __len__(self) -> int:
        return self.length

    def get(self, key: Hashable, value: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return value

    def clear(self) -> None:
        self.length = 0
        self.capacity = 8
        self.resize_threshold = self.capacity * (2 / 3)
        self.hash_table = [None] * self.capacity

    def __delitem__(self, key: Hashable) -> None:
        index = self.get_index_of_cell(key)
        for _ in range(self.capacity):
            if self.hash_table[index] is None:
                index = (index + 1) % self.capacity
            elif self.hash_table[index].key == key:
                self.hash_table[index] = None
                self.length -= 1
                return
            else:
                index = (index + 1) % self.capacity
        raise KeyError

    def pop(self, key: Hashable, default: Any = None) -> Any:
        try:
            value = self.__getitem__(key)
            self.__delitem__(key)
            return value
        except KeyError:
            if default:
                return default
            if default is None:
                return None
            if default is False:
                return False
