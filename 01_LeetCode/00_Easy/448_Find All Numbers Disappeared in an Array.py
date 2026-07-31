def find_disappeared_numbers(nums: list) -> list:
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums_len = len(nums)
    missing_numbers = []

    for i in range(1, nums_len + 1):
        if i not in nums:
            missing_numbers.append(i)

    return missing_numbers


nums1 = [4,3,2,7,8,2,3,1]
print(find_disappeared_numbers(nums1))