def missing_number(nums: list) -> int:
    max_num = len(nums)
    total_sum = max_num * (max_num + 1) // 2
    for num in nums:
           total_sum -= num

    return total_sum




nums1 = [9,6,4,2,3,5,7,0,1]
print(missing_number(nums1))
