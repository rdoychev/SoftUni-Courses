def intersection(nums1: list, nums2: list) -> list:
    return list(set(nums1) & set(nums2))


nums1a = [1,2,2,1]
nums22 = [2,2]
print(intersection(nums1a, nums22))
