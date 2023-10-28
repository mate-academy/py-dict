from typing import Any


class Dictionary:

    def __init__(
            self
    ) -> None:
        self.length = 0
        self.capacity = 8
        self.hash_table: list = [None] * self.capacity

    def _resize(self) -> None:
        self.capacity *= 2
        self.length = 0
        temp_table: list = self.hash_table
        self.hash_table = [None] * self.capacity
        for cell in temp_table:
            if cell:
                self[cell[0]] = cell[2]

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.length == int(self.capacity * (2 / 3)):
            self._resize()
        cell_number = hash(key) % self.capacity
        while True: # while loop > for loop
            if not self.hash_table[cell_number]:
                self.hash_table[cell_number] = [key, hash(key), value]
                self.length += 1
                break
            elif (self.hash_table[cell_number][0] == key
                    and self.hash_table[cell_number][1] == hash(key)):
                self.hash_table[cell_number][2] = value
                break
            else:
                cell_number = (cell_number + 1) % self.capacity

    def __getitem__(self, item: Any) -> None:
        cell_number = hash(item) % self.capacity
        for _ in range(self.capacity):
            if self.hash_table[cell_number] is None:
                break
            if (self.hash_table[cell_number][0] == item
                    and self.hash_table[cell_number][1] == hash(item)):
                return self.hash_table[cell_number][2]
            else:
                cell_number = (cell_number + 1) % self.capacity
        raise KeyError

    def __len__(self) -> int:
        return self.length
