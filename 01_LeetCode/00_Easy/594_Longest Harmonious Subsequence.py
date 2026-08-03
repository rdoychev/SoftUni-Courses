def find_lhs(nums: list[int]) -> int:
    from collections import Counter
    common = Counter(nums)

    if len(common) == 1:
        return 0

    max_len = 0
    for key in common.keys():
        if key + 1 in common.keys():
                max_len = max(max_len, common[key] + common[key + 1])

    return max_len


    # nums.sort()
    # j = 0
    # ans = 0
    #
    # for i in range(len(nums)):
    #     while nums[i] - nums[j] > 1:
    #         j += 1
    #
    #     if nums[i] - nums[j] == 1:
    #         ans = max(ans, i - j + 1)
    #
    # return ans


nums1 = [1,3,2,2,5,2,3,7,7,7,7,7,7,7]
print(find_lhs(nums1))
