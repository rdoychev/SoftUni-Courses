def find_shortest_sub_array(nums: list[int]) -> int:
    from collections import Counter
    count = Counter(nums).most_common()

    prev_value = count[0][1]
    nums_len = len(nums)
    min_len = nums_len + 1

    for key, value in count:
        if value != prev_value:
            break
        start_idx = nums.index(key)
        end_idx = nums_len - 1 -nums[::-1].index(key)
        min_len = min(min_len, end_idx - start_idx + 1)
        prev_value = value

    return min_len


nums1 = [1,2,2,3,1]
print(find_shortest_sub_array(nums1))