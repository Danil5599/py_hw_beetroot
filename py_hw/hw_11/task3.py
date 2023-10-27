def choose_func(nums: list, func1, func2):
    if all(map(lambda x: x > 0, nums)):
        return func1(nums)
    else:
        return func2(nums)

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

result1 = choose_func(nums1, square_nums, remove_negatives)
result2 = choose_func(nums2, square_nums, remove_negatives)

print(f"Результат для nums1: {result1}")
print(f"Результат для nums2: {result2}")

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]