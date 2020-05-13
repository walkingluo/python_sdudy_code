# -*- coding:utf-8 -*-


def binary_search(alist, key):
    '''
    binary_search by iteration
    '''
    first = 0
    last = len(alist)-1
    found = False
    index = None

    while first <= last and not found:
        mid = (last + first) // 2
        if alist[mid] == key:
            found = True
            index = mid
        else:
            if alist[mid] < key:
                first = mid + 1
            else:
                last = mid - 1

    return found, index


def binary_search_recursion(alist, key):
    '''
    binary_search by recursion
    '''
    if len(alist) == 0:
        return False, None
    else:
        mid = len(alist) // 2
        if alist[mid] == key:
            return True, mid
        else:
            if alist[mid] < key:
                return binary_search_recursion(alist[mid+1:], key)
            else:
                return binary_search_recursion(alist[:mid], key)


a = [1, 3, 5, 7, 9, 11]
b = []
c = [6]
# r, i = binary_search(c, 6)
r, i = binary_search_recursion(b, 6)
print(r, i)
