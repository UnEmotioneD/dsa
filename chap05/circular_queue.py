class CircularQueue:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_empty(self) -> bool:
        return self.front == self.rear

    def is_full(self) -> bool:
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item) -> None:
        if self.is_full():
            return
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')

        self.front = (self.front + 1) % self.capacity
        return self.array[self.front]

    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')

        return self.array[(self.front + 1) % self.capacity]

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def __str__(self) -> str:
        if self.is_empty():
            return '[]'

        if self.front < self.rear:
            return str(self.array[self.front + 1 : self.rear + 1])

        result = (
            self.array[self.front + 1 : self.capacity]
            + self.array[0 : self.rear + 1]
        )
        return str(result)
