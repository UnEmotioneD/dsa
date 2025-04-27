"""
Chapter 02 practice
"""


# 2.5
def celsius_fahrenheit() -> None:
    cel: float = float(input('Enter temperature for celsius: '))

    fah: float = 32 + ((180 / 100) * cel)

    print(f'Celsius to fahrenheit: {fah} 󰔅 ')

    cel = (fah - 32) * (100 / 180)

    print(f'Fahrenheit to celsius: {cel} 󰔄 ')


# 2.6
def print_list_reverse() -> None:
    the_list: list = [1, 2, 3, 4]

    # from -1 of list length
    # to index 0 (== -1 + 1)
    # by increment of -1
    for i in range(len(the_list) - 1, -1, -1):
        print(f'{the_list[i]}')


# 2.8
# ord(char): turn char into unicode integer
# chr(integer): tun integer into character
# enumerate: iterate and loop at the same time
def string_upper_lower() -> None:
    msg: str = 'Data Structure in Python'

    def to_upper_case(msg_to_upper: str) -> str:
        upper_msg: str = ''

        for i, c in enumerate(msg_to_upper):
            c = msg_to_upper[i]
            if 'a' <= c <= 'z':
                upper_msg += chr(ord(c) - 32)
            else:
                upper_msg += c

        return upper_msg

    def to_lower_case(msg_to_lower) -> str:
        lower_msg = ''

        for i, c in enumerate(msg_to_lower):
            c = msg_to_lower[i]
            if 'A' <= c <= 'Z':
                lower_msg += chr(ord(c) + 32)
            else:
                lower_msg += c

        return lower_msg

    print(f'Original message: {msg}')
    print('-' * 50)
    print(f'Message in upper case: {to_upper_case(msg)}')
    print(f'Message in lower case: {to_lower_case(msg)}')


# 2.10
# 1 + 1/2 + ... + 1/n
def harmonic_series() -> None:
    user_input = int(
        input('Enter natual number to calculate harmonic series to: ')
    )

    def harmonic_iter(num: int) -> None:
        result: float = 0
        for n in range(1, num + 1):
            print(f'1/{n}', end='')
            if n != num:
                print(' + ', end='')
            elif n == num:
                print()
            result = result + (1 / n)
        print(f'result: {result}')

    def harmonic_recur(num: int) -> float:
        if num != 1:
            print(f'1/{num} + ', end='')
        if num == 1:
            print('1')
            return 1.0
        return (1 / num) + harmonic_recur(num - 1)

    harmonic_iter(10)
    print(f'Result: {harmonic_recur(user_input)}')


# 2.11
# binomial coefficient
def binomial():
    print('Binomial_coefficient.')
    input_n: int = int(input('Enter value of n: '))
    input_k: int = int(input('Enter value of k: '))

    def bino_iter(n: int, k: int) -> int:
        print(f'input_n: {n}')
        print(f'input_k: {k}')

        fac_n: int = factorial_iterative(n)
        fac_k: int = factorial_iterative(k)
        fac_sub: int = factorial_iterative(n - k)

        return fac_n // (fac_k * fac_sub)

    result = bino_iter(input_n, input_k)
    print(f'Binomial coefficient (n choose k) is: {result}')


# 2.11-1
def factorial_iterative(target: int) -> int:
    result: int = 1
    for i in range(1, target + 1):
        result *= i

    return result


def main() -> None:
    # print_list_reverse()
    # celsius_fahrenheit()
    # string_upper_lower()
    # harmonic_series()
    binomial()


if __name__ == '__main__':
    main()
