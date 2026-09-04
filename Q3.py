def maximum_swap(num):
    digits = list(str(num))

    # Store the last index of each digit
    last_index = {}

    for i, digit in enumerate(digits):
        last_index[int(digit)] = i

    # Try to make the leftmost digit as large as possible
    for i, digit in enumerate(digits):
        current = int(digit)

        # Check larger digits from 9 down to current + 1
        for d in range(9, current, -1):
            if d in last_index and last_index[d] > i:
                # Swap
                j = last_index[d]
                digits[i], digits[j] = digits[j], digits[i]

                return int("".join(digits))

    # Already maximum
    return num


# Example
num = 2736

result = maximum_swap(num)
print(result)