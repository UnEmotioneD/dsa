"""
Chapter 02
Page 61

---

for/while loop multification
"""


def mul_for() -> None:
    print('With for loop\n')

    # 1 to 9
    for n in range(1, 10):
        print(f'3x{n}: {3 * n}')


def mul_while() -> None:
    print('With while loop\n')

    n: int = 1
    while n < 10:
        print(f'3x{n}: {3 * n}')
        n = n + 1


def mul_for_reverse() -> None:
    print('With for loop in reverse\n')

    # 9 to 1 increment of -1
    for n in range(9, 0, -1):
        print(f'3x{n} : {3 * n}')


def multification() -> None:
    for j in range(1, 10):
        print(f'{j}단:', end=' ')
        for k in range(1, 10):
            print(f'{j * k:2}', end=' ')

            if k == 9:
                print('\n')


def main() -> None:
    # mul_for()
    # mul_while()
    # mul_for_reverse()
    multification()


if __name__ == '__main__':
    main()
