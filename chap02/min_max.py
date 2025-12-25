from typing import List, Tuple


def min_max(numbers: List[int]) -> Tuple[int, int]:
    # initialize two variables in one line
    smallest = largest = numbers[0]

    for number in numbers[1:]:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    return smallest, largest


def main() -> None:
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    smallest, largest = min_max(data)

    print(f"Smallest value: {smallest}")
    print(f"Biggest value: {largest}")


if __name__ == "__main__":
    main()
