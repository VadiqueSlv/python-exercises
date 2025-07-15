def remove_max(nums):
    max_value = max(nums)
    result = []
    for x in nums:
        if x != max_value:
           result.append(x)
    return result

numbers = list(map(int, input("Enter numbers: ").split()))

print(remove_max(numbers))