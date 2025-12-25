def factorial_iteration(user_input: int) -> int:
    result: int = 1

    for i in range(1, user_input + 1):
        result = result * i

    return result


def factorial_recursion(number: int) -> int:
    if number == 1:
        return 1
    return number * factorial_recursion(number - 1)


def main() -> None:
    user_input: int = int(input("Integer to factorial: "))
    print("-" * 40)
    print(f"Iteration: {factorial_iteration(user_input)}")
    print(f"Resucsion: {factorial_recursion(user_input)}")


if __name__ == "__main__":
    main()
