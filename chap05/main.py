"""
Chapter 05
Page 173
---
Execute circular queue
"""


from circular_queue import CircularQueue


def run_cricular_queue():
    que = CircularQueue(8)
    que.enqueue('A')
    que.enqueue('B')
    que.enqueue('C')
    que.enqueue('D')
    que.enqueue('E')
    que.enqueue('F')

    print(f'A B C D E F inserted {que}')
    print(f'Delete --> {que.dequeue()}')
    print(f'Delete --> {que.dequeue()}')
    print(f'Delete --> {que.dequeue()}')
    print('\tDelete 3 times')

    que.enqueue('G')
    que.enqueue('H')
    que.enqueue('I')

    print(f'\tG H I inserted {que}')


def main() -> None:
    run_cricular_queue()


if __name__ == '__main__':
    main()
