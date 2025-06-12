from doubly_linked_deque import DoublyLinkedDeque
from linked_stack import LinkedStack


def run_linked_stack() -> None:
    stack = LinkedStack()

    print(f'Is stack empty? {stack.is_empty()}')

    stack.push(1)
    print('push 1')

    stack.push(2)
    print('push 2')

    stack.push(3)
    print('push 3')

    print('Inside the stack: ', end='')
    print(stack)

    print(f'Is stack empty? {stack.is_empty()}')

    print(f'size of linked_stack: {stack.size()}')

    print(f'peek: {stack.peek()}')
    print(f'pop: {stack.pop()}')

    print('Inside the stack: ', end='')
    print(stack)

    print(f'pop: {stack.pop()}')
    print(f'pop: {stack.pop()}')
    print(f'pop: {stack.pop()}')

    print(stack)


def run_doubly_linked_stack() -> None:
    dq = DoublyLinkedDeque()

    print(dq)
    print(f'Is dq empty: {dq.is_empty()}')
    print(f'Size of dq: {dq.size}')

    for i in range(10):
        if i % 2 == 0:
            dq.add_rear(i)
        else:
            dq.add_front(i)

    print(dq)
    print(f'Is dq empty: {dq.is_empty()}')
    print(f'Size of dq: {dq.size}')
    print(f'Peek front: {dq.peek_front()}')
    print(f'Peek rear: {dq.peek_rear()}')

    print(f'Delete front: {dq.delete_front()}')
    print(f'Delete rear: {dq.delete_rear()}')
    print(dq)

    print(f'Peek index 5: {dq.peek(5)}')
    print(dq)
    print(f'Delete index 5: {dq.delete(5)}')
    print(dq)
    print('Insert 10 to index 5')
    dq.insert(10, 5)
    print(dq)

    print('Reverse dq')
    dq.reverse()
    print('Add 1 to rear')
    dq.add_rear(1)
    print(dq)

    print(f'Search index of item 1: {dq.search(1)}')
    print(f'Search index of item 11: {dq.search(11)}')

    print(f"Count number of 1's: {dq.count(1)}")

    # can't use'em when empty
    print(f'Data of front: {dq.front.data}')
    print(f'Data of rear: {dq.rear.data}')

    # use of __iter__()
    print(f'Sum of all elements in dq: {sum(dq)}')
    print(f'Biggest value of dq: {max(dq)}')
    print(f'Smallest value of dq: {min(dq)}')


if __name__ == '__main__':
    run_linked_stack()
    print('=' * 50, end='\n')
    run_doubly_linked_stack()
