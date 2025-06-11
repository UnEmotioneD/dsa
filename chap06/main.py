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
    print(f'is dq empty: {dq.is_empty()}')
    print(f'length of dq: {dq.length()}')

    for i in range(10):
        if i % 2 == 0:
            dq.add_rear(i)
        else:
            dq.add_front(i)
    print(dq)

    dq.delete_front()
    dq.delete_rear()
    print(dq)
    print(f'is dq empty: {dq.is_empty()}')
    print(f'length of dq: {dq.length()}')


if __name__ == '__main__':
    run_linked_stack()
    print('=' * 50, end='\n')
    run_doubly_linked_stack()
