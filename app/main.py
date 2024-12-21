class Dictionary:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.hash = hash(key)

    def __init__(self, initial_capacity=8, load_factor=0.7):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        if self.size / self.capacity >= self.load_factor:
            self._resize()

        index = hash(key) % self.capacity

        if self.table[index] is None:
            self.table[index] = []

        for node in self.table[index]:
            if node.key == key:
                node.value = value
                return

        self.table[index].append(self.Node(key, value))
        self.size += 1

    def __getitem__(self, key):
        index = hash(key) % self.capacity

        if self.table[index] is not None:
            for node in self.table[index]:
                if node.key == key:
                    return node.value

        raise KeyError(f"Key '{key}' not found")

    def _resize(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for bucket in self.table:
            if bucket is not None:
                for node in bucket:
                    new_index = node.hash % new_capacity
                    if new_table[new_index] is None:
                        new_table[new_index] = []
                    new_table[new_index].append(node)

        self.capacity = new_capacity
        self.table = new_table

    def __repr__(self):
        items = []
        for bucket in self.table:
            if bucket is not None:
                for node in bucket:
                    items.append(f"{node.key}: {node.value}")
        return "{" + ", ".join(items) + "}"
