# def remove_element(nums, val) -> int:
#     count = 0
#     for i in range(len(nums) - 1, -1, -1):
#
#         if nums[i] == val:
#             count += 1
#             x = nums.pop(i)
#             nums.append(x)
#     print(nums)
#     return len(nums) - count


# def remove_element(nums, val) -> int:
#     nums = [x for x in nums if x != val]
#     print(nums)
#     return len(nums)


def remove_element(nums, val) -> int:

    idx = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[idx] = nums[i]
            idx += 1

    print(nums)
    return idx


nums1 = [3,2,2,3]
val1 = 3

print(remove_element(nums1, val1))