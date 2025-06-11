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
        return self.size == 0   # return True if empty

    def add_front(self, item) -> None:
        # create node
        #  "prev" is "None" because it's begin added to front-end of the dequeue
        #  "next" to point at what "front" is pointing currently
        node = DNode(item, None, self.front)
        if self.is_empty():
            # font and rear to point at newly created node
            self.front = self.rear = node
        else:
            # prev to point the new node
            self.front.prev = node
            # and move the front
            self.front = node
        self.size += 1

    def add_rear(self, item) -> None:
        node = DNode(item, self.rear, None)

        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self.size += 1

    def delete_front(self):
        return None

    def delete_rear(self):
        return None

    def size(self) -> int:
        return 0

    def __str__(self):
        return ''
