import time


def partition(arr, low, high):
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


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if low < high:
        # Partition return index of pivot
        part_index = partition(arr, low, high)

        # Recursion calls for smaller elements
        quick_sort(arr, low, part_index - 1)
        #  and greater or equals elements
        quick_sort(arr, part_index + 1, high)


if __name__ == '__main__':
    array = [4, 3, 8, 1, 2, 5, 9, 7, 0, 6]
    LENGTH = len(array)

    start = time.time()
    quick_sort(array, 0, LENGTH - 1)
    end = time.time()

    for val in array:
        print(val, end=' ')
        if val == array[LENGTH - 1]:
            print()

    print(f'Time took: {end - start}')
