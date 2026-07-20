def search_insert(nums, target) -> int:

    low = 0
    high = len(nums) - 1
    mid = low + (high - low) // 2

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if nums[mid] < target:
        return mid + 1
    return mid


nums1 = [1,3,5,6]
target1 = 7

print(search_insert(nums1, target1))
