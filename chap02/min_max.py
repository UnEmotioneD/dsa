def min_max(numbers: list[int]) -> tuple[int, int]:
    # initialize two variables in one line
    smallest = largest = numbers[0]

    for number in numbers[1:]:
        smallest = min(smallest, number)
        largest = max(largest, number)

    return smallest, largest


def main() -> None:
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    smallest, largest = min_max(data)

    print(f'Smallest value: {smallest}')
    print(f'Biggest value: {largest}')


if __name__ == '__main__':
    main()
