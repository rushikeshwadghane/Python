"""Finds the first index of a target value in a sorted list."""


def first_occurrence(values, target):
    """Return the first matching index, or -1 when the target is absent."""
    low = 0
    high = len(values) - 1
    result = -1

    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            result = middle
            high = middle - 1
        elif values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return result


if __name__ == "__main__":
    sample = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5]
    print(first_occurrence(sample, 3))
