def bubble_sort(lst):
    # Your code goes here
    
    k = 0
    size = len(lst)
    
    while k < size-1:
        j = 0
        while j < size-k-1:
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            j += 1
        k += 1
        
    return lst

lst = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(lst))