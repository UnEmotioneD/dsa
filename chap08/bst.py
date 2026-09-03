"""
Binary Search Tree

Orders left child node to be smaller then parent node.

TODO:
    - [x] create and shuffle the list
    - [x] create binary tree
    - [x] sort with in_order traverse
    - [x] get user input to search and delete
    - [x] on search print each node it goes through
    - [x] node deletion
    - [ ] print binary tree in tree style
"""

import random


class Node:
    def __init__(self, value: int, level: int = 0, gap: int = 0):
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None


def _insert(node: Node | None, value: int):
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = _insert(node.left, value)
    else:
        node.right = _insert(node.right, value)

    return node


def create_tree(numbers: list[int]):
    root = Node(numbers[0])

    for number in numbers[1:]:
        root = _insert(root, number)

    return root


def in_order(root: Node | None, result: list[int]):
    if root is None:
        return

    in_order(root.left, result)  # traverse left first
    result.append(root.value)
    in_order(root.right, result)


def prompt_search(numbers: list[int]):
    low = min(numbers)
    high = max(numbers)

    while True:
        try:
            key = int(input(f'Enter number to search [{low} ~ {high}]: '))

            if key in numbers:
                break
            else:
                print(f'{key} is not in the list.', end='\n\n')

        except ValueError:
            print('Input integer type', end='\n\n')

    return key


def search_node(root: Node | None, key: int) -> bool:
    if root is None:
        print(f'\n {key} is not found.', end='\n\n')
        return False

    if key == root.value:
        print(f'Reached: {root.value}')
        return True
    else:
        print(f'Traversing: {root.value}')

    if key < root.value:
        return search_node(root.left, key)
    else:
        return search_node(root.right, key)


def confirm_del(key: int):
    while True:
        try:
            print()
            foo = str(input(f'Delete node with {key}? [Y/n]: '))

            if foo.lower() == 'y' or foo == '':
                print()
                return True
            elif foo == 'n':
                print('Cancel node deletion.', end='\n\n')
                return False
            else:
                print('Enter `y` or `n`.')

        except ValueError:
            print('Enter string type.')


def _get_successor(curr: Node):
    assert curr.right is not None, '_get_successor() curr.right is None'
    curr = curr.right

    while curr.left is not None:
        curr = curr.left
    return curr


def del_node(root: Node | None, key: int):
    if root is None:
        return

    if root.value > key:
        root.left = del_node(root.left, key)
    elif root.value < key:
        root.right = del_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        successor: Node = _get_successor(root)
        root.value = successor.value
        root.right = del_node(root.right, successor.value)

    return root


def main():
    numbers = list(range(10))
    random.shuffle(numbers)

    print('Original: ')
    print(numbers, end='\n\n')

    root: Node | None = create_tree(numbers)

    while True:
        if root is None:
            print('The binary search tree is empty.')
            break

        result: list[int] = []
        in_order(root, result)

        print('Sorted: ')
        print(result, end=', ')
        print(f'Root: {root.value}', end='\n\n')

        key = prompt_search(result)
        if not search_node(root, key):
            continue

        if confirm_del(key):
            root = del_node(root, key)


if __name__ == '__main__':
    main()
