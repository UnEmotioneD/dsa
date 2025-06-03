class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self) -> bool:
        return self.top is None

    def is_full(self) -> bool:
        return False

    def push(self, e) -> None:
        self.top = Node(e, self.top)

    def pop(self):
        if not self.is_empty():
            n = self.top
            self.top = n.link
            return n.data

    def peek(self):
        if not self.is_empty():
            return self.top.data

    def size(self) -> int:
        node = self.top
        count: int = 0
        while not node is None:
            node = node.link
            count += 1
        return count

    def __str__(self):
        arr = []
        node = self.top
        while not node is None:
            arr.append(node.data)
            node = node.link
        return str(arr)
