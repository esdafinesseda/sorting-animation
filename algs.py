"""
Add own sorting algorithms in here.

NOTE: you should use yield every time you want the array to refresh 
and each yield call should contain the full updated array
"""

import random

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot_idx = start
    pivot = array[end]
    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
            pivot_idx += 1
        yield array
    array[end], array[pivot_idx] = array[pivot_idx], array[end]
    yield array

    yield from quick_sort(array, start, pivot_idx - 1)
    yield from quick_sort(array, pivot_idx + 1, end)

def bubble_sort(array, start, end):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j+1], array[j]
                swapped = True
                yield array
                
        if not swapped:
            break

def _is_sorted(array):
    for i in range(0, len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

def _shuffle(array):
    n = len(array)

    for i in range(0, n):
        r = random.randint(0, n-1)
        array[i],array[r] = array[r], array[i]


def bogo_sort(array, start, end):
    yield array
    while not _is_sorted(array):
        _shuffle(array)
        yield array
