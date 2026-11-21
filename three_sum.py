"""Finds unique triplets in a list whose values sum to a target."""


def three_sum(values: list[int], target: int) -> list[list[int]]:
    """Return unique triplets whose values add up to target."""
    numbers = sorted(values)
    triplets = []

    for index in range(len(numbers) - 2):
        if index > 0 and numbers[index] == numbers[index - 1]:
            continue

        left = index + 1
        right = len(numbers) - 1
        while left < right:
            total = numbers[index] + numbers[left] + numbers[right]
            if total == target:
                triplets.append([numbers[index], numbers[left], numbers[right]])
                left += 1
                right -= 1

                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return triplets


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4], 0))
