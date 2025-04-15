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
    theList: list = [1, 2, 3, 4]

    # from -1 of list length
    # to index 0 (== -1 + 1)
    # by increment of -1
    for i in range(len(theList) - 1, -1, -1):
        print(f'{theList[i]}')


def main() -> None:
    # print_list_reverse()
    celsius_fahrenheit()


if __name__ == '__main__':
    main()
