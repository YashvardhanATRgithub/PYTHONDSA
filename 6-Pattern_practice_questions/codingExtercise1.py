def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    
    lst = []
    str1 = ""
    for i in range(n):
        for j in range(n):
            str1 = str1 + "*"
        lst.append(str1)
        str1 = ""
        
    return lst
        
print(generate_square(3))