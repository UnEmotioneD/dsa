class ArrayStack:
    def __init__(self, capacity: int):
        self._capacity: int = capacity
        self._array = [None] * capacity
        self._top: int = -1

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == self._capacity - 1

    def push(self, item):
        if self.is_full():
            raise IndexError("Pushing to full stack.")
        self._top += 1
        self._array[self._top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Popping from empty stack.")
        item = self._array[self._top]
        self._top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peeking from empty stack.")
        return self._array[self._top]

    def __str__(self):
        return str(self._array[: self._top + 1])

    def __iter__(self):
        index: int = self._top
        while index != -1:
            yield self._array[index]
            index -= 1
