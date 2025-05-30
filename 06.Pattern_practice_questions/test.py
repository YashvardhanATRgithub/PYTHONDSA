def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    lst = []
    
    for i in range(n):
        if i == 0 or i == n-1:
            str1 = '*' * n
        else:
            str1 = '*' + (" " * (n-2)) + '*'
        lst.append(str1)
    return lst

print(generate_hollow_square(3))