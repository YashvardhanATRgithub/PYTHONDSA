def next_greatest_letter(letters, target):
    # Implement the function logic
    n = len(letters)

    for i in range(n):
        letters[i] = ord(letters[i])
    
    target_ascii = ord(target)

    start, end = 0,n-1
    while start < end:
        mid = (start + end)//2

        if letters[mid] < target_ascii:
            start = mid+1
        if letters[mid] > target_ascii:
            end = mid-1

    if letters[mid] > target_ascii:
        return chr(letters[mid])



letters = ['c', 'f', 'j']
target = 'c'
print(next_greatest_letter(letters,target))
