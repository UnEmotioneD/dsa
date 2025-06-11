class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next


class DoublyLinkedDequeue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.front == self.rear

    def add_front(self) -> None:
        return None

    def add_rear(self) -> None:
        return None

    def delete_front(self):
        return None

    def delete_rear(self):
        return None

    def size(self) -> int:
        return 0

    def __str__(self):
        return ''
