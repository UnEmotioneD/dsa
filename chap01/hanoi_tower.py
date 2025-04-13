def hanoi_tower(n: int, fr: str, temp: str, to: str) -> None:
    if n == 1:
        print(f'원판 1: {fr} --> {to}')
    else:
        hanoi_tower(n - 1, fr, to, temp)
        print(f'원판 {n}: {fr} --> {to}')
        hanoi_tower(n - 1, temp, fr, to)


def main() -> None:
    number_of_plate: int = 0

    while True:
        print('=' * 30)

        try:
            number_of_plate = int(input('원판의 갯수를 입력하시오: '))
            if number_of_plate <= 0:
                print('원판을 추가 하시오.')
                continue
            break

        except ValueError:
            print('정수를 입력하시오.')

    first_pole: str = 'A'
    second_pole: str = 'B'
    third_pole: str = 'C'
    hanoi_tower(number_of_plate, first_pole, second_pole, third_pole)


if __name__ == '__main__':
    main()
