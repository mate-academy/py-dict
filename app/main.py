from typing import Any, Hashable, List
from dataclasses import dataclass

INITIAL_CAPACITY = 8
RESIZE_THRESHOLD = 2 / 3
CAPACITY_MULTIPLIER = 2


@dataclass
class Node:
    key: Hashable
    value: Any
    hash_data: int


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: List[Node | None] = [None] * INITIAL_CAPACITY
        self.capacity = INITIAL_CAPACITY

    def __len__(self) -> int:
        return self.length

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.length + 1 > self.capacity * RESIZE_THRESHOLD:
            self.resize_table()

        hash_key = hash(key)
        key_index = hash_key % self.capacity

        while self.hash_table[key_index]:
            if (self.hash_table[key_index].hash_data == hash_key
                    and self.hash_table[key_index].key == key):
                self.hash_table[key_index].value = value
                return
            else:
                key_index = (key_index + 1) % self.capacity

        self.hash_table[key_index] = Node(key, value, hash_key)
        self.length += 1

    def resize_table(self) -> None:
        self.length = 0
        self.capacity *= CAPACITY_MULTIPLIER

        new_hash_table: List[Node | None] = [None] * self.capacity
        node_data = [node for node in self.hash_table if node is not None]

        for node in node_data:
            key_index = node.hash_data % self.capacity
            while new_hash_table[key_index]:
                if (new_hash_table[key_index].hash_data == node.hash_data
                        and new_hash_table[key_index].key == node.key):

                    self.hash_table[key_index].value = node.value
                    return
                else:
                    key_index = (key_index + 1) % self.capacity

            new_hash_table[key_index] = node
            self.length += 1

        self.hash_table = new_hash_table

    def __getitem__(self, key: Hashable) -> Any:

        key_hash = hash(key)

        index = key_hash % self.capacity

        while (self.hash_table[index] is not None
               and self.hash_table[index].key != key):
            index = (index + 1) % self.capacity

        if self.hash_table[index] is None:
            raise KeyError(f"Key {key} doesn't exist!")

        return self.hash_table[index].value
