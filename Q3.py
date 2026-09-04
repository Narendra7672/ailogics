def maximum_swap(num):
    digits = list(str(num))
    last_index = {}

    for i, digit in enumerate(digits):
        last_index[int(digit)] = i

    
    for i, digit in enumerate(digits):
        current = int(digit)

        
        for d in range(9, current, -1):
            if d in last_index and last_index[d] > i:
                
                j = last_index[d]
                digits[i], digits[j] = digits[j], digits[i]

                return int("".join(digits))

    
    return num



num = 2736

result = maximum_swap(num)
print(result)