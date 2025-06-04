class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__(self, count=0):
        self.top = None
        self.count = count

    def is_empty(self) -> bool:
        return self.top is None

    def is_full(self) -> bool:
        return False

    def push(self, e) -> None:
        self.top = Node(e, self.top)
        self.count += 1

    def pop(self):
        if not self.is_empty():
            n = self.top
            self.top = n.link
            self.count -= 1
            return n.data

    def peek(self):
        if not self.is_empty():
            return self.top.data

    def size(self) -> int:
        return self.count

    def __str__(self):
        arr = []
        node = self.top
        while not node is None:
            arr.append(node.data)
            node = node.link
        return str(arr)
