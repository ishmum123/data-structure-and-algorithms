from random import random


def get_random_numbers(n, maxim=10 ** 6, mini=0):
    return [int(random() * maxim) for _ in range(n)]


def quick_sort(arr):
    pass


def heap_sort(arr):
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


def merge_sort(arr, low=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if hi == low:
        return arr

    mid = (hi + low) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, hi)

    l1 = arr[low:mid + 1]
    l2 = arr[mid + 1:hi + 1]

    i1 = len(l1) - 1
    i2 = len(l2) - 1

    while i1 > -1 and i2 > -1:
        if l1[i1] > l2[i2]:
            arr[hi] = l1[i1]
            i1 -= 1
        else:
            arr[hi] = l2[i2]
            i2 -= 1
        hi -= 1

    while i1 > -1:
        arr[low + i1] = l1[i1]
        i1 -= 1

    while i2 > -1:
        arr[low + i2] = l2[i2]
        i2 -= 1

    return arr


if __name__ == '__main__':
    # n^2 sorting algorithms
    numbers = get_random_numbers(10 ** 3)
    print(insertion_sort(numbers.copy()))
    print(bubble_sort(numbers.copy()))

    # n*log(n) sorting algorithms
    numbers = get_random_numbers(10 ** 5)
    print(merge_sort(numbers.copy()))
