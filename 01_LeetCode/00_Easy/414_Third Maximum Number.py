def third_max(nums: list) -> int:
    # if len(nums) < 3:
    #     return max(nums)
    #
    # from sys import maxsize
    # first = -maxsize
    # second = -maxsize
    # third = -maxsize
    #
    # for idx in range(len(nums)):
    #     if nums[idx] != first and nums[idx] != second and nums[idx] != third:
    #         if nums[idx] > first:
    #             third = second
    #             second = first
    #             first = nums[idx]
    #         elif nums[idx] > second:
    #             third = second
    #             second = nums[idx]
    #         elif nums[idx] > third:
    #             third = nums[idx]
    # if third != -maxsize:
    #     return third
    # else:
    #     return max(first, second)

    if len(nums) < 3:
        return max(nums)

    a = sorted(list(set(nums)), reverse=True)
    if len(a) < 3:
        return max(a)
    return a[2]


nums1 = [1,1,5,4, 2]
print(third_max(nums1))