"""
Binary Tree

TODO:
    - [x] create and shuffle the list
    - [x] create binary tree
    - [x] sort with in_order traverse
    - [ ] get user input to search and delete
    - [ ] on search print each node it goes through
    - [ ] print binary tree in tree style
"""

import random


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left: Node | None = None
        self.right: Node | None = None


def create_tree(numbers: list[int]) -> Node:
    root: Node = Node(numbers[0])

    for number in numbers[1:]:
        root = _insert(root, number)

    return root


def in_order(node: Node | None, res: list[int]) -> None:
    if node is None:
        return

    in_order(node.left, res)  # traverse left first
    res.append(node.data)
    in_order(node.right, res)


def _insert(root: Node | None, data: int) -> Node:
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = _insert(root.left, data)
    else:
        root.right = _insert(root.right, data)

    return root


def main() -> None:
    numbers: list[int] = list[int](range(10))
    random.shuffle(numbers)
    # numbers: list[int] = [5, 8, 7, 0, 4, 9, 3, 2, 6, 1]  # fixed order for testing
    res: list[int] = []

    print('Before sorted: ')
    print(numbers, end='\n\n')

    root: Node = create_tree(numbers)

    in_order(root, res)

    print('After in_order: ')
    print(res, end='\n\n')


if __name__ == '__main__':
    main()
