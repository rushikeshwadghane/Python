def reverse_integer(x): 
    """
    Reverses the digits of an integer.

    Args:
        x (int): The integer to be reversed.

    Returns:
        int: The reversed integer. If the reversed integer overflows
             32-bit signed integer range, returns 0.
    """
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reversed_str = str(x_abs)[::-1]
    reversed_int = sign * int(reversed_str)

    if reversed_int < INT_MIN or reversed_int > INT_MAX:
        return 0
    return reversed_int


# Example usage
num = -12345    
print(reverse_integer(num))  # Output: -54321