from typing import Any, Hashable
from dataclasses import dataclass, field


@dataclass
class Node:
    key: Hashable
    hash_val: int
    value: Any


@dataclass
class Dictionary:
    initial_capacity = 8
    load_factor = 2 / 3
    size = 0
    hash_table: list[list[Node]] = field(init=False)

    def __post_init__(self) -> None:
        self.hash_table = [None] * self.initial_capacity

    def line_stop(self) -> int:
        return int(self.initial_capacity * self.load_factor)

    def get_index(self, key: Hashable) -> int:
        return hash(key) % self.initial_capacity

    @staticmethod
    def get_hash(key: Hashable) -> int:
        return hash(key)

    def __len__(self) -> int:
        return self.size

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size >= self.line_stop():
            self.resize()
        hash_val = self.get_hash(key)
        index = self.get_index(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = Node(key, hash_val, value)
            self.size += 1

        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                self.hash_table[index].value = value
                return
            index = (index + 1) % self.initial_capacity
            if self.hash_table[index] is None:
                self.hash_table[index] = Node(key, hash_val, value)
                self.size += 1
                return

        self.size += 1
        if self.size >= self.line_stop():
            self.resize()

    def __getitem__(self, key: Hashable) -> Any:

        for node in self.hash_table:
            if node:
                if node.key == key:
                    return node.value
        raise KeyError(f"Key not found: {key}")

    def resize(self) -> None:
        self.initial_capacity *= 2
        self.size = 0

        old_table = self.hash_table.copy()
        self.hash_table = [None] * self.initial_capacity

        for node in old_table:
            if node:
                self[node.key] = node.value
