def intersect(nums1: list, nums2:list) -> list:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    intersect_out = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            nums2.remove(nums1[i])
            intersect_out.append(nums1[i])

    return  intersect_out


nums1a = [4,9,5]
nums2a = [9,4,9,8,4]
print(intersect(nums1a, nums2a))
