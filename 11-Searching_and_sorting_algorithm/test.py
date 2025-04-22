def selection_sort(lst):
    # Your code goes here

    n = len(lst)

    for i in range(n):
        min = i
        k = i
        j = i + 1
        while j < n:
            if lst[j] < lst[k]:
                k  = j
            j += 1
        lst[min], lst[k] = lst[k], lst[min]

    return lst


lst = [29, 10, 14, 37, 13]
print(selection_sort(lst))    