class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False

    def push(self, e):
        self.top = Node(e, self.top)

    def pop(self):
        if not self.is_empty():
            n = self.top
            self.top = n.link
            return n.data

    def peek(self):
        if not self.is_empty():
            return self.top.data
