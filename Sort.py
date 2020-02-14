from random import random


def get_random_numbers(n, maxim=10 ** 6, mini=0):
    return [int(random() * maxim) for _ in range(n)]


def quick_sort(arr):
    pass


def heap_sort(arr):
    pass


def merge_sort(arr):
    pass


def bubble_sort(arr):
    if len(arr) < 2:
        return arr

    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                tmp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = tmp

    return arr


def insertion_sort(arr):
    narr = []
    for x in arr:
        idx = len(narr) - 1
        while idx > -1 and narr[idx] > x:
            idx -= 1
        narr.insert(idx + 1, x)
    return narr


if __name__ == '__main__':
    print(insertion_sort(get_random_numbers(10 ** 3)))
    print(bubble_sort(get_random_numbers(10 ** 3)))
