import time


def contain(space: list[str], e: str) -> bool:
    return e in space


def insert(space: list[str], e: str) -> None:
    space.append(e)


def remove(space: list[str], e: str) -> None:
    space.remove(e)


def count(space: list[str]) -> int:
    return len(space)


def main() -> None:
    bag: list[str] = []

    start = time.time()

    insert(bag, '휴대폰')
    insert(bag, '지갑')
    insert(bag, '손수건')
    insert(bag, '빗')
    insert(bag, '자료구조')
    insert(bag, '야구공')

    end = time.time()
    duration = end - start

    print('가방속 물건: ', bag)
    print('걸린 시간 : ', duration)

    insert(bag, '빗')
    remove(bag, '손수건')

    end = time.time()

    print('가방속 물건: ', bag)
    print('걸린 시간 : ', duration)


if __name__ == '__main__':
    main()
