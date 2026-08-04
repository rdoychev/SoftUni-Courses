def maximum_product(nums: list) -> int:
    nums.sort()
    max_product = max(nums[-1] * nums[-2] * nums[-3],
                      nums[-1] * nums[1] * nums[0])

    return max_product


nums1 = [1,2,3]
print(maximum_product(nums1))