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
# ord(char) : turn char into unicode integer
# chr(integer) : tun integer into character
def string_upper_lower() -> None:
    msg: str = 'Data Structure in Python'

    def to_upper_case(msg_to_upper: str) -> str:
        upper_msg: str = ''

        for i in range(len(msg_to_upper)):
            c = msg_to_upper[i]
            if 'a' <= c <= 'z':
                upper_msg += chr(ord(c) - 32)
            else:
                upper_msg += c

        return upper_msg

    def to_lower_case(msg_to_lower) -> str:
        lower_msg = ''

        for i in range(len(msg_to_lower)):
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


def main() -> None:
    # print_list_reverse()
    # celsius_fahrenheit()
    string_upper_lower()


if __name__ == '__main__':
    main()
