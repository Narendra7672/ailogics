def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


nums = [2, 2, 1, 1, 1, 2, 2]

result = majority_element(nums)
print(result)






# git remote add origin https://github.com/Narendra7672/Ai-logics-Assessment.git
#git remote add origin https://github.com/Narendra7672/ailogics.git