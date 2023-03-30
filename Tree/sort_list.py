# sort a list using recursion

def sort_list(lst, ind, num_loops=0):
    if ind + 1 == len(lst):
        return lst
    if lst[ind] < lst[ind+1]:
        lst[ind], lst[ind+1] = lst[ind+1], lst[ind]
    sort_list(lst, ind+1, num_loops+1)


lst = [5, 10, -15, 0, 7, 35, -40, 100, 3, -20, 75]

for _ in range(len(lst)):
    sort_list(lst, 0)
print(lst)