def array_pair_sum(nums: list[int]) -> int:
    # if len(nums) == 2:
    #     return min(nums)
    #
    # nums.sort()
    # max_sum = 0
    # for i in range(0, len(nums), 2):
    #     max_sum += min(nums[i], nums[i + 1])
    #
    # return max_sum

    return sum(sorted(nums)[::2])


nums1 = [6,2,6,5,1,2]
print(array_pair_sum(nums1))
