def contains_duplicate(nums:list) -> bool:
    if len(nums) == len(set(nums)):
        return False
    else:
        return True


nums1 = [1,2,3,4]
print(contains_duplicate(nums1))