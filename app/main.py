from __future__ import annotations
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8

    def resize_hash_table(self) -> bool:
        if self.length >= int(len(self.hash_table) * 2 / 3):
            self.hash_table += [None] * len(self.hash_table)

            return True
        return False

    def reindex_element_after_resize_table(self) -> None:
        elements_before_resize = [
            element
            for element in self.hash_table
            if isinstance(element, tuple)
        ]
        self.hash_table = [None] * len(self.hash_table)

        for key, value in elements_before_resize:
            self.insert_element_in_hash_table(key=key, value=value)

    def insert_element_in_hash_table(self, key: Any, value: Any) -> None:
        index_key = hash(key) % len(self.hash_table)

        while True:
            if self.hash_table[index_key] is None:
                self.hash_table[index_key] = (key, value)
                break
            elif index_key == (len(self.hash_table) - 1) \
                    and self.hash_table[index_key] is not None:
                index_key = 0
            else:
                index_key += 1

    def __setitem__(self, key: Any, value: Any) -> None:
        for element in self.hash_table:
            if isinstance(element, tuple) and (element[0] == key):
                index_el = self.hash_table.index(element)
                self.hash_table[index_el] = (key, value)
                return

        self.insert_element_in_hash_table(key=key, value=value)
        self.length += 1

        check_resize = self.resize_hash_table()
        if check_resize:
            self.reindex_element_after_resize_table()

    def __getitem__(self, item: Any) -> Any | Exception:
        for element in self.hash_table:
            if isinstance(element, tuple):
                if element[0] == item:
                    return element[1]
        else:
            raise KeyError

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, key: Any) -> None:
        for element in self.hash_table:
            if isinstance(element, tuple):
                if element[0] == key:
                    index_element = self.hash_table.index(element)
                    self.hash_table[index_element] = None
                    self.length -= 1
