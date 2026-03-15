def flatten(nested_list):
    """Flattens a nested list into a single list of values.

    Args:
        nested_list (list): A list that may contain other lists as elements.

    Returns:
        list: A flattened list containing all the values from the nested lists.
    """
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

lst = [1, [2, [3, 4], 5], 6, [7, 8]]
print(flatten(lst))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]