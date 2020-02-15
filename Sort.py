from random import random

from Utils import get_random_numbers, measure


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


def heapify(arr, i):
    ridx = (2 * i + 2)
    lidx = (2 * i + 1)

    if ridx < len(arr):
        r = arr[ridx]
        l = arr[lidx]
        m = arr[i]

        if m > r or m > l:
            if l > r:
                arr[i] = r
                arr[ridx] = m
                heapify(arr, ridx)
            else:
                arr[i] = l
                arr[lidx] = m
                heapify(arr, lidx)
    elif lidx < len(arr):
        l = arr[lidx]
        m = arr[i]
        if m > l:
            arr[i] = l
            arr[lidx] = m


def heap_sort(arr):
    narr = []
    for i in reversed(range(len(arr))):
        heapify(arr, i)
    while arr:
        narr.append(arr[0])
        tmp = arr.pop()
        if arr:
            arr[0] = tmp
            heapify(arr, 0)
    return narr


def quick_sort(arr):
    pass


if __name__ == '__main__':
    # n^2 sorting algorithms
    numbers = get_random_numbers(10 ** 3)
    measure(lambda: print(insertion_sort(numbers.copy())))
    measure(lambda: print(bubble_sort(numbers.copy())))

    # n*log(n) sorting algorithms
    numbers = get_random_numbers(10 ** 5)
    measure(lambda: print(merge_sort(numbers.copy())))
    measure(lambda: print(heap_sort(numbers.copy())))
