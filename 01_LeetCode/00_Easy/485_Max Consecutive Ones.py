def find_max_consecutive_ones(nums: list) -> int:
    max_consecutive_ones = 0
    s_idx = 0
    e_idx = 0
    is_one = False

    for idx in range(len(nums)):
        if nums[idx] == 1 and is_one:
            e_idx += 1
            continue
        elif nums[idx] == 1:
            s_idx = idx
            e_idx = idx + 1
            is_one = True
        else:
            max_consecutive_ones = max(max_consecutive_ones, e_idx - s_idx)
            is_one = False

    max_consecutive_ones = max(max_consecutive_ones, e_idx - s_idx)
    return max_consecutive_ones


nums1 = [0, 1]
print(find_max_consecutive_ones(nums1))
