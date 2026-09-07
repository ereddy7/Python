
def sum_all(*args):
    """
    Calculate the sum of all provided arguments.
    
    Args:
        *args: A variable number of numeric arguments.
    
    Returns:
        int: The sum of all provided arguments.
    """
    total = 0
    for num in args:
        total += num
    return total

total = sum_all(10)
print("Total sum is", total)

total = sum_all(10,23)
print("Total sum is", total)

total = sum_all(10,23,45,67,89,90)
print("Total sum is", total)