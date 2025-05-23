from circular_queue import CircularQueue


class CircularDequeue(CircularQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

    # Rename methods
    def add_rear(self, item):
        self.enqueue(item)

    def delete_front(self):
        self.dequeue()

    def get_front(self):
        self.peek()

    # New methods
    def add_front(self, item):
        if not self.is_full():
            item = self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            pass

    def delete_rear(self):
        if not self.is_empty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else:
            pass

    def get_rear(self):
        if not self.is_empty():
            return self.array[self.rear]
        else:
            pass
