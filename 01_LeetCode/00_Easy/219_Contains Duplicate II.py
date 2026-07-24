def contains_nearby_duplicate(nums, k) -> bool:
    # hash_map = {}
    # for idx, num in enumerate(nums):
    #     if num in hash_map and abs(idx - hash_map[num]) <= k:
    #         return True
    #     else:
    #         hash_map[num] = idx
    # return False
    if len(nums) == len(set(nums)):
        return False
    for i, n in enumerate(nums):
        if n in nums[i + 1:i + k + 1]:
            return True
    return False

nums1 = [1,2,3,1,2,3]
k1 = 2
print(contains_nearby_duplicate(nums1, k1))