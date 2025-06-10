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


if __name__ == '__main__':
    run_linked_stack()
