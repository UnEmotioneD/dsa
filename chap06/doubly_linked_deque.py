class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next


class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0  # return True if empty

    def length(self) -> int:
        return self.size

    def add_front(self, item) -> None:
        # create node
        #  "prev" is "None" because it's being added to front-end of the deque
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

    def insert(self, item, idx: int) -> None:
        front_node = self.front
        # idx - 1 to insert to actual index rather than after
        for _ in range(idx - 1):
            front_node = front_node.next
        back_node = front_node.next
        node = DNode(item, front_node, back_node)
        # pointer of nodes front and back to point the inserted node
        front_node.next = node
        back_node.prev = node
        self.size += 1

    def peek_front(self):
        if not self.is_empty():
            return self.front.data

    def peek_rear(self):
        if not self.is_empty():
            return self.rear.data

    def peek(self, idx: int):
        if idx < 0:
            return None
        if self.size - 1 >= idx:
            node = self.front
            for _ in range(idx):
                node = node.next
            return node.data

    def delete_front(self):
        data = None  # initialize data variable to return later
        if not self.is_empty():
            data = self.front.data  # get the data
            self.front = self.front.next  # move front
            # if the front is None after moving the front
            #  which means the deque is now empty
            if self.front is None:
                self.rear = None
            else:
                # clear prev after delete
                self.front.prev = None
            self.size -= 1
        else:
            pass
        return data

    def delete_rear(self):
        data = None
        if not self.is_empty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear is None:
                self.front = None
            else:
                self.rear.next = None
            self.size -= 1
        else:
            pass
        return data

    def delete(self, idx: int):
        if idx < 0:
            return None
        if self.size - 1 >= idx:
            node = self.front
            for _ in range(idx):
                node = node.next
            data = node.data

            # if not last
            if node.prev:
                node.prev.next = node.next
            else:
                self.front = node.next
            # if not first
            if node.next:
                node.next.prev = node.prev
            else:
                self.rear = node.prev

            self.size -= 1
            return data

    def __str__(self):
        arr = []
        node = self.front  # starting point of scan
        while node:
            arr.append(node.data)
            node = node.next  # move node to point next
        return str(arr)  # parse it to string before returning
