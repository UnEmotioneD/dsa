from circular_deque import CircularDeque
from circular_queue import CircularQueue


def run_cricular_queue():
    que = CircularQueue(8)
    que.enqueue("A")
    que.enqueue("B")
    que.enqueue("C")
    que.enqueue("D")
    que.enqueue("E")
    que.enqueue("F")

    print(f"A B C D E F inserted {que}")
    print(f"Delete --> {que.dequeue()}")
    print(f"Delete --> {que.dequeue()}")
    print(f"Delete --> {que.dequeue()}")
    print("\tDelete 3 times")

    que.enqueue("G")
    que.enqueue("H")
    que.enqueue("I")

    print(f"\tG H I inserted {que}")


def run_cricular_dequeue():
    deq = CircularDeque()

    for i in range(9):
        if i % 2 == 0:
            deq.add_rear(i)
        else:
            deq.add_front(i)

    print(f"Odd number -> front, Even number -> rear: {deq}")

    deq.delete_front()
    deq.delete_front()

    deq.delete_rear()
    deq.delete_rear()
    deq.delete_rear()

    print(f"delete front twice and rear 3 times: {deq}")

    for i in range(9, 14):
        deq.add_front(i)

    print(f"add front 9 to 13: {deq}")


def main() -> None:
    run_cricular_queue()
    print("\n", "=" * 70, "\n")
    run_cricular_dequeue()


if __name__ == "__main__":
    main()
