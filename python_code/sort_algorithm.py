# -*- coding: utf-8 -*-


def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        base = alist[0]
        i = 1
        j = len(alist)-1
        found_i = False
        found_j = False
        while i <= j:
            if alist[i] < base:
                i += 1
            else:
                found_i = True

            if alist[j] > base:
                j -= 1
            else:
                found_j = True

            if found_i and found_j:
                alist[i], alist[j] = alist[j], alist[i]
                i += 1
                j -= 1
                found_i = False
                found_j = False
        alist[0], alist[j] = alist[j], alist[0]
        left = quick_sort(alist[:j])
        right = quick_sort(alist[i:])
        return left + [alist[j]] + right


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def partition(arr, low, high):
    pivot = low
    for i in range(low+1, high+1):
        if arr[i] < arr[low]:
            pivot += 1
            arr[pivot], arr[i] = arr[i], arr[pivot]
    arr[pivot], arr[low] = arr[low], arr[pivot]
    return pivot


def quicksort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort_inplace(arr, low, pi-1)
        quicksort_inplace(arr, pi+1, high)


def bubble_sort(alist):
    for j in range(len(alist)-1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def short_bubble_sort(alist):
    exchanges = True
    n = len(alist)-1
    while n > 0 and exchanges:
        exchanges = False
        for i in range(n):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        n -= 1


def select_sort(alist):
    for j in range(len(alist)-1, 0, -1):
        max_index = 0
        for i in range(1, j+1):
            if alist[i] > alist[max_index]:
                max_index = i
        alist[j], alist[max_index] = alist[max_index], alist[j]


def insert_sort(alist):
    for i in range(1, len(alist)):
        current_value = alist[i]

        while i > 0 and alist[i-1] > current_value:
            alist[i] = alist[i-1]
            i -= 1
        alist[i] = current_value


def gap_insert_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        current_value = alist[i]

        while i >= gap and alist[i-gap] > current_value:
            alist[i] = alist[i-gap]
            i -= gap
        alist[i] = current_value


def shell_sort(alist):
    gap = len(alist) // 2

    while gap > 0:
        for i in range(gap):
            gap_insert_sort(alist, i, gap)
        gap = gap // 2


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        s = len(alist) // 2
        left = merge_sort(alist[:s])
        right = merge_sort(alist[s:])
        return merge(left, right)


def merge(l, r):
    a = []
    while len(l) > 0 and len(r) > 0:
        if l[0] <= r[0]:
            a.append(l[0])
            l.pop(0)
        else:
            a.append(r[0])
            r.pop(0)

    for i in l:
        a.append(i)
    for i in r:
        a.append(i)

    return a


if __name__ == '__main__':

    a = [3, 1, 1, 5, 9, 7, 11, 9]
    b = [3, 6, 8, 19, 1, 5]
    # aa = quick_sort(a)
    # aa = quicksort(b)
    # quicksort_inplace(a, 0, len(a)-1)
    # short_bubble_sort(a)
    # select_sort(a)
    # insert_sort(a)
    # shell_sort(a)
    a = merge_sort(b)
    print(a)
