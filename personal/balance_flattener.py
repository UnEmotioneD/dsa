import math


def ceil_up_to_n(number: int, digit: int) -> int:
    target: int = int(math.ceil(number / digit) * digit)
    return target


def calculate_point_usage(balance: int, price: int, point: int) -> int:
    without_point: int = balance - price
    ceil_to: int = 10 ** len(str(point))

    ceiled: int = ceil_up_to_n(without_point, ceil_to)
    print(f'ceiled: {ceiled}')

    to_use: int = ceiled - without_point

    return to_use


def floor_it(number: int, digit: int) -> int:
    target: int = int(math.floor(number / digit) * digit)
    return target


def foobar(balance: int, price: int, point: int) -> int:
    print(f'point: {point}')
    print(f'price: {price}')
    print(f'balance: {balance}')

    no_point = balance - price
    print(f'no_point: {no_point}')

    add_up: int = no_point + point
    print(f'add_up: {add_up}')

    point_digit: int = len(str(point))
    ceiled_add_up: int = floor_it(add_up, 10**point_digit)
    print(f'ceile_add_up: {ceiled_add_up}')

    print(f'{ceiled_add_up - no_point}')

    return 0


def main() -> None:
    # bank_balance: int = int(input('Enter remaining bank account: '))
    # total_price: int = int(input('Price of purchase: '))
    # available_point: int = int(input('Available points: '))

    bank_balance: int = 480_442
    total_price: int = 6_100
    available_point: int = 944

    # point_to_use: int = calculate_point_usage( bank_balance, total_price, available_point)

    point_to_use: int = foobar(bank_balance, total_price, available_point)

    print(f'how_much_to_use: {point_to_use}')


if __name__ == '__main__':
    main()
