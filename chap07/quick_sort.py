import random
import time


def swap(arr: list[int], i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr: list[int], low: int, high: int) -> int:
    # Choose the pivot
    pivot = arr[high]

    # Index of smaller element and indicates
    #  the right position of pivot found so far
    i = low - 1

    # Traverse arr[low..high] and move all smaller elements to the left side.
    # Elements from low to i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # Move pivot after smaller elements and
    #  return its position
    swap(arr, i + 1, high)
    return i + 1


def quick_sort(arr: list[int], low: int, high: int) -> None:
    if low < high:
        # Partition return index of pivot
        part_index = partition(arr, low, high)

        # Recursion calls for smaller elements
        quick_sort(arr, low, part_index - 1)
        #  and greater or equals elements
        quick_sort(arr, part_index + 1, high)


def print_array(arr: list[int]) -> None:
    for val in arr:
        print(val, end=' ')
        if val == arr[LENGTH - 1]:
            print()


if __name__ == '__main__':
    array = list(range(10))
    random.shuffle(array)
    LENGTH = len(array)

    print('Before sort: ')
    print_array(array)

    start: float = time.time()
    quick_sort(array, 0, LENGTH - 1)
    end: float = time.time()

    print('\nAfter sort: ')
    print_array(array)

    print(f'\nTime took: {end - start}')
