"""
Chapter 01
Page 45

---

fibonacci sequence iteration recursive
"""


def fibonacci_recursive(seq: int) -> int:
    if seq <= 1:
        return seq

    return fibonacci_recursive(seq - 2) + fibonacci_recursive(seq - 1)


def fibonacci_iteration(seq: int) -> int:
    sec_last: int = 0
    last: int = 1

    for _ in range(2, seq + 1):
        next_val: int = sec_last + last
        sec_last = last
        last = next_val
    return last


def main() -> None:
    user_input = int(input("Value of nth fibonacci sequence: "))
    print(
        f"{user_input}th value of fibonacci_recursive is: {fibonacci_recursive(user_input)}"
    )
    print(
        f"{user_input}th value of fibonacci_iteration is: {fibonacci_iteration(user_input)}"
    )


if __name__ == "__main__":
    main()
