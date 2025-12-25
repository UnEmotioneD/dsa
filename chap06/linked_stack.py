class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__(self):
        self._top = None
        self.count = 0

    def is_empty(self) -> bool:
        return self._top is None

    def is_full(self) -> bool:
        return False

    def push(self, e) -> None:
        self._top = Node(e, self._top)
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Popping from empty stack.")
        n = self._top
        self._top = n.link
        self.count -= 1
        return n.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peeking from empty stack.")
        return self._top.data

    def __str__(self):
        arr = []
        node = self._top
        while not node is None:
            arr.append(node.data)
            node = node.link
        return str(arr)
