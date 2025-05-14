import math


def ceil_up_to_n(number: int, digit: int) -> int:
    return int(math.ceil(number / digit) * digit)


def calculate_point_usage(balance: int, price: int, point: int) -> int:
    without_point: int = balance - price
    ceil_to: int = 10 ** len(str(point))
    ceiled: int = ceil_up_to_n(without_point, ceil_to)
    to_use: int = ceiled - without_point

    return to_use


def main() -> None:
    bank_balance: int = int(input('Enter remaining bank account: '))
    total_price: int = int(input('Price of purchase: '))
    available_point: int = int(input('Available points: '))

    point_to_use: int = calculate_point_usage(
        bank_balance, total_price, available_point
    )

    print(f'how_much_to_use: {point_to_use}')


if __name__ == '__main__':
    main()
