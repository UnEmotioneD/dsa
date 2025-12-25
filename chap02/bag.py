import time


def contain(space, e):
    return e in space


def insert(space, e):
    space.append(e)


def remove(space, e):
    space.remove(e)


def count(space):
    return len(space)


if __name__ == "__main__":
    bag = []

    start = time.time()
    insert(bag, "휴대폰")
    insert(bag, "지갑")
    insert(bag, "손수건")
    insert(bag, "빗")
    insert(bag, "자료구조")
    insert(bag, "야구공")
    end = time.time()
    duration = end - start
    print("가방속 물건: ", bag)
    print("걸린 시간 : ", duration)

    insert(bag, "빗")
    remove(bag, "손수건")
    end = time.time()
    print("가방속 물건: ", bag)
    print("걸린 시간 : ", duration)
