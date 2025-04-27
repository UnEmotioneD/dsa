class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def get_entry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        return None

    def insert(self, pos, e):
        if not self.is_full() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1

    def replace(self, pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e

    def delete(self, pos):
        if not self.is_empty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1
            return e

    def __str__(self):
        return str(self.array[: self.size])
