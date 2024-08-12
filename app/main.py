from typing import Hashable, Any


class Dictionary:
    def __init__(
            self,
            capacity: int = 8,
            size: int = 0,
            load_factor: float = 2 / 3
    ) -> None:
        self.capacity = capacity
        self.size = size
        self.load_factor = load_factor
        self.storage = [[None]] * self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size > self.capacity * self.load_factor:
            self.resize()
        key_hash = hash(key)
        key_index = self.get_index(key)

        if key != self.storage[key_index][0]:
            self.size += 1
        self.storage[key_index] = (key, key_hash, value)

    def get_index(self, key: Hashable) -> int:
        key_hash = hash(key)
        index = key_hash % self.capacity

        while True:
            if self.storage[index][0] is None:
                break
            elif self.storage[index][0] == key:
                break
            else:
                index = (index + 1) % self.capacity

        return index

    def resize(self) -> None:
        self.capacity *= 2
        temp_list = self.storage
        self.storage = [[None]] * self.capacity
        for element in temp_list:
            key_index = self.get_index(element[0])
            self.storage[key_index] = element

    def __getitem__(self, key: Hashable) -> Any:
        index = self.get_index(key)
        if not any(self.storage[index]):
            raise KeyError
        return self.storage[index][2]

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return (f"capacity: {self.capacity} "
                f"size: {self.size} "
                f"storage: {self.storage}")
