def find_error_nums(nums: list) -> list:
    n = len(nums)
    s = n * (n + 1) // 2
    miss = s - sum(set(nums))
    duplicate = sum(nums) + miss - s
    return [duplicate, miss]


nums1 = [2,3,2]
print(find_error_nums(nums1))
