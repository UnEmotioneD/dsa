"""
Binary Tree

TODO:
    - [x] create and shuffle the list
    - [x] create binary tree
    - [x] sort with in_order traverse
    - [x] get user input to search and delete
    - [x] on search print each node it goes through
    - [ ] node deletion
    - [ ] print binary tree in tree style
"""


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left: Node | None = None
        self.right: Node | None = None


def create_tree(numbers: list[int]):
    root = Node(numbers[0])

    for number in numbers[1:]:
        root = _insert(root, number)

    return root


def in_order(node: Node | None, res: list[int]):
    if node is None:
        return

    in_order(node.left, res)  # traverse left first
    res.append(node.data)
    in_order(node.right, res)


def get_search_no(numbers: list[int]):
    low = min(numbers)
    high = max(numbers)

    while True:
        try:
            search_no: int = int(input(f'Enter number to search [{low} ~ {high}]: '))

            if search_no >= low and search_no <= high:
                break
        except ValueError:
            print('Input integer type', end='\n\n')

    return search_no


def search_node(node: Node | None, search_no: int):
    if node is None:
        print('Not found')
        return

    if search_no is node.data:
        print(f'Reached: {node.data}')
        return
    else:
        print(f'Traversing: {node.data}')

    if search_no < node.data:
        search_node(node.left, search_no)
    else:
        search_node(node.right, search_no)


def _insert(node: Node | None, data: int):
    if node is None:
        return Node(data)

    if data < node.data:
        node.left = _insert(node.left, data)
    else:
        node.right = _insert(node.right, data)

    return node


def main():
    # numbers = list(range(10))
    # random.shuffle(numbers)
    numbers = [5, 8, 7, 0, 4, 9, 3, 2, 6, 1]  # fixed order for testing
    res: list[int] = []

    print('Original: ')
    print(numbers, end='\n\n')

    root: Node = create_tree(numbers)

    in_order(root, res)

    print('After in_order sorting: ')
    print(res, end='\n\n')

    search_no = get_search_no(numbers)
    search_node(root, search_no)


if __name__ == '__main__':
    main()
