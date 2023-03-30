def swap(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]


def pivot(lst, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if lst[i] < lst[pivot_index]:
            swap_index += 1
            swap(lst, swap_index, i)
    swap(lst, pivot_index, swap_index)
    return swap_index


def quicksort_helper(lst, left, right):
    if left < right:
        pivot_index = pivot(lst, left, right)
        quicksort_helper(lst, left, pivot_index-1)
        quicksort_helper(lst, pivot_index+1, right)
    return lst


def quicksort(lst):
    return quicksort_helper(lst, 0, len(lst) - 1)


my_list = [6,5,0,11,2,1,4,9,10]
print(quicksort(my_list))