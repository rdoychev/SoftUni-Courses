def find_max_average(nums: list, k: int) -> float:
    max_sum = sum(nums[:k])
    curr_sum = max_sum

    for idx in range(k, len(nums)):
        curr_sum += nums[idx] - nums[idx - k]
        max_sum = max(max_sum, curr_sum)

    return max_sum / k



nums1 = [1,12,-5,-6,50,3]
k1 = 4
print(find_max_average(nums1, k1))