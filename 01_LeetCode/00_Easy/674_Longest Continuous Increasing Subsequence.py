def find_length_of_lcis(nums: list[int]) -> int:
    if len(nums) == 1:
        return 1

    nums_len = len(nums)
    max_len = 1
    curr_len = 1

    for i in range(1, nums_len):
        if nums[i - 1] < nums[i]:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1

    return max_len


nums1 = [2,2,2,2,2]
print(find_length_of_lcis(nums1))