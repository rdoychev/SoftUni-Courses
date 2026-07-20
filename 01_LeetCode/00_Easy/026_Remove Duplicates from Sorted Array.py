def remove_duplicates(nums: list) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    len_nums = len(nums)
    # if len_nums == 1:
    #     return 1
    for idx in range(len(nums) - 1, -1, -1):
        if nums[idx] == nums[idx - 1] and idx != 0:
            count += 1
            nums.pop(idx)
        else:
            continue

    return len_nums - count


inp = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(f"Number of unique elements: {remove_duplicates(inp)}")