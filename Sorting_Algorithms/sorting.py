# sorting algorithms
import math


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)


def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    print(lst)


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


def bucket_sort(lst):
    num_of_buckets = round(math.sqrt(len(lst)))
    max_value = max(lst)
    arr = []

    for _ in range(num_of_buckets):
        arr.append([])
    for j in lst:
        index_b = math.ceil(j*num_of_buckets/max_value)
        arr[index_b-1].append(j)

    for i in range(num_of_buckets):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(num_of_buckets):
        for j in range(len(arr[i])):
            lst[k] = arr[i][j]
            k += 1
    return lst


def merge(lst, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = lst[l+i]

    for j in range(n2):
        R[j] = lst[m+1+j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        customlst[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customlst[k] = R[j]
        j += 1
        k += 1


def mergesort(lst, l, r):
    if l < r:
        m = (l + (r - 1))//2
        mergesort(lst, l, m)  # lst
        mergesort(lst, m+1, r) # lst
        merge(lst, l, m, r)
    return lst


def heapify(lst, n, i):
    smallest = i
    left = i*2 + 1
    right = i*2 + 2

    if left < n and lst[left] < lst[smallest]:
        smallest = left

    if right < n and lst[right] < lst[smallest]:
        smallest = right

    if smallest != i:
        lst[i], lst[smallest] = lst[smallest], lst[i]
        heapify(lst, n, smallest)


def heapsort(lst):
    n = len(lst)
    for i in range(int(n/2)-1, -1, -1):
        heapify(lst, n, i)

    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    lst.reverse()


customlst = [4,9,2,6,3,10,1,8,5,7]
heapsort(customlst)
print(customlst)
