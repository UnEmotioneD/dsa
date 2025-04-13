import time


def contains(bag, item):
    return item in bag


def insert(bag, item):
    bag.append(item)


def remove(bag, item):
    bag.remove(item)


def count(bag):
    return len(bag)


def num_of(bag, item):
    return bag.count(item)


def main():
    my_bag: list = []

    start = time.time()

    insert(my_bag, 'phone')
    insert(my_bag, 'wallet')
    insert(my_bag, 'handkerchief')
    insert(my_bag, 'comb')
    insert(my_bag, 'book')
    insert(my_bag, 'baseball')

    print('Items in the bag:', my_bag)
    print(f'Duration of the first task: {(time.time() - start) * 1000:.6f} ms')
    print('')

    insert(my_bag, 'comb')
    remove(my_bag, 'handkerchief')

    print('Items in the bag:', my_bag)
    print(f'Duration of the second task: {(time.time() - start) * 1000:.6f} ms')
    print('')

    target_item = input('Enter the name of the item to count: ')
    print(f'{target_item}: {num_of(my_bag, target_item)} item(s)')
    print(f'Total duration: {(time.time() - start):.6f} sec')


if __name__ == '__main__':
    main()
