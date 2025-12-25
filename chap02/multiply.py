def mul_for() -> None:
    print("With for loop\n")

    # 1 to 9
    for n in range(1, 10):
        print(f"3x{n}: {3 * n}")


def mul_while() -> None:
    print("With while loop\n")

    n: int = 1
    while n < 10:
        print(f"3x{n}: {3 * n}")
        n = n + 1


def mul_for_reverse() -> None:
    print("With for loop in reverse\n")

    # 9 to 1 increment of -1
    for n in range(9, 0, -1):
        print(f"3x{n} : {3 * n}")


def multification() -> None:
    for j in range(1, 10):
        print(f"{j}단:", end=" ")
        for k in range(1, 10):
            print(f"{j * k:2}", end=" ")

            if k == 9:
                print("\n")


def mul_input() -> None:
    base: int = int(input("enter base number for multification: "))
    limit: int = int(input("enter limit number for multification: "))

    for i in range(1, limit + 1):
        print(f"{base} * {i} = {base * i}")


def main() -> None:
    # mul_for()
    # mul_while()
    # mul_for_reverse()
    # multification()
    mul_input()


if __name__ == "__main__":
    main()
